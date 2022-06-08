#Un diccionario anidado se puede crear pasandole datos de variables o
#creandolos directamente... dollie es una variable y bella se crea al momento

dollie={
    "nombre" : "Dollie",
    "edad" :12
}

gatitos={
    "Dollie" : dollie,
    "Bella":{
        "nombre":"Bella",
        "Edad" : 3
    }
}

print("Gatitos del diccionario: " , gatitos)

#Cambiar contenido del diccionario
#Metodo 1
gatitos.get("Dollie")["nombre"] ="Peperoni"
print("Cambiar atributo con get: ",gatitos)
#Metodo 2
gatitos["Dollie"]["nombre"] ="Dollie"
print("Cambiar atributo con array: ",gatitos)

#CREAR DICCIONARIOS CON dict
perritos=dict(nombre='niko', edad = 10)
print("Diccionario con dict:", perritos)
