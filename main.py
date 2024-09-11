import random
# Generar número secreto
numerosecreto = random.randint(1, 100)

# Inicializar números para el usuario y la computadora
numero_usuario = None
numero_compu = random.randint(1, 100)

print(f"El número inicial de la computadora es {numero_compu}")

#bucle mientras sea true
while True:
    # Intento del usuario
    numero_usuario = int(input("Digite un número entre 1 y 100: "))
    
    # Validar el número del usuario
    while numero_usuario < 1 or numero_usuario > 100:
        print("Error, el número debe estar entre 1 y 100.")
        numero_usuario = int(input("Digite un número válido: "))

    # Verificar si el usuario adivinó el número secreto
    if numero_usuario == numerosecreto:
        print("¡Felicidades! El usuario ha adivinado el número secreto.")
        break

    # Verificar si el intento del usuario es mayor o menor que el número secreto
    if numero_usuario > numerosecreto:
        print("Tu número es muy alto.")
    else:
        print("Tu número es muy bajo.")

  #turno de la compu
    ajuste_compu = random.randint(1, 10) #numero aleatorio para hacer el ajuste
    if numero_compu > numerosecreto:
        numero_compu -= ajuste_compu
        if numero_compu < 1:
            numero_compu = 1
    else:
        numero_compu += ajuste_compu
        if numero_compu > 100:
            numero_compu = 100

    #nuevo intento de la computadora
    print(f"La computadora ajusta su número a: {numero_compu}")

    # Verificar si la computadora adivinó el número secreto
    if numero_compu == numerosecreto:
        print("La computadora ha adivinado el número secreto. ¡La computadora gana!")
        break