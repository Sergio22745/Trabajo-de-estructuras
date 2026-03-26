from collections import deque

# ---------------------------
# MEMORIA ESTÁTICA
# ---------------------------
print("=== MEMORIA ESTÁTICA ===")

try:
    tamano = int(input("Ingrese el tamaño fijo del arreglo: "))
except:
    print("Error: debes ingresar un número.")
    exit()

arreglo_estatico = [0] * tamano

for i in range(tamano):
    while True:
        try:
            valor = int(input(f"Ingrese el valor para la posición {i}: "))
            arreglo_estatico[i] = valor
            break
        except:
            print("Ingrese un número válido.")

print("Arreglo estático final:", arreglo_estatico)


# ---------------------------
# MEMORIA DINÁMICA
# ---------------------------
print("\n=== MEMORIA DINÁMICA ===")

lista_dinamica = []

while True:
    try:
        cantidad = int(input("¿Cuántos valores desea agregar?: "))
        break
    except:
        print("Ingrese un número válido.")

for i in range(cantidad):
    while True:
        try:
            valor = int(input(f"Ingrese el valor {i+1}: "))
            lista_dinamica.append(valor)
            break
        except:
            print("Ingrese un número válido.")

print("Lista dinámica final:", lista_dinamica)


# ---------------------------
# PILA (LIFO)
# ---------------------------
print("\n=== PILA (LIFO) ===")
pila = []

while True:
    print("\n1. Insertar")
    print("2. Eliminar")
    print("3. Ver pila")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        try:
            valor = int(input("Ingrese valor: "))
            pila.append(valor)
        except:
            print("Valor inválido")

    elif opcion == "2":
        if pila:
            print("Se eliminó:", pila.pop())
        else:
            print("La pila está vacía")

    elif opcion == "3":
        print("Pila actual:", pila)

    elif opcion == "4":
        break

    else:
        print("Opción inválida")


# ---------------------------
# COLA (FIFO)
# ---------------------------
print("\n=== COLA (FIFO) ===")
cola = deque()

while True:
    print("\n1. Insertar")
    print("2. Eliminar")
    print("3. Ver cola")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        try:
            valor = int(input("Ingrese valor: "))
            cola.append(valor)
        except:
            print("Valor inválido")

    elif opcion == "2":
        if cola:
            print("Se eliminó:", cola.popleft())
        else:
            print("La cola está vacía")

    elif opcion == "3":
        print("Cola actual:", list(cola))

    elif opcion == "4":
        break

    else:
        print("Opción inválida")