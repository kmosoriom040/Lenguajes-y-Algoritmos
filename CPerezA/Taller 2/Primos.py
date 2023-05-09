def lista_primos(n) 
    numeros = list(range(2, n+1)) # Inicializamos una lista de números del 2 hasta n
    primos = [] # Creamos una lista para almacenar los números primos
    while numeros:
        p = numeros.pop(0) # Tomamos el primer número de la lista y lo añadimos a la lista de primos
        primos.append(p)
        numeros = [n for n in numeros if n % p != 0] # Eliminamos todos los múltiplos de p de la lista de números
    return primos
