"""""1) Escribir una clase llamada Rectángulo que contenga una base y una altura, y que contenga un método que devuelva el área
del rectángulo."""

# class Rectangulo:
#     def __init__(self, base, altura):
#         self.base = base
#         self.altura = altura
    
#     def calcular_area(self):
#         return self.base * self.altura

# # Crear un objeto Rectángulo
# base = 5
# altura = 3
# mi_rectángulo = Rectangulo(base, altura)

# # Calcular y mostrar el área del rectángulo
# area = mi_rectángulo.calcular_area()
# print(f"El área del rectángulo con base {base} y altura {altura} es: {area}")

"""2) Modelar una clase Mate que describa el funcionamiento de la conocida bebida tradicional argentina. La clase debe contener
como miembros:
o Un atributo para la cantidad de cebadas restantes hasta que se lava el mate (representada por un número).
o Un atributo para el estado (lleno o vacío).
o Un atributo n, que indica la cantidad máxima de cebadas.
o Un método cebar, que llena el mate con agua. Si se intenta cebar con el mate lleno, se debe lanzar una
excepción que imprima el mensaje ¡Cuidado! ¡Te quemaste!
o Un método beber, que vacía el mate y le resta una cebada disponible. Si se intenta beber un mate vacío, se
debe lanzar una excepción que imprima el mensaje: ¡El mate está vacío!
o Es posible seguir cebando y bebiendo el mate aunque no haya cebadas disponibles. En ese caso la cantidad
de cebadas restantes se mantendrá en 0, y cada vez que se intente beber se debe imprimir un mensaje de aviso:
“Advertencia: el mate está lavado.” pero no se debe lanzar una excepción."""

# class Mate:
#     def __init__(self, n):
#         self.n = n
#         self.cebadas_restantes = n
#         self.lleno = False

#     def cebar(self):
#         if self.lleno:
#             raise Exception("¡Cuidado! ¡Te quemaste!")
#         else:
#             self.lleno = True
#             self.cebadas_restantes = self.n

#     def beber(self):
#         if not self.lleno:
#             raise Exception("¡El mate está vacío!")
#         else:
#             if self.cebadas_restantes > 0:
#                 self.cebadas_restantes -= 1
#                 if self.cebadas_restantes == 0:
#                     self.lleno = False
#                 return "¡Delicioso!"
#             else:
#                 return "Advertencia: el mate está lavado."

# mi_mate = Mate(5)

# mi_mate.cebar()
# print(mi_mate.beber())  # Output: ¡Delicioso!
# print(mi_mate.beber())  # Output: ¡Delicioso!
# print(mi_mate.beber())  # Output: ¡Delicioso!
# print(mi_mate.beber())  # Output: ¡Delicioso!
# print(mi_mate.beber())  # Output: ¡Delicioso!
# print(mi_mate.beber())  # Output: Advertencia: el mate está lavado.

"""3) Botella y Sacacorchos
 Escribir una clase Corcho, que contenga un atributo bodega (cadena con el nombre de la bodega).
 Escribir una clase Botella que contenga un atributo corcho con una referencia al corcho que la tapa, o None si está
destapada.
 Escribir una clase Sacacorchos que tenga un método destapar que le reciba una botella, le saque el corcho y se guarde
una referencia al corcho sacado. Debe lanzar una excepción en el caso en que la botella ya esté destapada, o si el
sacacorchos ya contiene un corcho.
 Agregar un método limpiar, que saque el corcho del sacacorchos, o lance una excepción en el caso en el que no haya
un corcho"""

# class Corcho:
#     def __init__(self, Bodega):
#         self.Bodega=Bodega
    
#     def __str__(self):
#         return self.Bodega

# class Botella:
#     def __init__(self, Corcho:Corcho):
#         self.CorchoDeBotella=Corcho

# class Sacacorcho:
#     def __init__(self):
#         self.CorchoSacacorcho=None
    
