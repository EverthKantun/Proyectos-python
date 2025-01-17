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
        #aquí podriamos usar el max max(0, self.fuerza - enemigo.defensa)
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
    
    #sobrescribir el constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    #sobrescribir impresión de atributos
    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("valor de la espada: ", self.espada)
    
    #sobrescribir el cálculo del daño
    def dañar(self, enemigo):
        return self.fuerza*self.espada - enemigo.defensa
        
    #escoger navaja
    def escoger_navaja(self):
        opcion = int(input("escoge la navaja de la muerte: \n (1) Navaja suiza, daño 10. \n (2) Navaja pioja, daño 6. \n >>>>>>>>"))
        if(opcion == 1):
            self.espada = 10
        elif(opcion == 2):
            self.espada = 6
        else:
            print("Valor inválido, intente nuevamente")
            #lo regresamos a elegir
            self.escoger_navaja()
    
class Mago(Personaje):
    
    #sobrescribir el constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    #sobrescribir impresión de atributos
    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("valor de su libro de hechizos: ", self.libro)
    
    #sobrescribir el cálculo del daño
    def dañar(self, enemigo):
        return self.inteligencia*self.libro - enemigo.defensa
        
    #escoger navaja
    def escoger_libro(self):
        opcion = int(input("escoge el libro de la sabiduría: \n (1) El principito, daño 10. \n (2) Crepúsculo, daño -10. \n >>>>>>>>"))
        if(opcion == 1):
            self.libro = 10
        elif(opcion == 2):
            self.libro = 6
        else:
            print("Valor inválido, intente nuevamente")
            #lo regresamos a elegir
            self.escoger_libro()
    


persona = Personaje("Ángel Suarez", 12, 3000, 2, 100)   
arturoSuarez = Guerrero("Arturo Suarez", 12, 3000, 2, 100, .5)
gandalf = Mago("Gandalf", 12, 3000, 2, 100, 5)
arturoSuarez.escoger_navaja()
gandalf.escoger_libro()
#atributos antes de la pelea
arturoSuarez.imprimir_atributos()
gandalf.imprimir_atributos()
persona.imprimir_atributos()
#iniciar ataques
persona.atacar(arturoSuarez)
arturoSuarez.atacar(gandalf)
gandalf.atacar(persona)
#atributos después de la tragedia
arturoSuarez.imprimir_atributos()
gandalf.imprimir_atributos()
persona.imprimir_atributos()

# print("el valor de la espada es:", arturoSuarez.espada)
    
#variable del constructor vacío
# mi_personaje = Personaje("EstebanDido", 100, 50, 45, 100)
# mi_enemigo = Personaje("Ángel", 70, 100, 400, 100)
# mi_personaje.imprimir_atributos()
# mi_enemigo.imprimir_atributos()
# mi_personaje.atacar(mi_enemigo)
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