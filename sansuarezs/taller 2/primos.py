def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def lista_primos(minimo, maximo):
    primos = []
    for num in range(minimo, maximo+1):
        if es_primo(num):
            primos.append(num)
    return primos
