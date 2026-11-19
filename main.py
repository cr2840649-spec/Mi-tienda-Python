from abc import ABC, abstractmethod
#Clase abstracta que representa un producto
class Producto(ABC):
     def __init__ (self,nombre, precio, cantidad):
          self.nombre = nombre
          self.precio= precio
          self.cantidad = cantidad

     @abstractmethod
     def mostrar_informacion(self):
          pass
#Interfaz para la administracion de las existencias
class Inventario(ABC):

     @abstractmethod
     def anadir_producto(self,cantidad):
          pass
     @abstractmethod
     def eliminar_producto(self,cantidad):
          pass
#Subclase para productos electronicos
class Electronico(Producto, Inventario):
     def __init__(self, nombre, precio, cantidad, garantia): 
          super().__init__(nombre, precio, cantidad)
          self.garantia = garantia
     def mostrar_informacion(self):
          print("Producto:",self.nombre)
          print("Precio:", self.precio)
          print("Cantidad:", self.cantidad)
          print("Garantia:",self.garantia)
     def anadir_producto(self,cantidad):
          self.cantidad += cantidad
     def eliminar_producto(self,cantidad):
          self.cantidad -= cantidad 
    
Celular= Electronico ("Celular", 3500, 1,"6 meses")
Celular.mostrar_informacion()
Celular.anadir_producto(9)
print("Cantidad actual:", Celular.cantidad)
Celular.eliminar_producto(4)
print("Cantidad actual:", Celular.cantidad)

#Subclase para productos alimenticios 
class Alimentos(Producto, Inventario):
     def __init__(self,nombre, precio, cantidad, caducidad):
         super().__init__(nombre,precio,cantidad)
         self.caducidad = caducidad
     def mostrar_informacion(self):
          print("Producto:",self.nombre)
          print("Precio:", self.precio)
          print("Cantidad:", self.cantidad)
          print("Caducidad:", self.caducidad)
     def anadir_producto(self,cantidad):
          self.cantidad += cantidad
     def eliminar_producto(self,cantidad):
          self.cantidad -= cantidad 

Leche = Alimentos ("Leche", 50, 10, "10/12/2026")
Leche.mostrar_informacion()
Leche.anadir_producto(2)
print("Cantidad actual:", Leche.cantidad)
Leche.eliminar_producto(4)
print("Cantidad actual:", Leche.cantidad)

#Subclase para productos de vestimenta
class Ropa(Producto, Inventario):
     def __init__(self,nombre, precio, cantidad, talla):
         super().__init__(nombre, precio, cantidad)
         self.talla= talla
     def mostrar_informacion(self):
          print("Producto:",self.nombre)
          print("Precio:", self.precio)
          print("Cantidad:", self.cantidad)
          print("Talla:", self.talla)
     def anadir_producto(self,cantidad):
          self.cantidad += cantidad
     def eliminar_producto(self,cantidad):
          self.cantidad -= cantidad 
Pantalon = Ropa("Pantalon", 200 , 1, "30")
Pantalon.mostrar_informacion()
Pantalon.anadir_producto(7)
print("Cantidad actual:", Pantalon.cantidad)
Pantalon.eliminar_producto(3)
print("Cantidad actual:", Pantalon.cantidad)

#Conjunto de los datos
Celular = Electronico("Celular", 3500, 1,"6 meses")
Leche = Alimentos ("Leche", 50, 10, "10/12/2026")
Pantalon = Ropa("Pantalon", 200 , 1, "30")

#Separacion de datos
productos = [Celular, Leche, Pantalon]
for producto in productos:
    producto.mostrar_informacion()
    print("------")
           
#Prueba de interfaz 
for producto in productos:
     producto.anadir_producto(2)
     print("Cantidad despues de añadir:",producto.cantidad)

     producto.eliminar_producto(1)
     print("Cantidad despues de eliminar:", producto.cantidad)