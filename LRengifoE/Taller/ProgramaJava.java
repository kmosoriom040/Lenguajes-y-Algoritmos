import java.util.Scanner;

public class Hola_mundo {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Bienvenido.Ingrese un valor para visualizar 'Hola mundo' en pantalla ");
        int n = input.nextInt();
        for (int i = 0; i < n; i++) {
            System.out.print("Hola mundo ");
        }
    }
}
