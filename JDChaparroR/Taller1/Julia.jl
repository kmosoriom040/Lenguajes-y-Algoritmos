# Pidiendo al usuario cuántas veces desea imprimir "Hola Mundo"
println("Ingrese la cantidad de veces que desea imprimir 'Hola Mundo': ")
n = parse(Int64, readline())

# Utilizando un bucle for para imprimir "Hola Mundo" n veces
for i in 1:n
    println("Hola Mundo")
end