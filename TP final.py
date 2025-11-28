import random, pickle, os, sys

archivo = "tickets"

diccionario_total = {}

if os.path.isfile(archivo):

    with open(archivo, "rb") as f:
        diccionario_total = pickle.load(f)


while True:
    opcion = (input("                                 TE DAMOS LA BIENVENIDA AL SISTEMA DE TICKETS \n 1 - Genere un nuevo ticket \n 2 - Consulte un ticket \n 3 - Salir \n \n Seleccione una opción: "))

    if opcion == "1":

        while True:
            print("Complete con los datos correspondientes \n")
            datos = {}
            datos["nombre"] = str(input(("Ingrese su nombre y apellido: ")))

            datos["sector"] = str(input("Ingrese el sector: "))
            
            datos["asunto"] = str(input("Ingrese el asunto: "))

            datos["mensaje"] = str(input("Ingrese su mensaje (opcional): "))

            numero_ticket = random.randrange(1000, 10000)

            diccionario_total[numero_ticket] = datos

            with open(archivo, "wb") as f:
                pickle.dump(diccionario_total, f)

            print(f"\nTu número de ticket es: {numero_ticket}. Por favor, no lo olvides.")
            print("\nResumen de tu ticket: \n")
            print(f"Nombre: {datos["nombre"]}")
            print(f"Sector: {datos["sector"]}")
            print(f"Asunto: {datos["asunto"]}")
            print(f"Mensaje: {datos["mensaje"]}")
            print("\n")

            continuar = input(f"¿Desea generar otro ticket? y/n \n").lower().strip()

            if continuar == "n":
                break

    elif opcion == "2":

        while True:

            consulta = int(input("Por favor, ingrese el número de ticket: "))
            
            if consulta in diccionario_total:
                print(f"Aquí tiene: \n")
                ticket = (diccionario_total[consulta])

                print(f"Nombre: {ticket["nombre"]}")
                print(f"Sector: {ticket["sector"]}")
                print(f"Asunto: {ticket["asunto"]}")
                print(f"Mensaje: {ticket["mensaje"]}")
                print("\n")

                otra_consulta = input(f"¿Desea consultar otro ticket? y/n \n").lower().strip()

                if otra_consulta == "n":
                    break

            else:
                print("Ticket no encontrado.")

    elif opcion == "3":

        salida = input("¿Desea cerrar el programa? y/n").lower().strip()

        if salida == "y":
            print ("Muchas gracias por utilizar este programa.")
            break
    
    else:
        print("\n Por favor, selecciona una opción válida.\n")