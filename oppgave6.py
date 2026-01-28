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
    p1 = Player("Jan Olav", 20)
    p2 = Player("Baltasor", 30)
    damage_p1 = p1.take_damage(0)
    damage_p2 = p2.take_damage(0)
    print("Spillet starter!")
    print("du har blitt angrepet! det beryktede trollet baltasor angriper deg, nå må du beskjyte deg selv.")
    print (f"----Runde {rund}----")
    print(f"du mistet {damage_p1} HP")
    print(f"baltasor har mistet {damage_p2} HP")
    print(f"navn: {p1.name}, HP: {p1.hp}, Lever: {p1.is_alive()}")
    print(f"navn: {p2.name}, HP: {p2.hp}, Lever: {p2.is_alive()}")
    while True:
        if p1.hp <= 0:
            print("Spilleren er død!")
            break
        elif p2.hp <= 0:
            print("Trollet baltasor er død! du vant!")
            break
        elif input("Trykk enter for å fortsette: ") == '':
            rund += 1
            print (f"----Runde {rund}----")
            damage_p1 = p1.take_damage(0)
            damage_p2 = p2.take_damage(0)
            print(f"du mistet {damage_p1} HP")
            print(f"baltasor har mistet {damage_p2} HP")
            print(f"navn: {p1.name}, HP: {p1.hp}, Lever: {p1.is_alive()}")
            print(f"navn: {p2.name}, HP: {p2.hp}, Lever: {p2.is_alive()}")
        else:
            print("Avslutter spillet.")
            break
else:
    print("Spillet avsluttes.")