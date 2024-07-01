def nuevo_producto(inventario):
    nombre = input("Ingrese el nombre del nuevo producto: ")
    cantidad = int(input("Ingrese la cantidad inicial del producto: "))
    inventario.append([nombre, cantidad])
    print("Producto agregado al inventario.")

def compras(inventario):
    producto = input("Ingrese el nombre del producto que se va a comprar: ")
    cantidad = int(input("Ingrese la cantidad del producto que se va a comprar: "))
    for item in inventario:
        if item[0] == producto:
            item[1] += cantidad
            print(f"Compra registrada. Inventario actualizado. Cantidad actual en inventario de {producto}: {item[1]}")
            return
    inventario.append([producto, cantidad])
    print(f"Compra registrada. Inventario actualizado. Cantidad actual en inventario de {producto}: {cantidad}")

def ventas(inventario):
    producto = input("Ingrese el nombre del producto que se va a vender: ")
    cantidad = int(input("Ingrese la cantidad del producto que se va a vender: "))
    for item in inventario:
        if item[0] == producto:
            if item[1] >= cantidad:
                item[1] -= cantidad
                print(f"Venta registrada. Inventario actualizado. Cantidad actual en inventario de {producto}: {item[1]}")
            else:
                print("No hay suficiente inventario para realizar esta venta.")
            return
    print("El producto no se encuentra en el inventario.")

def mostrar_inventario(inventario):
    print("Inventario:")
    for producto, cantidad in inventario:
        print(f"{producto}: {cantidad}")

def menu():
    inventario = []
    
    while True:
        print("\nMenú:")
        print("1. Ingresar un nuevo producto")
        print("2. Ingresar compras de productos")
        print("3. Ingresar ventas de productos")
        print("4. Mostrar lista de productos con su inventario")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nuevo_producto(inventario)
        elif opcion == "2":
            compras(inventario)
        elif opcion == "3":
            ventas(inventario)
        elif opcion == "4":
            mostrar_inventario(inventario)
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

menu()
