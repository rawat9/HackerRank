import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String A = scan.next();
        String B = scan.next();

        // Sum of lengths
        System.out.println(A.length() + B.length());

        // Lexicographically sorted?
        if (A.compareTo(B) > 0) {
            System.out.println("Yes");
        } else
            System.out.println("No");
        
        // Capitalise first letters of both words
        String first = A.substring(0, 1).toUpperCase() + A.substring(1, A.length()) + " ";
        String second = B.substring(0, 1).toUpperCase() + B.substring(1, B.length());
        
        System.out.println(first + second);         
        
        scan.close();
    }
}
