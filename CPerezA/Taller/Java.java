import java.util.Scanner;

public class Hola_mundo {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Ingrese la cantidad de veces que desea sea impresa la frase 'Hola mundo' ");
        int n = input.nextInt();
        for (int i = 0; i < n; i++) {
            System.out.print("Hola mundo ");
        }
    }
}
