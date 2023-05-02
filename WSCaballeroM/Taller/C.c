include <stdio.h>
int main() { int i = 1;

int x;

printf("Numero de veces que desea repetir Hola mundo: "); scanf("%d", &x);

while (i <= x) { printf("Hola mundo\n"); i++; }

return 0; }

