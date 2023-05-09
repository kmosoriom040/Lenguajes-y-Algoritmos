import java.util.Scanner;

public class HolaMundo {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Ingrese una variable: ");
        int n = input.nextInt();
        for (int i = 0; i < n; i++) {
            System.out.print("hola mundo ");
        }
    }
}
