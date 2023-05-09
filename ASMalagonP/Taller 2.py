# Algoritmo para listar los números primos hasta un valor n ingresado
# Pedimos al usuario que ingrese el valor de n, es decir,
#el valor hasta que se obtendrán los números primos
n = int(input("Ingresa un valor n: "))
# es_primo; actúa como función para definir si los números arrojados son primos
def es_primo(numero):
    if numero < 1:
      return False
    for i in range(2, numero):
      if numero % i == 0:
        return False
    return True
primos = []
# Iteramos sobre los números del 0 hasta n para verificar si son primos
for numero in range(2, n+1):
    if es_primo(numero):
        primos.append(numero)
#Finalmente imprimimos los números primos contenidos en la lista que se creó
print("Los números primos hasta", n, "son:", primos)
 #Angela Malagon_20221107081
