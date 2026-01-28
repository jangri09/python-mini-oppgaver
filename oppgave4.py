handle_list = []
i = int(0)
while True:
    item = input("Legg til et element i handlelisten (eller skriv 'ferdig' for å avslutte): ")
    try:
        if item == '':
            raise ValueError("Du må skrive inn noe!")
    except ValueError as e:
        print(e)
        continue
    if item.lower() == 'ferdig':
        while i < len(handle_list):
            print(f"{i+1}. {handle_list[i]}")
            i += 1
        print("antall elementer i handlelisten:", len(handle_list))
        break
    handle_list.append(item)