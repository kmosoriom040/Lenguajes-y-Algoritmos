n = int(input("Bienvenido, este es un programa que muestra los números primos hasta un valor ingresado.Ingrese el valor: "))
for i in range(2, n+1): 
    es_primo = True  
    for j in range(2, i//2 + 1): 
        if i % j == 0:  
            es_primo = False 
            break   
    if es_primo:  
        print(i)