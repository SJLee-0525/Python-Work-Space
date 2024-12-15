package ssafy.array;

import java.util.Scanner;
import java.util.Arrays;

public class SweaArrayAdd {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();
        for (int tc = 1; tc <= T; tc++) {
            int aLen = scanner.nextInt();
            int bLen = scanner.nextInt();
            scanner.nextLine();

            String[] A = scanner.nextLine().split(" ");
            String[] B = scanner.nextLine().split(" ");

            String[] result = new String[aLen + bLen];

            int minLen;
            int maxLen;
            if (aLen < bLen) {
                minLen = aLen;
                maxLen = bLen;
            } else {
                minLen = bLen;
                maxLen = aLen;
            }

            for (int r = 0; r < minLen; r++) {
                result[r * 2] = A[r];
                result[r * 2 + 1] = B[r];
            }
            if (aLen > bLen) {
                for (int r = 0; r < maxLen - minLen; r++) {
                    result[minLen * 2 + r] = A[minLen + r];
                }
            } else if (aLen < bLen){
                for (int r = 0; r < maxLen - minLen; r++) {
                    result[minLen * 2 + r] = B[minLen + r];
                }
            }
            System.out.print("#" + tc);
            for (String num : result) {
                System.out.print(" " + num);
            }
            System.out.println();
        }
        scanner.close();
    }
}
