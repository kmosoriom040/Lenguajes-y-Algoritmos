#En esta versión 2 del programa búsqueda binaria, se le solicita al ususario una lista de número ordenados y un número. El programa solamente le indicará si pertenece o no a la lista.
## Se define la funcion de busqueda binaria
def busqueda_binaria(lista, n, objetivo):

	## se define el inicio
	i = 0

	## se escriben las variables que definen el rango de busqueda
	## y se inician con las condiciones de la lista
	izq = 0
	der = n - 1

	## repitiendo sobre la lista
	while i < n:
		## buscando el punto medio
		punto_medio = (izq + der) // 2

		## se compara el punto medio con el elemento objetivo
		if lista[punto_medio] == objetivo:
			## si esta entonces es verdadero
			return True
		elif lista[punto_medio] <objetivo:
			## ajustando el area de busqueda a la derecha
			izq = punto_medio + 1
		else:
			## ajustando el area de busqueda a la izquierda
			der = punto_medio - 1
		i += 1
	return False


if __name__ == '__main__':
	## iniciando el proceso para que el usuario provea una lista 
	lista =  list(input("Ingrese una lista de números positivos ordenados limitada por paréntesis cuadrados"))
	n = len(lista)
	elemento_objetivo=input("Ingrese el numero el cual desea comprobar que está en la lista:")
	# se hace que el usuario pida buscar el elemento

	if busqueda_binaria(lista, n, elemento_objetivo):
		print(elemento_objetivo, "pertenece")
	else:
		print(elemento_objetivo, "no pertenece")
