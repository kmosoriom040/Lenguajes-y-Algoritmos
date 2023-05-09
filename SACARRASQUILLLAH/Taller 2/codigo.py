n = int(input("Ingrese un número entero positivo: "))

primos = []

for num in range(2, n+1):
    es_primo = True

    for i in range(2, num):
        if num % i == 0:
            es_primo = False
            break

    if es_primo:
        primos.append(num)

print("Los números primos hasta", n, "son:", primos)
