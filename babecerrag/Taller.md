brayan andres becerra

Python:
a = input("Ingrese la cantidad de veces que desea imprimir el mensaje Hola Mundo:")
a = int(a)

for i in range(a):
    print("Hola Mundo")

Fortran:

program hola_mundo
  implicit none
  integer :: n, i

  write(*,*) 'Ingresa el número de veces que deseas imprimir "hola mundo": '
  read(*,*) n

  do i = 1, n
    write(*,*) 'hola mundo'
  end do

end program hola_mundo


Java: 

import java.util.Scanner;

public class HolaMundo {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n;
        System.out.print("Ingresa el número de veces que deseas imprimir 'hola mundo': ");
        n = scanner.nextInt();
        for (int i = 1; i <= n; i++) {
            System.out.println("hola mundo");
        }
    }
}


Julia: 

println("Ingresa el número de veces que quieres imprimir 'hola mundo': ")
n = parse(Int, readline())

for i in 1:n
    println("hola mundo")
end