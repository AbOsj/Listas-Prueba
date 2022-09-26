from Pulperia import Producto as prod, ListadoProd as lst
from os import system
lProd = lst()

def menu():
    print("1. Agregar un nuevo producto")
    print("2. Editar un producto")
    print("3. Eliminar un producto")
    print("4. Buscar Producto por código")
    print("5. Buscar Producto por Precio")
    print("6. Buscar Producto por Nombre")
    print("7. Mostrar todos los productos")
    print("8. Salir")
    op = int(input("Escriba su opción: "))
    return op

def agregarProducto():
    print("Agregar Producto")
    codigo = input("Código: ")
    nombre = input("Producto: ")
    descripcion = input("Descripcion del producto: ")
    precio = int(input("Precio: "))
    minimoex = int(input("Digita la existencia minima: "))
    ex = int(input("Digita cuantas unidades en existencia hay del producto: "))
    productos = prod(codigo, nombre, descripcion, precio, minimoex, ex)
    if minimoex<ex:
        print("Todo correcto, los productos existentes son mayores que el minimo permitdo")
    else: 
        print("Error 1: Los productos existentes son menores que el mínimo")    
    lProd.agregarElemento(productos)
    print("Producto agregado uwu")
    system("pause")  

def modificarProducto():
    print("Editar Producto")
    cod = input("Código: ")
    est1, pos = lProd.buscarElemento(cod)
    print (f"""Producto Actual {pos}: """)
    print(prod)
    print("Nuevos Datos")
    nuevoProducto = input("Nombres: ")
    nuevaDescripcion = input("Descripcion: ")
    nuevoPrecio = int(input("Precio: "))
    nuevaExistencia = input("Hay Producto en existencia: ")
    if(nuevaExistencia.upper() == "SI"): nuevaExistencia = True
    else: nuevaExistencia = False
    newMinimo = int(input("Minimo: "))
    newProd = prod(cod, nuevoProducto, nuevaDescripcion, nuevoPrecio, nuevaExistencia, newMinimo)
    lProd.editarElemento(newProd, pos)

def eliminarProducto():
    print("Eliminar Producto")
    cod = input("Código: ")
    prod, pos = lProd.buscarElemento(cod)
    print(f"""Realmente desea eliminar el producto seleccionado? {prod}""")
    resp = input("SI - NO: ")
    if resp.upper()=="SI":
        lProd.eliminarElemento(prod)
    else:
        print("Operación cancelada")

def buscarProductoCod():
    print("Buscar Producto")
    cod = input("Código: ")
    try:
        prod, pos = lProd.buscarElemento(cod)
 
        if prod.Codigo != None:
            print (prod)
    except:
        print("El producto ha sido exitosamente encontrado uwu")
        
def mostrarProducto():
    for Producto in lProd.lista:
        print(Producto)
        print("*"*30)
        system("pause")

def buscarProductoPrecio():
    print("Buscar Producto por Precio")
    precio = int(input("Precio: "))
    try:
        pre, pos = lProd.buscarPPrecio(precio)

        if pre.Precio != None:
            print(pre)
    except:
        print("Todo bien, sigue")

def buscarProductoNombre():
    print("Buscar Producto por Nombre")
    nom = input("Nombre: ")
    try:
        p1, pos = lProd.buscarPNombre(nom)

        if p1.Nombres != None:
            print(p1)
    except:
        print("Todo bien, sigue")
def main():
    op = 0
    while(op!=10):
        op = menu()
        if op   == 1: agregarProducto()
        elif op == 2: modificarProducto()
        elif op == 3: eliminarProducto()
        elif op == 4: buscarProductoCod()
        elif op == 5: buscarProductoPrecio()
        elif op == 6: buscarProductoNombre()
        elif op == 7: mostrarProducto()
        elif op == 10: print("Have a nice day...")
        else: print("Opcion no valida")

main()