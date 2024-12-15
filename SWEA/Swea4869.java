package ssafy.stack;

import java.util.Scanner;

public class Swea4869 {

    static int[] memo = new int[31];

    static int myDef(int N) {
        if (N == 1) {
            return 1;
        } else if (N == 2) {
            return 3;
        }
        return memo[N] = myDef(N - 1) + (myDef(N - 2) * 2);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();
        for (int tc = 1; tc <= T; tc++) {
            int N = scanner.nextInt();
            N /= 10;

            int result = myDef(N);
            System.out.println("#" + tc + " " + result);
        }
        scanner.close();
    }
}
