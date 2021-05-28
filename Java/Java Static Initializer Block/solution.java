import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int breadth = scan.nextInt();
        int height = scan.nextInt();

        if (breadth >= 1 && height >= 1)
            System.out.println(breadth * height);
        else {
            System.out.println("java.lang.Exception: Breadth and height must be positive\n" + "");
        }
        scan.close();
    }
}
