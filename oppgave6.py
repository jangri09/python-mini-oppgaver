import random
rund = int(1)
class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def take_damage(self, damage):
        damage = random.randint(1, 15)
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        return damage

    def is_alive(self):
        return self.hp > 0
if input("Start spillet?: ").strip().lower() == 'ja':
    p1 = Player(input("Skriv inn navnet spiller 1: "), 30)
    p2 = Player(input("Skriv inn navnet spiller 2: "), 30)
    damage_p1 = p1.take_damage(0)
    damage_p2 = p2.take_damage(0)
    print("Spillet starter!")
    print()
    print (f"----Runde {rund}----")
    print(f"{p1.name} mistet {damage_p1} HP")
    print(f"{p2.name} mistet {damage_p2} HP")
    print(f"navn: {p1.name}, HP: {p1.hp}, Lever: {p1.is_alive()}")
    print(f"navn: {p2.name}, HP: {p2.hp}, Lever: {p2.is_alive()}")
    while True:
        if p1.hp <= 0 and p2.hp <= 0:
            print("Begge spillere er døde! Det er uavgjort!")
            break
        elif p2.hp <= 0:
            print(f"{p2.name} er død! {p1.name} vant!")
            break
        elif p1.hp <= 0:
            print(f"{p1.name} er død! {p2.name} vant!")
            break
        elif input("Trykk enter for å fortsette: ") == '':
            rund += 1
            print()
            print (f"----Runde {rund}----")
            damage_p1 = p1.take_damage(0)
            damage_p2 = p2.take_damage(0)
            print(f"{p1.name} mistet {damage_p1} HP")
            print(f"{p2.name} mistet {damage_p2} HP")
            print(f"navn: {p1.name}, HP: {p1.hp}, Lever: {p1.is_alive()}")
            print(f"navn: {p2.name}, HP: {p2.hp}, Lever: {p2.is_alive()}")
        else:
            print("Avslutter spillet.")
            break
else:
    print("Spillet avsluttes.")