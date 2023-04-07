user_choice = 0
while user_choice != 5:
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Wyjdź")

    user_choice = int(input("Wpisz liczbę: "))

    if user_choice in range(1, 5):
        liczba_pierwsza = liczba_druga = wynik = 0
        liczba_pierwsza = int(input("Podaj pierwszą liczbę: "))
        liczba_druga = int(input("Podaj drugą liczbę: "))

        if user_choice == 1:
            wynik = liczba_pierwsza + liczba_druga
        elif user_choice == 2:
            wynik = liczba_pierwsza - liczba_druga
        elif user_choice == 3:
            wynik = liczba_pierwsza * liczba_druga
        elif user_choice == 4:
            if liczba_druga != 0:  # nie dzielimy przez 0
                wynik = round(liczba_pierwsza / liczba_druga, 2)
            else:
                wynik = "nie dzielimy przez zero '0'"

        print(f"Wynik: {wynik}\n")
