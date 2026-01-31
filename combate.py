import random
from Personaje import Personaje, Monstruo
from LimpiarPantalla import limpiar_terminal

def combate(jugador, monstruo):
    print(f"\n{jugador.clase} vs {monstruo.clase}")
    ronda = 1 

    while jugador.hp > 0 and monstruo.hp > 0:
        print(f"\n- - Ronda {ronda} - -")
        ronda += 1

        print(f"{jugador.clase} HP: {jugador.hp} | {monstruo.clase} HP: {monstruo.hp}")

        accion = input("¿Que quieres hacer? (a = atacar / h = huir): ").lower()
        if accion in ("h", "huir"):
            print("Has huido del combate.")
            return "huido"

        if accion not in ("a", "atacar"):
            print("Opcion no valida.")
            continue

        #Defensa independiente
        defiende_monstruo = random.choice([True, False])
        defiende_jugador = random.choice([True, False])

        #ATAQUE DEL JUGADOR
        if defiende_monstruo:
            print("El monstruo bloqueo tu ataque.")
        else:
            daño = jugador.ataque + jugador.arma["dano"]
            monstruo.hp -= daño
            print(f"Le hiciste {daño} de daño.")

        if monstruo.hp <= 0:
            break

        #ATAQUE DEL MONSTRUO
        if defiende_jugador:
            print("Bloqueaste el ataque del monstruo.")
        else:
            daño_m = monstruo.ataque
            jugador.hp -= daño_m
            print(f"El monstruo te golpea y te quita {daño_m} de daño.")

    #RESULTADO FINAL
    if jugador.hp <= 0:
        print("\nHas sido derrotado...")
        return "jugador_muerto"

    print("\n¡Has vencido al monstruo!")
    monstruo.morir()

    #recompensa del monstruo
    recompensa = monstruo.recompensa
    if "oro" in recompensa:
        jugador.dinero += recompensa["oro"]
        print(f"Has ganado {recompensa['oro']} monedas de oro.")

    #objetos (armas, pociones, otros)
    if "tipo" in recompensa:
        jugador.inventario[recompensa["tipo"]].append(recompensa)
        print(f"Has obtenido: {recompensa['nombre']}")

    #Recompensas
    exp = 20
    oro = random.randint(10, 50)
    jugador.exp += exp
    jugador.dinero += oro

    print(f"Ganaste {exp} EXP y {oro} monedas de oro.")

    return "victoria"