#     def Destapar(self,Botella:Botella):
#         if self.CorchoSacacorcho==None:
#             if Botella.CorchoDeBotella!=None:
#                 self.CorchoSacacorcho=Botella.CorchoDeBotella
#                 Botella.CorchoDeBotella=None
#                 print("Botella destapada")
#             else:
#                 print("La botella ya esta destapada")
#         else:
#             print("El sacacorchos ya tiene un corcho, primero hay que limpiarlo")
            
#     def Limpiar(self):
#         if self.CorchoSacacorcho==None:
#             print("El sacacorchos ya esta limpio")
#         else:
#             self.CorchoSacacorcho=None
#             print("Sacacorcho limpiado")



"""4) Una heladería es un tipo especial de restaurante. Cree una clase Restaurante, cuyo método __init__() guarde dos atributos:
restaurante_nombre y tipo_comida. Cree un método describir_restaurante() que muestre estas piezas de información, y un
método abrir_restaurante() que muestre un mensaje indicando que el restaurante ahora está abierto. Luego cree una clase
Heladeria que herede de Restaurante, y agregue a los existentes un atributo llamado sabores que almacene una lista de los
sabores de helado disponibles. Escriba también un método que muestre estos valores, cree una instancia de la clase y llame
al método."""

# class Restaurante:
#     def __init__(self, restaurante_nombre, tipo_comida):
#         self.restaurante_nombre = restaurante_nombre
#         self.tipo_comida = tipo_comida
    
#     def describir_restaurante(self):
#         print(f"Restaurante: {self.restaurante_nombre}")
#         print(f"Tipo de comida: {self.tipo_comida}")
    
#     def abrir_restaurante(self):
#         print(f"¡{self.restaurante_nombre} ahora está abierto!")

# class Heladeria(Restaurante):
#     def __init__(self, restaurante_nombre, tipo_comida, sabores):
#         super().__init__(restaurante_nombre, tipo_comida)
#         self.sabores = sabores
    
#     def describir_sabores(self):
#         print("Sabores de helado disponibles:")
#         for sabor in self.sabores:
#             print("- " + sabor)

# sabores_helado = ["Chocolate", "Vainilla", "Fresa", "Mango"]
# heladeria = Heladeria("La Heladería Delicia", "Heladería", sabores_helado)

# heladeria.describir_restaurante()
# heladeria.abrir_restaurante()

# heladeria.describir_sabores()

"""5) Escribir una clase Personaje que contenga los atributos vida, posicion y velocidad, y los métodos recibir_ataque, que
reduzca la vida según una cantidad recibida y lance una excepción si la vida pasa a ser menor o igual que cero, y mover
que reciba una dirección y se mueva en esa dirección la cantidad indicada por velocidad.
 Escribir una clase Soldado que herede de Personaje, y agregue el atributo ataque y el método atacar, que reciba otro
personaje, al que le debe hacer el daño indicado por el atributo ataque.
 Escribir una clase Campesino que herede de Personaje, y agregue el atributo cosecha y el método cosechar, que
devuelva la cantidad cosechada"""


# class Personaje:
#     def __init__(self, vida, posicion, velocidad):
#         self.vida = vida
#         self.posicion = posicion
#         self.velocidad = velocidad

#     def recibir_ataque(self, cantidad):
#         self.vida -= cantidad
#         if self.vida <= 0:
#             raise Exception("El personaje ha muerto.")

#     def mover(self, direccion):
#         self.posicion += self.velocidad * direccion

# class Soldado(Personaje):
#     def __init__(self, vida, posicion, velocidad, ataque):
#         super().__init__(vida, posicion, velocidad)
#         self.ataque = ataque

#     def atacar(self, personaje_objetivo):
#         personaje_objetivo.recibir_ataque(self.ataque)

# class Campesino(Personaje):
#     def __init__(self, vida, posicion, velocidad, cosecha):
#         super().__init__(vida, posicion, velocidad)
#         self.cosecha = cosecha

