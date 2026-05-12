import tkinter as tk
from tkinter import Frame, Label, Button, Entry
from faqtree import FAQ_TREE

# ==========================
#   Dymek Chatu
# ==========================
class ChatBubble(Frame):
    def __init__(self, master, text, side="left", bg="#e0e0e0", wrap=300):
        super().__init__(master, bg=master['bg'])
        self.pack(fill="x", pady=4, padx=6)

        self.label = Label(
            self,
            text=text,
            bg=bg,
            fg="black",
            wraplength=wrap,
            justify="left",
            padx=12,
            pady=8,
            bd=0
        )

        if side == "right":
            self.label.pack(anchor="e")
        else:
            self.label.pack(anchor="w")
# ==========================
#   Główna aplikacja
# ==========================
class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot FAQ")
        self.root.geometry("600x780")
        self.mode = "bot"

        # ---- GRID UKŁAD ----
        root.grid_rowconfigure(0, weight=1)
        root.grid_rowconfigure(1, weight=0)
        root.grid_rowconfigure(2, weight=0)
        root.grid_columnconfigure(0, weight=1)

        # CHAT FRAME
        self.chat_frame = Frame(root, bg="#f5f5f5")
        self.chat_frame.grid(row=0, column=0, sticky="nsew")

        self.canvas = tk.Canvas(self.chat_frame, bg="#f5f5f5", highlightthickness=0)
        self.canvas.pack(side="left", fill="both", expand=True)

        self.scrollbar = tk.Scrollbar(self.chat_frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.inner_frame = Frame(self.canvas, bg="#f5f5f5")
        self.window_item = self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")

        self.canvas.bind("<Configure>", self._on_canvas_resize)
        self.inner_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel_windows)
        self.canvas.bind_all("<Button-4>", self._on_mousewheel_linux)
        self.canvas.bind_all("<Button-5>", self._on_mousewheel_linux)
        
        self.options_frame = Frame(root, bg="#ffffff")
        self.options_frame.grid(row=1, column=0, sticky="ew", pady=4)

        self.input_frame = Frame(root, bg="#ffffff")
        self.input_frame.grid(row=2, column=0, sticky="ew")

        self.entry = Entry(self.input_frame, font=("Arial", 12))
        self.entry.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
        self.entry.bind("<Return>", lambda e: self.send_user_message())

        self.input_frame.grid_columnconfigure(0, weight=1)

        self.send_btn = Button(self.input_frame, text="Wyślij", command=self.send_user_message)
        self.send_btn.grid(row=0, column=1, padx=10, pady=10)

        self.state = "START"

        self.show_bot_message(FAQ_TREE["START"]["message"])
        self.show_options(FAQ_TREE["START"]["options"], is_main_menu=True)

    def _on_canvas_resize(self, event):
        self.canvas.itemconfig(self.window_item, width=event.width)
        
    # --- HANDLERY SCROLLA ---
    def _on_mousewheel_windows(self, event):
        try:
            self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        except Exception:
            pass

    def _on_mousewheel_linux(self, event):
        if event.num == 4:
            self.canvas.yview_scroll(-1, "units")
        elif event.num == 5:
            self.canvas.yview_scroll(1, "units")

    def show_bot_message(self, text):
        wrap = int(self.root.winfo_width() * 0.6)
        ChatBubble(self.inner_frame, text, side="left", bg="#e8e8e8", wrap=wrap)
        self.scroll_to_end()

    def show_user_message(self, text):
        wrap = int(self.root.winfo_width() * 0.6)
        ChatBubble(self.inner_frame, text, side="right", bg="#a8d5ff", wrap=wrap)
        self.scroll_to_end()

    def scroll_to_end(self):
        self.canvas.update_idletasks()
        self.canvas.yview_moveto(1.0)

    def show_options(self, options, is_main_menu=False):
        for w in self.options_frame.winfo_children():
            w.destroy()

        for text, next_state in options.items():
            btn = Button(
                self.options_frame,
                text=text,
                wraplength=int(self.root.winfo_width() * 0.50),
                justify="left",
                bd=0,
                bg="#a8d5ff",
                activebackground="#7fbfff",
                padx=12,
                pady=8,
                command=lambda t=text, n=next_state: self.option_clicked(t, n)
            )
            btn.pack(anchor="e", padx=10, pady=4)

        if not is_main_menu:
            back_btn = Button(
                self.options_frame,
                text="Powrót",
                wraplength=int(self.root.winfo_width() * 0.50),
                justify="left",
                bd=0,
                bg="#a8d5ff",
                activebackground="#7fbfff",
                padx=12,
                pady=8,
                command=self.reset_to_start
            )
            back_btn.pack(anchor="e", padx=10, pady=6)

    def option_clicked(self, text, next_state):
        if self.mode == "consultant":
            return

        self.show_user_message(text)

        self.state = next_state

        bot_msg = FAQ_TREE[next_state]["message"]
        self.show_bot_message(bot_msg)

        next_options = FAQ_TREE[next_state].get("options", {})
        if next_options:
            self.show_options(next_options)
        else:
            pass

    def send_user_message(self):
        text = self.entry.get().strip()
        if not text:
            return
        self.entry.delete(0, tk.END)

        self.show_user_message(text)

        if self.mode == "consultant":
            return

        if text.lower() == "chcę rozmawiać z konsultantem":
            self.mode = "consultant"
            self.show_bot_message("Łączę z konsultantem… Proszę o chwilę cierpliwości.")
            for w in self.options_frame.winfo_children():
                w.destroy()
            return

        self.show_bot_message(
            "Proszę korzystać z gotowych dymków z pytaniami (po prawej).\n"
            "Aby rozmawiać z konsultantem, wpisz: „chcę rozmawiać z konsultantem”."
        )

    def reset_to_start(self):
        if self.mode == "consultant":
            return
        self.show_options(FAQ_TREE["START"]["options"], is_main_menu=True)
# ==========================
#   Uruchomienie Aplikacji
# ==========================
if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()