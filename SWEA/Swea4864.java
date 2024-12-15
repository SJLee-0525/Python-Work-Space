package ssafy.string;

import java.util.Scanner;

public class Swea4864 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();
        scanner.nextLine();
        for (byte tc = 1; tc <= T; tc++) {
            String target = scanner.nextLine();
            String pattern = scanner.nextLine();

            int result = bruteForce(target, pattern);

            System.out.println("#" + tc + " " + result);
        }
    }

    public static int bruteForce(String target, String pattern) {
        char[] targetArr = target.toCharArray();
        char[] patternArr = pattern.toCharArray();

        int ti = 0;
        int pi = 0;
        while (ti < target.length() && pi < pattern.length()) {
            if (targetArr[ti] != patternArr[pi]) {
                pi -= ti;
                ti = -1;
            }
            ti += 1;
            pi += 1;
        }
        if (ti == targetArr.length) {
            return 1;
        } else {
            return 0;
        }
    }
}
