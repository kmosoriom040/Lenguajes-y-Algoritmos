TALLER:

    Realizar un programa "Hola mundo", que solicite la cantidad de "Hola mundo".
    Python-Código:

#Este es un algoritmo que permite imprimir una cantidad n de "hola mundo" que la persona quiera.

cantidad = int(input("Ingrese la cantidad de veces que desea imprimir 'Hola mundo': "))
for i in range(cantidad):

print("Hola mundo")

Julia-Código:

println("Ingrese la cantidad de veces que desea imprimir 'Hola mundo': ")
cantidad = parse(Int, readline())

for i in 1:cantidad
println("Hola mundo")
end

Fortran-Código:

program hola_mundo
implicit none
integer :: cantidad, contador

write(*,*) "Ingrese la cantidad de veces que desea imprimir 'Hola mundo': "
read(*,*) cantidad

do contador = 1, cantidad
    write(*,*) "Hola mundo"
end do

end program hola_mundo

C++-Código:

#include <iostream.h>

int main()
{
int cantidad;
printf("Ingrese la cantidad de veces que desea imprimir 'Hola mundo': ");
scanf("%d", &cantidad);

int contador = 0;
while (contador < cantidad) {
    printf("Hola mundo\n");
    contador++;
}

return 0;

}

C-Código:

#include <stdio.h>

int main() {
int cantidad;
printf("Ingrese la cantidad de veces que desea imprimir 'Hola mundo': ");
scanf("%d", &cantidad);

int contador;
for (contador = 0; contador < cantidad; contador++) {
    printf("Hola mundo\n");
}

return 0;

}
