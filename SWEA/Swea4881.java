package ssafy.stack;

import java.util.Scanner;

public class Swea4881 {

    public static int[][] arr;
    public static int[] permArr;
    public static int result;

    public static void perm(int lv, int N) {
        if (lv == N) {
            calArr(N);
            return;
        }
        int i = lv;
        for (int j = lv; j < N; j++)  {
            int temp = permArr[i];
            permArr[i] = permArr[j];
            permArr[j] = temp;
            perm(lv + 1, N);
            permArr[j] = permArr[i];
            permArr[i] = temp;
        }
    }

    public static void calArr(int N) {
        int temp = 0;
        for (int i = 0; i < N; i++) {
            temp += arr[i][permArr[i]];
        }
        // System.out.println(temp);
        if (result > temp) {
            result = temp;
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();
        for (int tc = 1; tc <= T; tc++) {
            int N = scanner.nextInt();

            arr = new int[N][N];
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    arr[i][j] = scanner.nextInt();
                }
            }
            result = 11111111;
            permArr = new int[N];
            for (int b = 0; b < N; b++) {
                permArr[b] = b;
            }

            perm(0, N);

            System.out.println("#" + tc + " " + result);
        }
        scanner.close();
    }
}
