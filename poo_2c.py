class Personaje:
    #atributos de la clase
    nombre = "default"
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0
    

#variable del constructor vacío
mi_personaje = Personaje()
#modificando valores de los atributos
mi_personaje.nombre = "EstebanDido"
mi_personaje.fuerza = 300
mi_personaje.inteligencia = -2
mi_personaje.defensa = 30
mi_personaje.vida = 2

print("el nombre de mi personaje es: ", mi_personaje.nombre)
print("vida de mi personaje es: ", mi_personaje.vida)
print("fuerza de mi personaje es: ", mi_personaje.fuerza)
print("inteligencia de mi personaje es: ", mi_personaje.inteligencia)
print("defensa de mi personaje es: ", mi_personaje.defensa)