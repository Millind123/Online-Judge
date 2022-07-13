import java.util.Scanner;
public class p2ans {
    public static void main(String args[] ){
        Scanner sc = new Scanner(System.in);
        int h = sc.nextInt();
        int max =0 ;
        for (int i =0;i<h ;i++){
            int n = sc.nextInt();
            if (n>max)max=n;
        } 
        System.out.println(max);
    }
}
