----------------------------------

Inloggningssystem – Individuell inlämningsuppgift

Detta skript är ett användarvänligt inloggningssystem, med fokus på säkerhet, tydlig menystruktur och stabil felhantering. Systemet hanterar registrering, inloggning, användarlistning och radering med verifiering, och loggar viktiga händelser i en lokal historikfil.

----------------------------------------

Instruktioner
- Klona repot
- skriv: git clone https://github.com/ikarosbernardini/Individuell-uppgift.git i din terminal. 
- skriv sedan: cd Individuell-uppgift
- Kör skriptet:
python main.py eller python3 main.py beroende på ditt operativsystem


----------------------------------------

Funktioner
- Registrera nya användare med lösenord (hashas säkert)
- Logga in med verifiering mot sparad data
- Lista alla registrerade användare
- Radera användare (med lösenordsverifiering och bekräftelse)
- Tydlig menystruktur med validering och återkoppling
- Loggning av viktiga händelser i historik.log
- Felhantering för tomma fält, ogiltiga val och misslyckade operationer
- "Tryck Enter för att fortsätta"-flöde för bättre användarupplevelse

----------------------------------------

Moduler och språk
- Språk: Python
- Moduler: hashlib,datetime,json
- Loggfil: historik.log


----------------------------------------

Källor
- COPILOT 
- Stackoverflow
- Python book - Automate the boring stuff :  
https://automatetheboringstuff.com/#toc
- Python imports : 
https://docs.python.org/3/library/hashlib.html

https://docs.python.org/3/library/datetime.html

https://docs.python.org/3/library/json.html

Unicode tecken table :
https://symbl.cc/en/unicode-table/#spacing-modifier-letters

ANSI escape codes table : 
https://jakob-bagterp.github.io/colorist-for-python/ansi-escape-codes/introduction/


----------------------------------------

Skapat av Ikaros Bernardini

