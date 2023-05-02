#include <stdio.h>

int main() {
    int n;
    printf("Ingrese la cantidad de veces que desea sea impresa la frase 'Hola mundo'");
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        printf("Hola mundo");
    }
    return 0;
}
