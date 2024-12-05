import random as slump
import sys
import time

# Klass för spelare
class Spelare:
    def __init__(self, hp, styrka, tur, nivå, namn):
        self.hp = hp
        self.styrka = styrka
        self.tur = tur
        self.nivå = nivå
        self.erfarenhet = 0  # Ny variabel för erfarenhet
        self.förråd = []  # Förråd för föremål
        self.namn = namn

    def visa_statistik(self):
        print(f"\n{self.namn}s Statistik:")
        print(f"Hälsa: {self.hp}")
        print(f"Styrka: {self.styrka}")
        print(f"Tur: {self.tur}")
        print(f"Nivå: {self.nivå}")
        print(f"Erfarenhet: {self.erfarenhet}\n")

    def lägg_till_föremål(self, föremål):
        if len(self.förråd) < 15:  # Max 15 föremål
            self.förråd.append(föremål)
            print(f"Du lade till {föremål.namn} i ditt förråd.")
            self.styrka += föremål.styrka_bonus
            self.hp += föremål.hälsa_bonus
            self.tur += föremål.tur_bonus
        else:
            print("Ditt förråd är fullt! Du kan inte ta fler föremål.")

    def visa_förråd(self):
        if self.förråd:
            print("\nDitt förråd innehåller:")
            for i, föremål in enumerate(self.förråd, start=1):
                print(f"[{i}] {föremål}")
        else:
            print("\nDitt förråd är tomt.")

    def öka_erfarenhet(self, mängd):
        self.erfarenhet += mängd
        print(f"Du fick {mängd} erfarenhetspoäng!")
        if self.erfarenhet >= 50:  # Mängd erfarenhet för att gå upp i nivå
            self.erfarenhet = 0
            self.nivå += 1
            print(f"Grattis! Du har gått upp till nivå {self.nivå}!")
            if self.nivå == 3:
                print("Du har nått nivå 3! Spelet är slut!")
                sys.exit()  # Avsluta spelet när spelaren når nivå 3

# Klass för föremål
class Föremål:
    def __init__(self, styrka_bonus, hälsa_bonus, tur_bonus, namn):
        self.styrka_bonus = styrka_bonus
        self.hälsa_bonus = hälsa_bonus
        self.tur_bonus = tur_bonus
        self.namn = namn

    def __str__(self):
        return f"{self.namn} (Styrka: {self.styrka_bonus}, Hälsa: {self.hälsa_bonus}, Tur: {self.tur_bonus})"

# Funktioner för att skapa föremål
def skapa_svärd():
    return Föremål(slump.randint(1, 10), 0, 0, "Svärd")

def skapa_dryck():
    return Föremål(0, slump.randint(10, 30), 0, "Hälsodryck")

def skapa_turarmband():
    return Föremål(0, 0, slump.randint(1, 5), "Turarmband")

# Text med fördröjning
def skriv_med_fördröjning(text, fördröjning=0.02):
    for tecken in text:
        sys.stdout.write(tecken)
        sys.stdout.flush()
        time.sleep(fördröjning)
    print()

# Funktion för att skapa slumpmässiga rum
def slumpmässigt_rum():
    rum_typ = slump.choice(["drake", "fälla", "kista"])
    if rum_typ == "drake":
        möt_drake()
    elif rum_typ == "fälla":
        gå_in_i_fälla()
    elif rum_typ == "kista":
        öppna_kista()

# Rumsfunktioner
def möt_drake():
    skriv_med_fördröjning("En fruktansvärd drake hoppar fram!")
    drake_hp = slump.randint(10, 30)
    drake_styrka = slump.randint(3, 10)
    print(f"Drakens hälsa: {drake_hp}, Styrka: {drake_styrka}")

    while drake_hp > 0 and spelare.hp > 0:
        print("\nVad vill du göra?")
        print("[1] Attackera")
        print("[2] Försök fly")
        val = input("Ange ditt val: ")

        if val == "1":
            skada = slump.randint(1, spelare.styrka)
            drake_hp -= skada
            if drake_hp < 0:
                drake_hp = 0  
            print(f"Du slog draken för {skada} skada! Drakens hälsa: {drake_hp}")
            if drake_hp > 0:
                skada_tillbaka = slump.randint(1, drake_styrka)
                spelare.hp -= skada_tillbaka
                print(f"Draken attackerade dig för {skada_tillbaka} skada! Din hälsa: {spelare.hp}")
        elif val == "2":
            if slump.randint(1, 10) + spelare.tur > 8:
                print("Du lyckades fly!")
                return
            else:
                print("Du misslyckades med att fly!")
                skada_tillbaka = slump.randint(1, drake_styrka)
                spelare.hp -= skada_tillbaka
                print(f"Draken attackerade dig för {skada_tillbaka} skada! Din hälsa: {spelare.hp}")

    if drake_hp == 0:
        print("Du besegrade draken!")
        spelare.öka_erfarenhet(10)  # Spelaren får erfarenhet för att besegra draken
    if spelare.hp <= 0:
        print("Du blev besegrad av draken... Spelet är över!")
        sys.exit()

def gå_in_i_fälla():
    print("Du aktiverade en fälla!")
    skada = slump.randint(5, 15)
    spelare.hp -= skada
    print(f"Du tog {skada} skada. Din hälsa är nu {spelare.hp}.")
    if spelare.hp <= 0:
        print("Du dog av skadorna... Spelet är över!")
        sys.exit()

def öppna_kista():
    print("Du hittar en kista!")
    föremål_typ = slump.choice([skapa_svärd, skapa_dryck, skapa_turarmband])
    föremål = föremål_typ()
    print(f"Du hittade {föremål}!")
    spelare.lägg_till_föremål(föremål)
    spelare.öka_erfarenhet(5)  # Spelaren får erfarenhet för att öppna kistan

# Startmeny
def start_meny():
    skriv_med_fördröjning("\nVälkommen till Dragonslayer!\n")
    namn = input("Vad heter din karaktär? ")
    global spelare
    spelare = Spelare(100, 10, 5, 1, namn)
    while True:
        print("\nVad vill du göra?")
        print("[1] Gå in i en läskig grotta")
        print("[2] Visa din statistik")
        print("[3] Visa ditt förråd")
        print("[4] Avsluta spelet")
        val = input("Vad väljer du?: ")

        if val == "1":
            slumpmässigt_rum()
        elif val == "2":
            spelare.visa_statistik()
        elif val == "3":
            spelare.visa_förråd()
        elif val == "4":
            print("Tack för att du spelade! Hejdå!")
            break
        else:
            print("Ogiltigt val. Försök igen.")

# Starta spelet
start_meny()