#     def cosechar(self):
#         return self.cosecha


# soldado1 = Soldado(100, 0, 5, 20)
# soldado2 = Soldado(100, 10, 6, 25)
# campesino = Campesino(50, 2, 2, 10)

# print("Vida del soldado 1:", soldado1.vida)
# print("Vida del soldado 2:", soldado2.vida)

# soldado1.atacar(soldado2)
# print("Vida del soldado 2 después del ataque:", soldado2.vida)

# print("Posición inicial del campesino:", campesino.posicion)
# campesino.mover(1)
# print("Posición del campesino después de moverse:", campesino.posicion)

# print("Cantidad cosechada por el campesino:", campesino.cosechar())

"""6)Usuarios: Cree una clase Usuario. Cree también dos atributos nombre y apellido, así como otros atributos que típicamente
se guardan en un perfil de usuario. Escriba un método describir_usuario() que muestre un resumen de la información del
usuario. Escriba otro método saludar_usuario() que muestre un saludo personalizado al usuario.
Cree varias instancias que representen distintos usuarios y llame ambos métodos para cada uno."""

# class Usuario:
#     def __init__(self, nombre, apellido, edad, ubicacion, ocupacion):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#         self.ubicacion = ubicacion
#         self.ocupacion = ocupacion

#     def describir_usuario(self):
#         print(f"Nombre: {self.nombre} {self.apellido}")
#         print(f"Edad: {self.edad}")
#         print(f"Ubicación: {self.ubicacion}")
#         print(f"Ocupación: {self.ocupacion}")

#     def saludar_usuario(self):
#         print(f"Hola, {self.nombre} ¡Bienvenido de nuevo!")


# usuario1 = Usuario("Juan", "Pérez", 25, "Ciudad de México", "Estudiante")
# usuario2 = Usuario("María", "González", 32, "Madrid", "Ingeniera")
# usuario3 = Usuario("Carlos", "Sánchez", 45, "Buenos Aires", "Abogado")

# usuario1.describir_usuario()
# usuario1.saludar_usuario()

# print("\n")

# usuario2.describir_usuario()
# usuario2.saludar_usuario()

# print("\n")

# usuario3.describir_usuario()
# usuario3.saludar_usuario()

"""7) Admin: Un administrador es un tipo de usuario con privilegios especiales. Cree una clase Admin que herede de la clase
Usuario del ejercicio anterior y agréguele un atributo privilegios que almacene una lista de strings tales como “puede
postear en el foro”, “puede borrar un post”, “puede banear usuario”, etc. Escriba un método mostrar_privilegios() que
muestre el conjunto de privilegios del administrador, cree una instancia de la clase y llame al método."""
class Usuario:
    def __init__(self, nombre, apellido, edad, ubicacion, ocupacion):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.ubicacion = ubicacion
        self.ocupacion = ocupacion

    def describir_usuario(self):
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"Edad: {self.edad}")
        print(f"Ubicación: {self.ubicacion}")
        print(f"Ocupación: {self.ocupacion}")

    def saludar_usuario(self):
        print(f"Hola, {self.nombre} ¡Bienvenido de nuevo!")

class Admin(Usuario):
    def __init__(self, nombre, apellido, edad, ubicacion, ocupacion, privilegios):
        super().__init__(nombre, apellido, edad, ubicacion, ocupacion)
        self.privilegios = privilegios

    def mostrar_privilegios(self):
        print(f"Privilegios del administrador {self.nombre}:")
        for privilegio in self.privilegios:
            print(f"- {privilegio}")


admin1 = Admin("Admin", "Principal", 30, "Ciudad Administrativa", "Administrador", ["puede postear en el foro", "puede borrar un post", "puede banear usuario"])


admin1.describir_usuario()
admin1.mostrar_privilegios()
admin1.saludar_usuario()




