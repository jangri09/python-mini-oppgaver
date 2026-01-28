import random
gjet = int(0)
hjemlig_tall = int(random.randint(1, 100))
gjetning = int(input("Gjett et tall mellom 1 og 100: "))
while gjetning != hjemlig_tall or gjet <= 7:
    if gjetning < hjemlig_tall:
        print("For lavt! Prøv igjen.")
    else:
        print("For høyt! Prøv igjen.")
    gjet += 1
    if gjet >= 7:
        print(f"Beklager, du har brukt opp alle forsøkene. Det riktige tallet var {hjemlig_tall}.")
        break
    print(f"Du har {7 - gjet} forsøk igjen.")
    gjetning = int(input("Gjett et tall mellom 1 og 100: "))
print(f"Gratulerer! Du gjettet riktig tall: {hjemlig_tall}")