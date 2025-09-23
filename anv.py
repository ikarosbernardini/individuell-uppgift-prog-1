import hashlib
import json
from anvhant import Användarhantering as a

class Användare:
    """
    Skapat en klass som representera varje enskild användare och dessa innehåll
    """


    def __init__(self, namn: str, lösenord: str): 
        self.namn = namn
        self.lösenord_hash = self.hasha_lösenord(lösenord) 
        self.användare = []
        self.felaktiga_försök = 3 
    
    def hasha_lösenord(self, lösenord: str): # konverterar inmatningen av lösenord till ett hashat lösenord
        """
        Tar de inmatade lösenordet och retunerar dess 'SHA256-hash som en hex-sträng'
        """
        return hashlib.sha256(lösenord.encode("utf-8")).hexdigest()

    def till_dict(self) -> dict: 
        """
        Gör om användaren som en dict för att kunna spara den i .json filen.
        """
        return {"namn": self.namn, "lösenord_hash": self.lösenord_hash}
    def från_dict(self) -> dict:
        """
        Skapar en Användare från en dict.
        """
        return Användare(anvdata["namn"], anvdata["lösenord"])
    
    def registrera(self) -> bool: # start metod för att låta användaren registera en ny obentlig användare.
        """
        Registerar ny användare och sparar användarens uppgifter i .json filen för att låta användaren 
        sedan kunna enkelt logga in med sparade uppgifter.
        """
        namn = input("Nytt användarnamn: ")
        lösenord = input("Nytt lösenord: ")
        
        if any(anv["namn"] == namn for anv in self.användare):
            print("Användarnamnet finns redan.")
            return False
        self.användare.append({
            "namn": namn,
            "lösenord_hash": self.hasha_lösenord(lösenord)
        })
        a.spara_användare()
        print("Användare registerad.")
        return True 
    

    def logga_in(self) -> bool:# start metoden för att låta användaren logga in med en befintlig användare.
        """
        Inloggingsmetod för användare som redan har ett konto sparat i .json filen.
        """
        while self.felaktiga_försök > 0:
            namn = input("Användarnamn:")
            lösenord = input("Lösenord:")
            lösenord_hash = self.hasha_lösenord(lösenord)
            for anv in self.användare:
                if anv["namn"] == namn and anv["lösenord_hash"] == lösenord_hash:
                    print(f"Välkommen {namn}!")
                    return True
            else:
                self.felaktiga_försök -= 1
                if self.felaktiga_försök == 0:
                    print("För många felaktiga försök. Programmet avslutas.")
                    return False
                else: 
                    print(f"Felaktigt användarnamn eller lösenord. Du har {self.felaktiga_försök} försök kvar, Försök igen")