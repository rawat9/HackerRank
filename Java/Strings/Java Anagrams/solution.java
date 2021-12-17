import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String word1 = sortChar(scanner.next());
        String word2 = sortChar(scanner.next());

        String result = (word1.equals(word2)) ? "Anagrams" : "Not Anagrams";
        System.out.println(result);
        scanner.close();
    }

    public static String sortChar(String word) {
        char[] chars = word.toLowerCase().toCharArray();
        Arrays.sort(chars);
        return new String(chars);
    }

}
