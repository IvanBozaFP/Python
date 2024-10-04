import random

# Joc Adivina Número
def adivina_numero():
    numero_secret = random.randint(1, 10)
    intents = 3
    print("Benvingut a Adivina Número! Tens 3 intents per adivinar el número entre 1 i 10.")
    while intents > 0:
        try:
            endevina = int(input("Introdueix el teu número: "))
            if endevina < 1 or endevina > 10:
                print("Si us plau, introdueix un número entre 1 i 10.")
                continue
        except ValueError:
            print("Introdueix un número vàlid!")
            continue

        if endevina == numero_secret:
            print(f"Correcte! El número era {numero_secret}. Has guanyat!")
            return
        elif endevina < numero_secret:
            print("El número és major.")
        else:
            print("El número és menor.")
        intents -= 1

    print(f"Has perdut! El número era {numero_secret}.")

# Joc Pedra, Paper, Tisores
def pedra_paper_tisores():
    opcions = ["pedra", "paper", "tisores"]
    puntuacio_usuari = 0
    puntuacio_maquina = 0
    print("Benvingut a Pedra, Paper, Tisores! El primer a arribar a 3 punts guanya.")

    def jugar_una_partida():
        no_valid = True
        while no_valid:
            usuari = input("Pedra, paper o tisores?: ").lower()
            if usuari not in opcions:
                print("Opció no vàlida! Introdueix 'pedra', 'paper' o 'tisores'.")
            else:
                no_valid = False
        maquina = random.choice(opcions)
        print(f"La màquina tria {maquina}")
        return usuari, maquina

    while puntuacio_usuari < 3 and puntuacio_maquina < 3:
        usuari, maquina = jugar_una_partida()

        if usuari == maquina:
            print("Empat!")
        elif (usuari == "pedra" and maquina == "tisores") or (usuari == "paper" and maquina == "pedra") or (usuari == "tisores" and maquina == "paper"):
            puntuacio_usuari += 1
            print("Has guanyat aquesta ronda!")
        else:
            puntuacio_maquina += 1
            print("La màquina ha guanyat aquesta ronda!")

        print(f"Marcador: Tu {puntuacio_usuari} - Màquina {puntuacio_maquina}")

    if puntuacio_usuari == 3:
        print("Enhorabona! Has guanyat!")
    else:
        print("La màquina ha guanyat.")

# Joc El Penjat
def el_penjat():
    with open('paraules.txt', 'r') as file:
        paraules = [line.strip() for line in file.readlines()]

    paraula = random.choice(paraules)
    intents = len(paraula) * 2
    paraula_mostrada = ['_'] * len(paraula)
    lletres_encertades = set()

    print(f"Benvingut al Penjat! Has d'endevinar una paraula de {len(paraula)} lletres. Tens {intents} intents.")

    while intents > 0 and '_' in paraula_mostrada:
        print(f"Paraula: {' '.join(paraula_mostrada)}")
        lletra = input("Introdueix una lletra: ").lower()

        if not lletra.isalpha() or len(lletra) != 1:
            print("Introdueix una lletra vàlida!")
            continue

        if lletra in lletres_encertades:
            print("Ja has introduït aquesta lletra!")
            continue

        lletres_encertades.add(lletra)

        if lletra in paraula:
            for i, c in enumerate(paraula):
                if c == lletra:
                    paraula_mostrada[i] = lletra
            print(f"Bé! La lletra '{lletra}' és a la paraula.")
        else:
            intents -= 1
            print(f"La lletra '{lletra}' no és a la paraula. Et queden {intents} intents.")

    if '_' not in paraula_mostrada:
        print(f"Enhorabona! Has endevinat la paraula: {paraula}")
    else:
        print(f"Has perdut! La paraula era: {paraula}")

# Menú principal
def menu():
    while True:
        print("\nMenú de Jocs")
        print("1. Adivina Número")
        print("2. Pedra, Paper, Tisores")
        print("3. El Penjat")
        print("4. Sortir")

        try:
            eleccio = int(input("Selecciona un joc: "))
        except ValueError:
            print("Introdueix una opció vàlida.")
            continue

        if eleccio == 1:
            adivina_numero()
        elif eleccio == 2:
            pedra_paper_tisores()
        elif eleccio == 3:
            el_penjat()
        elif eleccio == 4:
            print("Gràcies per jugar!")
            break
        else:
            print("Introdueix una opció vàlida.")

if __name__ == "__main__":
    menu()