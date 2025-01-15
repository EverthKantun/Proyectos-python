class Personaje:
    #atributos de la clase
    # nombre = "default"
    # fuerza = 0
    # inteligencia = 0
    # defensa = 0
    # vida = 0
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        #self es una referencia al mismo objeto
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
        
# preguntas de examen
# ¿que es self en programación? es una referencia al mismo objeto
# ¿qué es el método init?  constructor que inicializa atributos de un objeto
# ¿por qué se usa doble guión bajo? dunder, método especial de python, mágico
# ¿cuando se ejecuta el método init? se ejecuta automático al crear un objeto
# #signo igual es asignar una variable

    def imprimir_atributos(self):
        print(self.nombre, "tiene:")
        print("-Fuerza:", self.fuerza)
        print("-Inteligencia:", self.inteligencia)
        print("-defensa:", self.defensa)
        print("-vida:", self.vida)
        
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
        
    def esta_vivo(self):
        return self.vida > 0 
    
    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")
    
    def dañar(self, enemigo):
        return self.fuerza - enemigo.defensa
    
    def atacar(self, enemigo):
        daño = self.dañar(enemigo)
        # Si el daño es negativo, lo ajustamos a 0
        if daño < 0:
            daño = 0
        # Evitar que la vida del enemigo sea negativa
        if enemigo.vida - daño < 0:
            enemigo.vida = 0
        else:
            enemigo.vida -= daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        print("vida de ", enemigo.nombre, "es ", enemigo.vida)
        
class Guerrero(Personaje):
    
    #sobreescribir el constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

arturoSuarez = Guerrero("Arturo Suarez", 12, 3000, 2, 100, .5)
arturoSuarez.imprimir_atributos()
print("el valor de la espada es:", arturoSuarez.espada)
    
#variable del constructor vacío
mi_personaje = Personaje("EstebanDido", 100, 50, 45, 100)
mi_enemigo = Personaje("Ángel", 70, 100, 400, 100)
mi_personaje.imprimir_atributos()
mi_enemigo.imprimir_atributos()
mi_personaje.atacar(mi_enemigo)
#print(mi_personaje.esta_vivo())
# mi_personaje.subir_nivel(15, 5, 10)
# print("valores actualizados")
# mi_personaje.imprimir_atributos()

#modificando valores de los atributos
# mi_personaje.nombre = "EstebanDido"
# mi_personaje.fuerza = 300
# mi_personaje.inteligencia = -2
# mi_personaje.defensa = 30
# mi_personaje.vida = 2

# print("el nombre de mi personaje es: ", mi_personaje.nombre)
# print("vida de mi personaje es: ", mi_personaje.vida)
# print("fuerza de mi personaje es: ", mi_personaje.fuerza)
# print("inteligencia de mi personaje es: ", mi_personaje.inteligencia)
# print("defensa de mi personaje es: ", mi_personaje.defensa)