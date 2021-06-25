import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String str = scan.next();

        int start = scan.nextInt();
        int end = scan.nextInt();
        
        String substring = str.substring(start, end);
        
        System.out.println(substring);
        scan.close();
    }
}
