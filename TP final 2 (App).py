import secrets, string, sys

posibles = {
  'letras': string.ascii_letters,
  'numeros': string.digits,
  'caracteres': string.punctuation
}

password = ""


while True:
    opcion = (input("                                 GENERADOR DE CONTRASEÑAS \n 1 - Generar contraseña solo de letras \n 2 - Generar contraseña solo de números \n 3 - Generar contraseña con letras y números \n 4 - Generar contraseña con letras, números y caracteres \n 0 - Salir \n \n Seleccione una opción: "))

    if opcion == "1":

        print("\nAquí tiene su contraseña: \n")
        password_letras = posibles['letras']
        password = "".join(secrets.choice(password_letras) for i in range(12))
        print(f"\n{password}")

    elif opcion == "2":

        print("\nAquí tiene su contraseña: \n")
        password_numeros = posibles['numeros']
        password = "".join(secrets.choice(password_numeros) for i in range(12))
        print(f"\n{password}")

    elif opcion == "3":

        print("\nAquí tiene su contraseña: \n")
        password_combi3 = posibles['letras'] + posibles["numeros"]
        password = "".join(secrets.choice(password_combi3) for i in range(12))
        print(f"\n{password}")

    elif opcion == "4":

        print("\nAquí tiene su contraseña: \n")
        password_combi4 = posibles['letras'] + posibles["numeros"] + posibles["caracteres"]
        password = "".join(secrets.choice(password_combi4) for i in range(12))
        print(f"\n{password}")

    elif opcion == "0":

        salida = input("\n¿Desea cerrar el programa? y/n\n").lower().strip()

        if salida == "y":
            print ("Muchas gracias por utilizar este programa.")
            break

    else:
        print("\n Por favor, selecciona una opción válida.\n")