# PC 2

# EJERCICIO 1

for num in range(1500, 2701):
    if num % 7 == 0 and num % 5 == 0:
        print(num)



# EJERCICIO 2

a = 5

for i in range(1, a + 1,1):
        print("*"*(i))

for i in range(a - 1, 0, -1):
        print("*"*(i))



# EJERCICIO 3

num_pares = []
num_impares = []
num_ingresados = []

while True:
    consulta = input("¿Desea ingresar un número?: ")
    
    if consulta == "SI":
            numero = int(input("Ingrese el número: "))
            num_ingresados.append(numero)
            
            if numero % 2 == 0:
                num_pares.append(numero)
            else:
                num_impares.append(numero)

    elif consulta == "NO":
        break
    else:
        print("Respuesta inválida. Por favor, responda 'SI' o 'NO'.")

print("Números ingresados:", num_ingresados)
print("Cantidad de números pares:", len(num_pares))
print("Cantidad de números impares:", len(num_impares))


# EJERCICIO 4

listado_alumnos = []

n = int(input("Ingrese el número de alumnos: "))

for i in range(n):
    nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")
    
    notas = []
    for j in range(3):
        nota = int(input(f"Ingrese la nota {j + 1} para {nombre}: "))
        notas.append(nota)
    
    dic_alumnos = {
        "Alumno": nombre,
        "Notas": notas
    }
    listado_alumnos.append(dic_alumnos)

print(f"Se muestra el listado de los alumnos y sus notas:")
for dic_alumnos in listado_alumnos:
    print(f"El alumno {dic_alumnos['Alumno']} tiene las siguientes notas: {dic_alumnos['Notas']}.")


# EJERCICIO 5


# EJERCICIO 6

a, b = 0, 1

print(a)

while b < 50:
    print(b)
    a, b = b, a + b


# EJERCICIO 8
def factorial(num):
    if num == 0:
        return 1
    resultado = 1

    for i in range(1, num + 1):
        resultado *= i 
        return resultado

num = int(input("Ingrese un número entero no negativo: "))
resultado = factorial(num)
print(f"El factorial de {num} es {resultado}")


# EJERCICIO 9

texto = input("Introduzca una palabra o texto: ")

vacio = ""

for cadena in texto:
    if cadena not in ['a', 'e', 'i', 'o', 'u']:
        vacio +=cadena

print(vacio)
