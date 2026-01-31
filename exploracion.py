import random
from combate import combate
from Personaje import Monstruo
from LimpiarPantalla import limpiar_terminal

#generar monstruo segun el piso
def generar_monstruo_por_piso(piso, monstruos_base):
    nivel = min(piso, 30)  #limite maximo
    return monstruos_base[nivel]


#generar monstruos desde datos
def crear_monstruo(monstruo_data):
    nombre, hp, mana, escudo, ataque, nivel, recompensa = monstruo_data
    return Monstruo(nombre, hp, mana, escudo, ataque, nivel, recompensa)

#manejar combate y muerte
def enfrentar_monstruo(jugador, monstruo):
    combate(jugador, monstruo)

    if jugador.hp <= 0:
        print("\nHas muerto... pierdes todo tu inventario.")
        print("¡La vida solo es una! ;)")
        jugador.inventario = {
            "armas": [],
            "pociones": [],
            "otros": []
        }
        jugador.desequipar_arma()

            
           
        input("ENTER para continuar...")
        return True  #murio

    return False  #sigue vivo

#exploracion
def explorar(jugador, monstruos_base, piso_actual):

    print("\n-Exploracion-")
    print("¿A dónde quieres ir?")
    print("1. Bosque")
    print("2. Mazmorra")
    print("3. Montaña")
    print("4. Aldea (descansar)")
    print("0. Volver al menu")

    opcion = input("Elige una zona: ")
    evento = random.randint(1, 100)

    #bosque
    if opcion == "1":
        limpiar_terminal()
        input("\nCaminando hacia el Bosque...")

        if evento > 50:
            print("\nTe encuentras con un monstruo!")
            monstruo_data = random.choice(list(monstruos_base.values()))
            enemigo = crear_monstruo(monstruo_data)

            if enfrentar_monstruo(jugador, enemigo):
                return piso_actual  #vuelve al menu

        else:
            print("No has encontrado nada.")

    #mazmorra(utiliza pisos)
    elif opcion == "2":
        limpiar_terminal()
        input(f"\nBajando al piso {piso_actual} de la Mazmorra...")

        if evento < 60:
            print("\nUn monstruo aparece!")
            monstruo_data = generar_monstruo_por_piso(piso_actual, monstruos_base)
            enemigo = crear_monstruo(monstruo_data)

            if enfrentar_monstruo(jugador, enemigo):
                piso_actual = 1
                return piso_actual

            #si gana, baja un piso
            print(f"\nHas derrotado al monstruo. Bajas al piso {piso_actual + 1}.")
            piso_actual += 1
            input("ENTER para continuar...")
            limpiar_terminal()

        else:
            print("No has encontrado nada.")

    #montaña
    elif opcion == "3":
        limpiar_terminal()
        input("\nCaminando hacia la Montaña...")

        if evento < 25 or evento > 75:
            print("\nTe encuentras con un monstruo!")
            monstruo_data = random.choice(list(monstruos_base.values()))
            enemigo = crear_monstruo(monstruo_data)

            if enfrentar_monstruo(jugador, enemigo):
                return piso_actual

        else:
            print("No has encontrado nada.")

    #aldea
    elif opcion == "4":
        limpiar_terminal()
        input("\nCaminando hacia la Aldea...")
        jugador.hp += 50
        print("Descansas y recuperas +20 HP.")
        return piso_actual

    return piso_actual
