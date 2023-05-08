#include <stdio.h>

int main() {
    int n;
    printf("Ingrese el número de veces que desea imprimir 'hola mundo': ");
    scanf("%d", &n);
    
    for(int i = 0; i < n; i++) {
        printf("hola mundo\n");
    }
    
    return 0;
}
