import json
class Användarhantering: 
    """ 
    Hanterar alla olika funktioner vid inlogging eller registering av användare.
    Lagrar alla användare och historik i en .json fil.
    """
    def __init__(self,filväg:str) -> None: 
        self.filväg = filväg 
        self.felaktiga_försök = 3 # startvärde för antal försök användaren får vid inloggning.
        self.användare = self.läs_in_användare()
        self.val = 0


    def läs_in_användare(self) -> dict:
        """"
        Läser in användarna från filen och retunerar dem som en dict så att tidigare data
        är sparad och kan användas igen.
        """
        try:
            with open(self.filväg, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return [] # en tom lista om filen inte finns

    def spara_användare(self):
        """
        Sparar nuvarande användarlista till .json filen.
        """
        with open(self.filväg, "w") as f:
            json.dump(self.användare, f)

   
    def ta_bort_anv(self, användarnamn: str):
        """
        En funktion för att ta bort befintliga användare ur .json filen
        """
        self.hittade = False
        for anv in self.användare:
            if anv["nam"] == användarnamn:
                self.användare.remove(anv)
                print("f{self.användarnamn} togs bort ur systemet")
                self.spara_användare()
                break
        if not self.hittade:
            print("Hittade ingen med det namnet")

    
    def hantera_val(self) -> bool:
        """
        Hantera de olika valen användaren gör under skriptets gång genom att anropa de olika 
        metoderna vid korrekt inmatning."""
        self.val = input() 
        try: # try / except sats för krashhantering vid felaktig inmatning.
            if self.val == "1":
                self.resultat = self.logga_in()
                return self.resultat
            elif self.val == "2":
                self.registrera()
                return True
            else:
                print("Ogiltigt val försök igen")
                return False

        except ValueError:
            print("Felaktig inmatning, försök igen")
            return False

    def lista_användare(self): 
        pass
    def byt_användare(self): 
        pass