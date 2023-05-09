#include <stdio.h>

int main() {
    int n;
    printf("Bienvenido. Ingrese el valor que desea visulizar 'Hola mundo' en su pantalla");
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        printf("Hola mundo");
    }
    return 0;
}
