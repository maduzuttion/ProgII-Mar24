import java.util.Scanner;
clas Input {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Digite seu nome:");
        String inp = input.nextline();
        System.out.print("Informe sua idade: ");
        int idade = input.nextInt();
        
        System.out.printIn("Hello, " + inp + "sua idade é: " + idade)
    }
}