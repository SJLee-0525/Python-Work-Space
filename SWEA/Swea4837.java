package ssafy.stack;

import java.util.Arrays;
import java.util.ArrayList;
import java.util.Scanner;

public class Swea4837 {

    public static int[] arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12};
    public static int[] bool = new int[12];

    public static int resultCount;

    public static void combi(int sum, int cnt, int lv, int N, int K) {
        if (cnt == N && sum == K) {
            // System.out.println(Arrays.toString(bool));
            resultCount++;
            return;
        } else if (lv >= 12 || cnt > N || sum > K) {
            return;
        }
        bool[lv] = 1;
        combi(sum + arr[lv],cnt + 1, lv + 1, N, K);
        bool[lv] = 0;
        combi(sum, cnt, lv + 1, N, K);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();
        for (int tc = 1; tc <= T; tc++) {
            resultCount = 0;

            int N = scanner.nextInt();  // 원소의 수
            int K = scanner.nextInt();  // 부분 집합의 합

            combi(0,0,0, N, K);

            if (resultCount >= 1) {
                System.out.println("#" + tc + " " + resultCount);
            } else {
                System.out.println("#" + tc + " " + resultCount);
            }
        }
        scanner.close();
    }
}
