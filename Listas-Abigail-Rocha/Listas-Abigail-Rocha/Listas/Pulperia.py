#Realice un programa que permita almacenar datos de un producto tales como:
#código, nombres, descripción, precio, existencia, existencia 
# mínima. El programa debe ser
#capaz de registrar cada producto, editar o modificar,
# buscar por código, nombre y precio, al
#igual que mostrar todos los productos con existencia menor
# que la existencia mínima,
#finalmente debe eliminar un producto especifico.
#Crear una lista de estudiante
"""
Create
Read
Update
Delete
"""

class Producto:

    def __init__(self, cod, nom, descrip, precio, exist,minimo):
        self.Codigo = cod
        self.Nombres = nom
        self.Descripcion = descrip
        self.Precio = precio
        self.Existencia = exist
        self.ExitenciaMinima = minimo
    def __str__(self):
        return f"""Codigo: {self.Codigo}
Nombres: {self.Nombres}
Descripcion: {self.Descripcion}
Precio: {self.Precio}
Existencia: {self.Existencia}
ExistenciaMinima: {self.ExitenciaMinima}
"""

class ListadoProd:

    def __init__(self):
        self.lista =[]
    
    def agregarElemento(self, dato):
        try:
            self.lista.append(dato)
        except Exception as ex:
            print("Ocurrio un error al agregar: ", str(ex))
        
    def editarElemento(self, dato, pos):
        try:
            self.lista[pos]=dato
        except Exception as ex:
             print("Ocurrio un error al editar:", str(ex))
    
    def eliminarElemento(self, est):
        try:
            self.lista.remove(est)
        except Exception as ex:
            print("Error al eliminar:", str(ex))
    
    def buscarElemento(self, codigo):
        try:
            pos = 0
            for est in self.lista:
                
                if est.Codigo == codigo:
                    print("Producto encontrado...")
                    return est, pos
                pos+=1
            else:
                print("No se encontro el producto deseado...")
            
        except Exception as ex:
            print("Error al buscar elemento:", str(ex))
    def buscarPNombre(self,Nombres):
        try:
            p=0
            for Art in self.lista:
                if Art.Nombres == Nombres:
                    print("Producto encontrado...")
                    return Art, p
            else:
                print("No se pudo encontrar el producto, intente nuevamente")
            p+=1
        except Exception as ex:
            print("Error al encontrar el producto")
        
    def buscarPPrecio(self, precio):
        try:
            p=0
            for Art in self.lista:
                if Art.Precio == precio:
                    return Art, p
            else:
                print("No se pudo encontrar el producto, intente nuevamente")
            p+=1
        except Exception as ex:
            print("Error al encontrar el producto")


    

    

