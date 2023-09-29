texto = input("Introduzca una palabra o texto: ")

vacio = ""

for cadena in texto:
    if cadena not in ['a', 'e', 'i', 'o', 'u']:
        vacio +=cadena

print(vacio)
