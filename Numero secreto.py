"""
Juego: Adivina el Número Secreto
Desarrollado para simular un mini-proyecto ágil con integración continua.
"""

import random


def generar_numero_secreto():
    """Genera un número aleatorio entre 1 y 100."""
    return random.randint(1, 100)


def evaluar_intento(secreto, intento):
    """Compara el intento del usuario con el número secreto."""
    if intento < secreto:
        return "Demasiado bajo. Intenta con un número mayor."
    elif intento > secreto:
        return "Demasiado alto. Intenta con un número menor."
    else:
        return "¡Correcto! Has adivinado el número."


def jugar():
    print("=== ADIVINA EL NÚMERO SECRETO ===")
    secreto = generar_numero_secreto()
    intentos = 0

    while True:
        try:
            intento = int(input("Ingresa un número del 1 al 100: "))
            intentos += 1
            resultado = evaluar_intento(secreto, intento)
            print(resultado)
            if intento == secreto:
                print(f"Total de intentos: {intentos}")
                break
        except ValueError:
            print("Por favor, ingresa un número entero válido.")


if __name__ == "__main__":
    jugar()
