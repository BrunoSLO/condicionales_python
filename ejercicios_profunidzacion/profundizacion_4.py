# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor

IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''

print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio

palabra1 = str(input("ingresar palabra: "))
palabra2 = str(input("ingresar palabra: "))
palabra3 = str(input("ingresar palabra: "))

letras1 = len(palabra1) # Cantidad de caracteres
letras2 = len(palabra2)
letras3 = len(palabra3)

opcion = int(input("ingresar numero 1 si desea ordenar alfabeticamente o 2 si desea ordenar por cantidad de letras: "))

if (opcion == 1):
    if palabra1 > palabra2 and palabra2 > palabra3:
        print("el orden alfabetico es:", palabra1, palabra2, palabra3)
    elif palabra1 > palabra2 and palabra3 > palabra2:
        print("el orden alfabetico es:", palabra1, palabra3, palabra2)
    elif palabra2 > palabra1 and palabra1 > palabra3:
        print("el orden alfabetico es:", palabra2, palabra1, palabra3)
    elif palabra2 > palabra1 and palabra3 > palabra1:
        print("el orden alfabetico es", palabra2, palabra3, palabra1)
    elif palabra3 > palabra1 and palabra1 > palabra2:
        print("el orden alfabetico es:", palabra3, palabra1, palabra2)
    elif palabra3 > palabra1 and palabra2 > palabra1:
        print("el orden alfabetico es:", palabra3, palabra2, palabra1)

    
elif (opcion == 2):
    if letras1 > letras2 and letras2 > letras3:
        print("el orden por cantidad de letras es: ", letras1, letras2, letras3) 
    elif letras1 > letras2 and letras3 > letras2:
        print("el orden por cantidad de letras es:", letras1, letras3, letras2)
    elif letras2 > letras1 and letras1 > letras3:
        print("el orden por cantidad de letras es", letras2, letras1, letras3)
    elif letras2 > letras1 and letras3 > letras1:
            print("el orden por cantidad de letras es", letras2, letras3, letras1)
    elif letras3 > letras2 and letras2 > letras1:
        print("el orden por cantidad de letras es:", letras3, letras2, letras1)
    elif letras3 > letras2 and letras1 > letras2:
        print("el orden por cantidad de letras es:", letras3, letras1, letras2)
        


    
