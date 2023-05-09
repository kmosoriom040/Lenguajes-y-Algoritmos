num = int(input("Escribe un numero: "))

for i in range(2, num+1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(f"{i} es primo")