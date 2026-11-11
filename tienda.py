
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
Pan= Producto ("Pan", 50)
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