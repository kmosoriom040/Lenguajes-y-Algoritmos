#include <stdio.h>

int main() {
    int n;
    printf("Escriba el numero de 'Hola Mundo!' que desee ver en pantalla en forma de valor numerico: ");
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        printf("Hola mundo");
    }
    return 0;
}
