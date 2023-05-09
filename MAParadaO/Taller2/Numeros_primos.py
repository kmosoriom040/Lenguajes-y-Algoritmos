n = int(input("Ingrese un valor para n: "))
for i in range(2, n+1): #Revisa los numeros i en el inetrvalo
    es_primo = True  
    for j in range(2, i//2 + 1): #Prueba de divisibiladad de i sobre j
        if i % j == 0:  
            es_primo = False #Si i es divisible salir del bucle
            break   
    if es_primo:  
        print(i) #Imprime los numeros primos hasta n
#Basado en el pseudocodigo puesto en uno de los trabajos anteriores
