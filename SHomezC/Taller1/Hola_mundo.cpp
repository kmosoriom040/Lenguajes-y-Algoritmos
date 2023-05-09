#include <iostream>

using namespace std;

int main()
{
    int n, i;

    // Pedir al usuario la cantidad de veces que desea imprimir "Hola Mundo"
    cout << "Ingrese la cantidad de veces que desea imprimir 'Hola Mundo': ";
    cin >> n;

    // Utilizar un bucle for para imprimir "Hola Mundo" n veces
    for(i=0; i<n; i++)
    {
        cout << "Hola Mundo\n";
    }

    return 0;
}
