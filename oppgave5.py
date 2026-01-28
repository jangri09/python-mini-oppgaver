forbudt_ord = ["dritt", "fy", "67", "idiot"]
while True:
    setning = str(input("Skriv inn en setning: ")).lower()
    if any(ord in forbudt_ord for ord in setning.split()):
        print("melding stoppet!")
    else:
        print("melding sendt.")
        break
