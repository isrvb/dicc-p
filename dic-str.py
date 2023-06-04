#Diccionario OSINT

import string

def generar_diccionario():
    longitud = int(input("Ingrese la longitud de las claves del diccionario: "))
    incluir_mayusculas = input("¿Desea incluir letras mayúsculas? (s/n): ").lower() == "s"
    incluir_minusculas = input("¿Desea incluir letras minúsculas? (s/n): ").lower() == "s"
    incluir_numeros = input("¿Desea incluir números? (s/n): ").lower() == "s"
    incluir_simbolos = input("¿Desea incluir símbolos? (s/n): ").lower() == "s"
    
    caracteres = ""
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation
    
    diccionario = {}
    generar_claves(diccionario, "", longitud, caracteres)
    
    return diccionario

def generar_claves(diccionario, clave_actual, longitud, caracteres):
    if len(clave_actual) == longitud:
        diccionario[clave_actual] = ""
    else:
        for caracter in caracteres:
            generar_claves(diccionario, clave_actual + caracter, longitud, caracteres)

diccionario = generar_diccionario()

# Imprimir las claves generadas
for clave in diccionario:
    print(clave)
