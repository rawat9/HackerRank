import java.io.*;
import java.util.*;
import java.math.BigInteger;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        BigInteger a = new BigInteger(scan.next());
        BigInteger b = new BigInteger(scan.next());
        
        BigInteger addition = a.add(b);
        BigInteger multiply = a.multiply(b);
        
        System.out.println(addition);
        System.out.println(multiply);
    }   
}
