num = int(input("Ingrese el valor del punto maximo del rango para calcular primos: ")
 
 for i in range(2, num+1):
          for j in range(2,i):
           if i % j == 0:
            break
          else:
           print(f"(i) es primo")
