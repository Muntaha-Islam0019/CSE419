import java.util.Scanner ;

public class Task06 {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in) ;
        
        for (int count = 1 ; count>= 0 ; count++) {

            String s = sc.nextLine();

            if (s.equals("HELLO")) {
                System.out.printf("Case %d: ENGLISH\n",count);
            } else if (s.equals("HOLA")) {
                System.out.printf("Case %d: SPANISH\n",count);
            } else if (s.equals("HALLO")) {
                System.out.printf("Case %d: GERMAN\n",count);
            } else if (s.equals("BONJOUR")) {
                System.out.printf("Case %d: FRENCH\n",count);
            } else if (s.equals("CIAO")) {
                System.out.printf("Case %d: ITALIAN\n",count);
            } else if (s.equals("ZDRAVSTVUJTE")) {
                System.out.printf("Case %d: RUSSIAN\n",count);
            } else if (s.equals("#")){
                break;
            } else {
                System.out.printf("Case %d: UNKNOWN\n",count) ;
            }
        }

        sc.close();
    }
}
