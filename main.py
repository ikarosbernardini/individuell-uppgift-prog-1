from anvhant import Användarhantering as a
from anv import Användare as anv
 # importerar klassen Användarhantering som innehåller alla mina menyvals funktioner som bokstaven "a".

def meny_innan_inloggning():
    while True: 
        print("""
    -----------------------------------------
    Välj alternativ: 
        1. Logga in med befintlig användare 
        2. Registrera ny användare.
        3. Avsluta programmet. 
    -----------------------------------------
    """)
    
meny_innan_inloggning()


def meny_efter_inloggning():
    while True:
        print(f"\nInloggad som ")
        print("""
    -----------------------------------------
    Välj alternativ: 
        1. Byt lösenord 
        2. Byt namn 
        3. Byt användare 
        4. Ta bort användare 
        5. Visa användarlista 
        6. Avsluta programmet.
    -----------------------------------------
    """)
        a.val = input("\n:")
        
        if a.val == "1": # genererar en ny hash nyckel
            a.byt_lösenord()

        elif a.val == "2":
            nytt_namn = input("Ange nytt användarnamn:")
            a.ändra_namn(nytt_namn)

        elif a.val == "3":
            a.bytt_användare()
        elif a.val == "4":
            a.ta_bort_anv()
        elif a.val == "5":
            meny_innan_inloggning()
            a.hantera_val()
        elif a.val == "6":
            print("\nProgrammet avslutas.")
            exit()

meny_efter_inloggning()