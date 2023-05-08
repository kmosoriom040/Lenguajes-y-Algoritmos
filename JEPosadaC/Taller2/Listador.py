
def primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def listar_primos(n):
    l_primos = []
    for numero in range(2, n + 1):
        if primo(numero):
            l_primos.append(numero)
    return l_primos

numero= int(input("Ingrese un número límite: "))
lista_primos = listar_primos(numero)
print("Números primos hasta", numero, ":")
print(lista_primos)