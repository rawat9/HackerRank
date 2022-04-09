import java.io.*;
import java.util.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        List<List<Integer>> arr = new ArrayList<>();

        IntStream.range(0, 6).forEach(i -> {
            try {
                arr.add(
                        Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                                .map(Integer::parseInt)
                                .collect(toList()));
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        System.out.println(getMax(arr));
        bufferedReader.close();
    }

    public static int getMax(List<List<Integer>> array) {
        int maxSum = Integer.MIN_VALUE; 
        int currSum = 0;

        for (int i = 1; i < 5; i++) {
            for (int j = 1; j < 5; j++) {
                int top = (array.get(i-1).get(j-1) + array.get(i-1).get(j) + array.get(i-1).get(j+1));
                int bottom = (array.get(i+1).get(j-1) + array.get(i+1).get(j) + array.get(i+1).get(j+1));
                currSum = (top + bottom + array.get(i).get(j));
                maxSum = Math.max(currSum, maxSum);
            }
        }
        return maxSum;
    }
}
