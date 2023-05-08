import java.util.Scanner;

public class HolaMundo {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingresa el número de veces que quieres imprimir 'Hola mundo': ");
        int n = scanner.nextInt();
        for (int i = 1; i <= n; i++) {
            System.out.println("Hola mundo");
        }
    }
}
