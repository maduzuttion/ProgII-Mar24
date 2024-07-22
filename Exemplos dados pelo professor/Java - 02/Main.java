//código 1:
//public class Main {
//        public static void main(String[] args) {
//        System.out.println("Testes");

//        System.out.println(args[0]);
 //       System.out.println(args[1]);
//    }
//}

//For:
public class Main{
    public static void main (String[] args) {
        System.out.println("Apenas Testes");

        for (String lista : args){
            System.out.println(lista);
        }

        for (int i=0; i<args.length; i++){
            System.out.println(args[i]);
        }
    }
}