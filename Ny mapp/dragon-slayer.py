# def meny():
#     print("""
#     Välkommen!
          
#     Välj ett alternativ:
#     [1] Spela
#     [2] Se ditt inventory
#     [3] Se dina stats
#     [4] Avsluta
#     """)

# def spel_meny():
#     print("""
#     Du har fått ett vapen - 
#     Spelmeny:
#     [1] Attackera en fiende
#     [2] Utforska området
#     [3] Gå tillbaka till huvudmenyn
#     """)

# def get_user_input():
#     try:
#         tal = int(input("Gör ett val: "))
#     except ValueError:
#         print("Det var inte ett heltal, välj ett annat alternativ.")
#         return 0
#     except Exception as ex:
#         print(f"Något gick fel: {ex}")
#         return 0
#     return tal

# dmg = 0
# hp = 100

# while True:
#     meny()
#     val = get_user_input()
    
#     if val == 0:
#         continue
#     if val == 1:
#         while True:
#             spel_meny()
#             spel_val = get_user_input()
#             if spel_val == 0:
#                 continue
#             if spel_val == 1:
#                 print("dungeon 1")
#             elif spel_val == 2:
#                 print("dungeon 2")
#             elif spel_val == 3:
#                 print("Dungeon 3")
#             else:
#                 print("Ogiltigt val, försök igen.")

#     elif val == 2:
#         print("Ditt inventory är tomt än så länge.")
#     elif val == 3:
#         print(f""" 
              
              
# Dina stats:
#     - Damage: {dmg}
#     - HP: {hp}
# """)
#     elif val == 4:
#         print("Spelet avslutas.")
#         break
#     else:
#         print("Ogiltigt val, försök igen.")



class Spelare:
    def __init__(self, namn):
        self.namn = namn
        self.damage = 0
        self.hp = 100
        self.inventory = []

    def visa_stats(self):
        print(f"""
Dina stats:
    - Damage: {self.damage}
    - HP: {self.hp}
        """)

    def visa_inventory(self):
        if self.inventory:
            print("Ditt inventory innehåller:")
            for item in self.inventory:
                print(f"- {item}")
        else:
            print("Ditt inventory är tomt än så länge.")

    def lägg_till_föremål(self, föremål):
        self.inventory.append(föremål)
        print(f"{föremål} har lagts till i ditt inventory.")


class Spel:
    def __init__(self):
        self.spelare = None

    def visa_meny(self):
        print("""
    Välj ett alternativ:
    [1] Spela
    [2] Se ditt inventory
    [3] Se dina stats
    [4] Avsluta
        """)

    def spel_meny(self):
        print("""
    Spelmeny:
    [1] Attackera en fiende
    [2] Utforska området
    [3] Gå tillbaka till huvudmenyn
        """)


    import random

    class vapen:
        def __init__(self, vapen_dmg, vapen_namn):
            self.vapen_dmg = vapen_dmg
            self.vapen_namn= vapen_namn
            self.inventory 


  def starta_spel(self, self_spelare):
        namn = input("Vad heter din karaktär? ")
        self_spelare = Spelare(namn)
        print(f"Välkommen till spelet, {self_spelare.namn}!") 

        while True:
            self.visa_meny()
            val = self.get_user_input()
            
            if val == 1:
                self.spel_loop()
            elif val == 2:
                self.spelare.visa_inventory()
            elif val == 3:
                self.spelare.visa_stats()
            elif val == 4:
                print("Spelet avslutas.")
                break
            else:
                print("Ogiltigt val, försök igen.")

    def spel_loop(self):
        while True:
            self.spel_meny()
            spel_val = self.get_user_input()
            if spel_val == 1:
                print("Du attackerar en fiende!")
                self.spelare.damage += 5  
            elif spel_val == 2:
                print("Du utforskar området och hittar ett svärd!")
                self.spelare.lägg_till_föremål("Svärd")
            elif spel_val == 3:
                print("Du återvänder till huvudmenyn.")
                break
            else:
                print("Ogiltigt val, försök igen.")

    def get_user_input(self):
        try:
            tal = int(input("Gör ett val: "))
            return tal
        except ValueError:
            print("Det var inte ett heltal, välj ett annat alternativ.")
        return 0


spel = Spel()
spel.starta_spel()
