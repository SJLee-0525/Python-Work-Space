package ssafy.array;

import java.util.Scanner;
import java.util.Arrays;

public class SweaFrequentNum {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();
        scanner.nextLine();
        for (int t = 0; t < T; t++) {
            int tc = scanner.nextInt();
            scanner.nextLine();

            int[] scoreArr = new int[101];
            for (int i = 0; i < 1000; i++) {
                scoreArr[scanner.nextInt()]++;
            }
            // System.out.println(Arrays.toString(scoreArr));

            int maxScore = -1;
            int maxStudent = -1;
            for (int i = 0; i <= 100; i++) {
                if (maxStudent <= scoreArr[i]) {
                    maxStudent = scoreArr[i];
                    maxScore = i;
                }
            }
            System.out.println("#" + tc + " " + maxScore);
        }
    }
}
