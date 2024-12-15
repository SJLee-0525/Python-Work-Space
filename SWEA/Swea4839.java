package ssafy.array;

import java.util.Scanner;
import java.util.Arrays;

public class Swea4839 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();

        for (int tc = 1; tc <= T; tc++) {
            int P = scanner.nextInt();
            int A = scanner.nextInt();
            int B = scanner.nextInt();

            int resultA = binarySearch(P, A);
            int resultB = binarySearch(P, B);

            // System.out.println("result" + resultA + " " + resultB);
            String result = "0";
            if (resultA < resultB) {
                result = "A";
            } else if (resultA > resultB){
                result = "B";
            }
            System.out.println("#" + tc + " " + result);
        }
    }

    public static int binarySearch(int Page, int tar) {
        int left = 1;
        int right = Page;

        int cnt = 0;
        while (left <= right) {
            int mid = (left + right) / 2;
            cnt++;
            // System.out.println(left + " " + right + " " + mid + " " + tar + " " + cnt);
            if (tar == mid) {
                return cnt;
            } else if (tar < mid) {
                right = mid;
            } else {
                left = mid;
            }
        }
        return cnt;
    }
}