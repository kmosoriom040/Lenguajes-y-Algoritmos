import java.util.Scanner;

public class Holas_Mundo {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Escriba el numero de 'Hola Mundo!' que desee ver en pantalla en forma de valor numerico: ");
        int n = input.nextInt();
        for (int i = 0; i < n; i++) {
            System.out.print("Hola mundo ");
        }
    }
}
