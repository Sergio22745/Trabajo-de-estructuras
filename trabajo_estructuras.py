from collections import deque

lista = []
pila = []
cola = deque()

while True:
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Trabajar con LISTA")
    print("2. Trabajar con PILA")
    print("3. Trabajar con COLA")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    # ---------------- LISTA ----------------
    if opcion == "1":
        while True:
            print("\n--- LISTA ---")
            print("1. Agregar elemento")
            print("2. Ver lista")
            print("3. Volver al menú")

            op = input("Seleccione: ")

            if op == "1":
                valor = input("Ingrese valor: ")
                lista.append(valor)

            elif op == "2":
                print("Lista:", lista)

            elif op == "3":
                break

            else:
                print("Opción inválida")

    # ---------------- PILA ----------------
    elif opcion == "2":
        while True:
            print("\n--- PILA (LIFO) ---")
            print("1. Insertar")
            print("2. Eliminar")
            print("3. Ver pila")
            print("4. Volver")

            op = input("Seleccione: ")

            if op == "1":
                valor = input("Ingrese valor: ")
                pila.append(valor)

            elif op == "2":
                if pila:
                    print("Se eliminó:", pila.pop())
                else:
                    print("La pila está vacía")

            elif op == "3":
                print("Pila:", pila)

            elif op == "4":
                break

            else:
                print("Opción inválida")

    # ---------------- COLA ----------------
    elif opcion == "3":
        while True:
            print("\n--- COLA (FIFO) ---")
            print("1. Insertar")
            print("2. Eliminar")
            print("3. Ver cola")
            print("4. Volver")

            op = input("Seleccione: ")

            if op == "1":
                valor = input("Ingrese valor: ")
                cola.append(valor)

            elif op == "2":
                if cola:
                    print("Se eliminó:", cola.popleft())
                else:
                    print("La cola está vacía")

            elif op == "3":
                print("Cola:", list(cola))

            elif op == "4":
                break

            else:
                print("Opción inválida")

    # ---------------- SALIR ----------------
    elif opcion == "4":
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida")
