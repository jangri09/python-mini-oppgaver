
try:
    poengsum = int(input("Skriv inn poengsummen din (0-100): "))
    if poengsum < 0 or poengsum > 100:
        raise ValueError("Feil! Poengsummen må være mellom 0 og 100.")
    if poengsum >= 90:
        karakter = '6'
    elif poengsum >= 80:
        karakter = '5'
    elif poengsum >= 65:
        karakter = '4'
    elif poengsum >= 50:
        karakter = '3'
    elif poengsum >= 35:
        karakter = '2'
    else:
        karakter = '1'
    print(f"Din karakter er: {karakter}")

except ValueError:
    print("Feil! Du må skrive inn et gyldig tall mellom 0 og 100.")