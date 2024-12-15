package ssafy.stack;

import java.util.Scanner;
import java.util.Arrays;

public class SweaPascal {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();
        for (byte tc = 1; tc <= T; tc++) {
            int N = scanner.nextInt();

            int[][] pascalArr = new int[N][];
            for (int i = 0; i < N; i++) {
                pascalArr[i] = new int[i + 1];
            }

            pascalArr[0][0] = 1;
            for (int i = 1; i < N; i++) {
                for (int j = 0; j < pascalArr[i].length; j++) {
                    if (j - 1 >= 0) {
                        pascalArr[i][j] += pascalArr[i - 1][j - 1];
                    }
                    if (j < i) {
                        pascalArr[i][j] += pascalArr[i - 1][j];
                    }
                }
            }
            //System.out.println(Arrays.deepToString(pascalArr));

            System.out.println("#" + tc);
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < pascalArr[i].length; j++) {
                    System.out.print(pascalArr[i][j] + " ");
                }
                System.out.println();
            }
        }
        scanner.close();
    }
}
