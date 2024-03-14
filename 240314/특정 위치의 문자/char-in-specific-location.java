import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner scanner = new Scanner(System.in);
        
        char[] word = new char[]{'L','E','B','R','O','S'};
        char a = scanner.next().charAt(0);

        int idx = -1;

        for(int i=0; i<6; i++){
            if(word[i]==a){
                idx = i;
            }
        }

        if(idx == -1){
            System.out.print("None");
        } else {
            System.out.print(idx);
        }
    }
}