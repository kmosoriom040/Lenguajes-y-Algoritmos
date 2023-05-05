En C++:

#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Dime el número de veces que quieres que se imprima 'himundo': ";
    cin >> n;
    for (int i = 1; i <= n; i++) {
        cout << "himundo" << endl;
    }
    return 0;
}

En Python:

a=input("Dime el número de veces que quieres que se imprima 'himundo'? ")
a=int(a)

for i in range(a):
  print("Himundo")

En Fortran: 

program himundo
  implicit none
  integer :: n, i

  write(*,*) 'Dime el número de veces que quieres que se imprima "himundo": '
  read(*,*) n

  do i = 1, n
    write(*,*) 'himundo'
  end do

end program himundo

En Java: 

import java.util.Scanner;

public class Himundo {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n;
        System.out.print("Dime el número de veces que quieres que se imprima 'himundo': ");
        n = scanner.nextInt();
        for (int i = 1; i <= n; i++) {
            System.out.println("himundo");
        }
    }
}

En Julia: 

println("Dime el número de veces que quieres que se imprima 'himundo': ")
n = parse(Int, readline())

for i in 1:n
    println("himundo")
end
