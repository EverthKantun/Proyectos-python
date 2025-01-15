class Personaje:
    #atributos de la clase
    # nombre = "default"
    # fuerza = 0
    # inteligencia = 0
    # defensa = 0
    # vida = 0
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        #self es una referencia al mismo objeto
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida
        
# preguntas de examen
# ¿que es self en programación? es una referencia al mismo objeto
# ¿qué es el método init?  constructor que inicializa atributos de un objeto
# ¿por qué se usa doble guión bajo? dunder, método especial de python, mágico
# ¿cuando se ejecuta el método init? se ejecuta automático al crear un objeto
# #signo igual es asignar una variable

    def imprimir_atributos(self):
        print(self.__nombre, "tiene:")
        print("-Fuerza:", self.__fuerza)
        print("-Inteligencia:", self.__inteligencia)
        print("-defensa:", self.__defensa)
        print("-vida:", self.__vida)
        
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.__fuerza = self.__fuerza + fuerza
        self.__inteligencia = self.__inteligencia + inteligencia
        self.__defensa = self.__defensa + defensa
        
    def esta_vivo(self):
        return self.__vida > 0 
    
    def morir(self):
        self.__vida = 0
        print(self.__nombre, "ha muerto")
    
    def dañar(self, enemigo):
        return self.__fuerza - enemigo.__defensa
    
    def atacar(self, enemigo):
        daño = self.dañar(enemigo)
        # Si el daño es negativo, lo ajustamos a 0
        if daño < 0:
            daño = 0
        # Evitar que la vida del enemigo sea negativa
        if enemigo.__vida - daño < 0:
            enemigo.__vida = 0
        else:
            enemigo.__vida -= daño
        print(self.__nombre, "ha realizado", daño, "puntos de daño a", enemigo.__nombre)
        print("vida de ", enemigo.__nombre, "es ", enemigo.__vida)
        
    def get_vida(self):
        return self.__vida
    
    def set_vida(self, vida):
        self.__vida = vida
        if self.__vida <= 0: 
            self.morir()
    
#variable del constructor vacío
mi_personaje = Personaje("EstebanDido", 100, 50, 45, 100)
mi_enemigo = Personaje("Ángel", 70, 100, 400, 100)
mi_personaje.imprimir_atributos()
mi_personaje.vida = 0
print(f"hola: {mi_personaje.get_vida()}")
mi_personaje.set_vida(-5)
print(f"actualizado: {mi_personaje.get_vida()}")
mi_personaje._Personaje__vida = -50
#mi_personaje.vida()
mi_personaje.imprimir_atributos()
# mi_enemigo.imprimir_atributos()
#mi_personaje.atacar(mi_enemigo)
#print(mi_personaje.esta_vivo())
# mi_personaje.subir_nivel(15, 5, 10)
# print("valores actualizados")
# mi_personaje.imprimir_atributos()

#modificando valores de los atributos
# mi_personaje.__nombre = "EstebanDido"
# mi_personaje.__fuerza = 300
# mi_personaje.__inteligencia = -2
# mi_personaje.__defensa = 30
# mi_personaje.__vida = 2

# print("el nombre de mi personaje es: ", mi_personaje.__nombre)
# print("vida de mi personaje es: ", mi_personaje.__vida)
# print("fuerza de mi personaje es: ", mi_personaje.__fuerza)
# print("inteligencia de mi personaje es: ", mi_personaje.__inteligencia)
# print("defensa de mi personaje es: ", mi_personaje.__defensa)