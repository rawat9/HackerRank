import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int t = scan.nextInt();
        for (int j = 0; j < t; j++) {
            int a = scan.nextInt();
            int b = scan.nextInt();
            int n = scan.nextInt();

            for (int i = 0; i < n; i++) {
                a += (int) (Math.pow(2, i) * b);
                System.out.printf("%s ", a);
            }
            System.out.println();
        }
        scan.close();
    }
}
