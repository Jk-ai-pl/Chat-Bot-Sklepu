FAQ_TREE = {
    "START": {
        "message": "W czym mogę pomóc?",
        "options": {
            "Mam pytanie odnośnie zamówienia": "ORDER",
            "Chcę dowiedzieć się o dostawie": "DELIVERY",
            "Potrzebuję pomocy z produktem": "PRODUCT"
        }
    },

    # ------ ZAMÓWIENIA ------
    "ORDER": {
        "message": "Jasne, słucham. W czym mogę pomóc w kwestii zamówienia?",
        "options": {
            "Jak złożyć zamówienie?": "ORDER_HOW",
            "Chcę anulować zamówienie": "ORDER_CANCEL",
            "Gdzie sprawdzę status zamówienia?": "ORDER_STATUS"
        }
    },
    "ORDER_HOW": {
        "message": "Aby złożyć zamówienie: wybierz produkt, dodaj do koszyka i przejdź do kasy. Co chcesz wiedzieć dokładniej?",
        "options": {
            "Płatności (jak opłacić?)": "ORDER_HOW_PAYMENT",
            "Promocje i kody rabatowe": "ORDER_HOW_PROMO",
            "Faktury i dane do faktury": "ORDER_HOW_INVOICE"
        }
    },
    "ORDER_HOW_PAYMENT": {
        "message": "Akceptujemy przelewy, płatności kartą oraz BLIK. Po wyborze metody postępuj zgodnie z instrukcjami na stronie kasy.",
        "options": {}
    },
    "ORDER_HOW_PROMO": {
        "message": "Kody rabatowe dodajesz na etapie kasy w polu 'Kod promocyjny'. Każdy kod ma warunki użycia (min. wartość koszyka, produkty wyłączone).",
        "options": {}
    },
    "ORDER_HOW_INVOICE": {
        "message": "Dane do faktury możesz wpisać podczas składania zamówienia. Faktury wystawiamy na zgłoszony adres i NIP (jeśli podano).",
        "options": {}
    },
    "ORDER_CANCEL": {
        "message": "Anulowanie zamówienia jest możliwe do momentu przekazania do realizacji. Skontaktuj się z obsługą, podaj numer zamówienia.",
        "options": {}
    },
    "ORDER_STATUS": {
        "message": "Status zamówienia sprawdzisz w sekcji 'Moje zamówienia' po zalogowaniu. Podaj numer zamówienia, jeśli chcesz pomoc ręczną.",
        "options": {}
    },

    # ------ DOSTAWA ------
    "DELIVERY": {
        "message": "Chętnie pomogę! Co chcesz wiedzieć o dostawie?",
        "options": {
            "Gdzie jest moja paczka?": "DELIVERY_TRACKING",
            "Jaki jest czas dostawy?": "DELIVERY_TIME",
            "Czy mogę zmienić adres dostawy?": "DELIVERY_ADDRESS"
        }
    },
    "DELIVERY_TRACKING": {
        "message": "Czy masz numer śledzenia przesyłki?",
        "options": {
            "Tak, mam numer śledzenia": "DELIVERY_TRACKING_HAVE",
            "Nie, nie otrzymałem numeru śledzenia": "DELIVERY_TRACKING_NONE"
        }
    },
    "DELIVERY_TRACKING_HAVE": {
        "message": "Wpisz numer śledzenia na stronie przewoźnika (np. DPD, InPost) aby zobaczyć aktualny status. Jeśli status jest nieaktualny — czasem aktualizacje mają opóźnienie do 24h.",
        "options": {}
    },
    "DELIVERY_TRACKING_NONE": {
        "message": "Numer śledzenia wysyłamy w e-mailu po nadaniu paczki. Sprawdź spam; jeśli nie otrzymałeś, skontaktuj się z obsługą podając numer zamówienia.",
        "options": {}
    },
    "DELIVERY_TIME": {
        "message": "Czas dostawy zależy od metody. Wybierz co chcesz wiedzieć:",
        "options": {
            "Standard (2–4 dni robocze)": "DELIVERY_TIME_STD",
            "Ekspres (1 dzień)": "DELIVERY_TIME_EXP"
        }
    },
    "DELIVERY_TIME_STD": {"message": "Standardowa dostawa trwa zwykle 2–4 dni robocze.", "options": {}},
    "DELIVERY_TIME_EXP": {"message": "Dostawa ekspresowa (jeśli dostępna) często realizowana jest w ciągu 1 dnia roboczego.", "options": {}},
    "DELIVERY_ADDRESS": {
        "message": "Adres dostawy można zmienić przed spakowaniem przesyłki. Skontaktuj się z obsługą i podaj nowy adres oraz numer zamówienia.",
        "options": {}
    },

    # ------ PRODUKT ------
    "PRODUCT": {
        "message": "Co chciałbyś wiedzieć o produkcie?",
        "options": {
            "Potrzebuję instrukcji obsługi": "PRODUCT_MANUAL",
            "Produkt jest uszkodzony": "PRODUCT_DAMAGE",
            "Jakie warianty produktu są dostępne?": "PRODUCT_VARIANTS"
        }
    },
    "PRODUCT_MANUAL": {
        "message": "Instrukcja obsługi znajduje się na stronie produktu w sekcji 'Dokumenty'. Chcesz instrukcję w formacie PDF czy krótką pomoc?",
        "options": {
            "PDF z instrukcją": "PRODUCT_MANUAL_PDF",
            "Krótka pomoc / najczęstsze pytania": "PRODUCT_MANUAL_FAQ"
        }
    },
    "PRODUCT_MANUAL_PDF": {"message": "PDF jest do pobrania na stronie produktu. Jeśli nie możesz znaleźć, podaj model produktu, a sprawdzę ręcznie.", "options": {}},
    "PRODUCT_MANUAL_FAQ": {"message": "Sprawdź sekcję FAQ na karcie produktu — tam znajdziesz najczęściej zadawane pytania i krótkie instrukcje.", "options": {}},
    "PRODUCT_DAMAGE": {
        "message": "Jeśli produkt jest uszkodzony, złóż reklamację przez formularz zwrotów i dołącz zdjęcia uszkodzeń. Otrzymasz instrukcje dalszego postępowania.",
        "options": {}
    },
    "PRODUCT_VARIANTS": {
        "message": "Warianty (kolor/rozmiar) dostępne są na karcie produktu w menu 'Wybierz wariant'. Jeśli wariant niedostępny — zostaw powiadomienie o dostępności.",
        "options": {}
    }
}