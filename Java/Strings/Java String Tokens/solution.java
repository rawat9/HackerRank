import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String s = scanner.nextLine().trim();
        String delimiters = "[!.,?_'@\\s]+";
        String[] tokens = s.split(delimiters);
        
        if (s.length() > 0) {
            System.out.println(tokens.length);
            for (String token : tokens) {
                System.out.println(token);
            }
        } else {
            System.out.println(0);
        }
        scanner.close();

    }
}
