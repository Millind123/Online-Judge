import java.util.Scanner;
public class p1ans {
    public static void main(String args[] ){
        Scanner sc = new Scanner(System.in);
        int h = sc.nextInt();
        int max =10000000;
        for (int i =0;i<h ;i++){
            int n = sc.nextInt();
            if (n<max&&n%2==1)max=n;
        } 
        System.out.println(max);
    }
}
