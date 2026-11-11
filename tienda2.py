
class Producto:       
     def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio 
     def mostrar_informacion(self):
         print ("Producto self.nombre")
         print ("Producto self.precio")
         Pan.mostrar_informacion()
         Leche.mostrar_informacion ()
         Huevo.mostrar_informacion ()
Pan= Producto ("Pan", 50   )
print (Pan.nombre)
print (Pan.precio)  
Leche= Producto ("Leche", 45)
print (Leche.nombre)
print (Leche.precio)
Huevo= Producto ("Huevo", 60)
print (Huevo.nombre )
print (Huevo.precio) 

def calcula_total():
     total = Pan.precio + Leche.precio + Huevo.precio
     print("El total es:", total)
calcula_total()


class Productojuguetes (Producto):
    def __init__ (self,nombre,precio,cantidad):
      super().__init__ (nombre,precio)
      self.cantidad= cantidad
    def mostrar_cantidad(self):
       print("Cantidad a comprar:",self.cantidad)
    def calcular_total(self): 
      total= self.precio * self.cantidad
      print ("Total a pagar es:",total)
       
Pelota=Productojuguetes ("Pelota", 60, 2)
print(Pelota.nombre)
print(Pelota.precio)
Pelota.mostrar_cantidad()
Pelota.calcular_total()

Muñeca=Productojuguetes ("Muñeca", 100, 3)
print(Muñeca.nombre)
print(Muñeca.precio)
Muñeca.mostrar_cantidad()
Muñeca.calcular_total()


class ProductoElectronico (Producto):
     def __init__(self, nombre, precio, modelo, marca, garantia):
          super().__init__(nombre, precio)
          self.modelo= modelo
          self.marca = marca
          self.garantia = garantia
     def mostrar_informacion(self):
          print("Modelo:",self.modelo)
          print("Marca:",self.marca)
          print("Garantia:", self.garantia)

Celular= ProductoElectronico ("Celular", 3500,"Galaxy A15", "Samsung","1 año")
print(Celular.nombre)
print(Celular.precio)
Celular.mostrar_informacion()
Tableta= ProductoElectronico ("Tableta", 8000, "Tab M10 Plus","Lenovo", "6 meses")
print(Tableta.nombre)
print(Tableta.precio)
Tableta.mostrar_informacion()