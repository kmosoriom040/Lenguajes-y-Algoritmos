#Psudocódigo:

#1. Leer el valor de n ingresado por el usuario.
#2. Crear una lista vacía para almacenar los números primos encontrados.

#3. Inicializar un bucle for que recorra los números del 2 al n (ambos incluidos).

#4. En cada iteración del bucle for, inicializar una variable booleana como verdadera para comprobar si el número es primo.

#5. Inicializar un segundo bucle for que recorra los números del 2 al número actual (menos 1).

#6. En cada iteración del segundo bucle for, comprobar si el número actual es divisible por el número actual del segundo bucle for.

#7. Si el número actual es divisible por cualquier número en el segundo bucle for, establecer la variable booleana a falso y salir del segundo bucle for.

#8. Si la variable booleana es verdadera después de recorrer todos los números del segundo bucle for, el número actual es primo. Añadir el número a la lista de números primos.

#9. Imprimir la lista de números primos encontrados.


#Código de Python:

n = int(input("Ingrese un número entero: "))
primos = []

for i in range(2, n+1):
    es_primo = True
    for j in range(2, i):
        if i % j == 0:
            es_primo = False
            break
    if es_primo:
        primos.append(i)

print("Los números primos hasta", n, "son:", primos)
