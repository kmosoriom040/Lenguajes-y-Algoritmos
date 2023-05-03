Julia
println("Numero de veces que desea repetir Hola mundo:")
x = parse(Int64, readline())
for i in 1:x
  println("Hola mundo")
end