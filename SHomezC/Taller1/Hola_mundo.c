#include <stdio.h>

int main()
{
    int n, i;

    // Pedir al usuario la cantidad de veces que desea imprimir "Hola Mundo"
    printf("Ingrese la cantidad de veces que desea imprimir 'Hola Mundo': ");
    scanf("%d", &n);

    // Utilizar un bucle for para imprimir "Hola Mundo" n veces
    for(i=0; i<n; i++)
    {
        printf("Hola Mundo\n");
    }

    return 0;
}