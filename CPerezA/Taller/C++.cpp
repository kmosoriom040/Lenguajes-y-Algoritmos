#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Ingrese la cantidad de veces que desea sea impresa la frase 'Hola mundo' ";
    cin >> n;
    for (int i = 0; i < n; i++) {
        cout << "Hola mundo ";
    }
    return 0;
}
