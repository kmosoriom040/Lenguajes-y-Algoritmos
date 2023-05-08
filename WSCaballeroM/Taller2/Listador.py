def primo(n):  ##Creo una clase para definir que es un número primo
  if n==1:     ##Si el numero es igual a uno ejecute
    return False    ##Si no es así no haga nada, o envie un falso lógico.
  for x in range(2, n): ##Cree una variable x que pertenezca al intervalo entre 2 y el número
    if n % x ==0:  ##Si el número inicial dividido algún x tiene como residuo 0 ejecute
      return False  ##Envie un falso lógico
  return True       ##Envie un verdadero lógico y continue

contador=0          ##Indicar donde inicia el contador
n=2            ##Primer número primo
limite=float(input("Escribir la cantidad de numeros primos que desea:   ")) ##Ingrese la cantidad de números primos que sea obtener

while limite > contador:      ##Mientras que'l contador funcione, ejecute
  if primo(n):           ##Si el número es primo, ejecute
    contador +=1              ##avance
    print(contador, n)   ##Imprima el número del primo y el primo perse
    
  n += 1                 ##Pase al siguiente primo