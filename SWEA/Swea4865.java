package ssafy.string;

import java.util.Scanner;
import java.util.Arrays;

public class Swea4865 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();
        scanner.nextLine();
        for (byte tc = 1; tc <= T; tc++) {
            String target = scanner.nextLine();
            String pattern = scanner.nextLine();

            char[] targetArr = target.toCharArray();
            char[] patternArr = pattern.toCharArray();

            int result = 0;
            for (int ti = 0; ti < targetArr.length; ti++) {
                int tempCnt = 0;
                for (int pi = 0; pi < patternArr.length; pi++) {
                    if (patternArr[pi] == targetArr[ti]) {
                        tempCnt += 1;
                    }
                }
                if (result < tempCnt) {
                    result = tempCnt;
                }
            }
            System.out.println("#" + tc + " " + result);
        }
    }
}
