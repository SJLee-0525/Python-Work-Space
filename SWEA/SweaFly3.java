package ssafy.array;

import java.util.Scanner;
import java.util.Arrays;

public class SweaFly3 {

    public static int[][] flies;

    public static int[] di = {1, 0, -1, 0};
    public static int[] dj = {0, 1, 0, -1};

    public static int[] xi = {1, 1, -1, -1};
    public static int[] xj = {1, -1, -1, 1};

    public static int plusKill(int i, int j, int N, int M, int temp) {
        for (int k = 0; k < 4; k++) {
            for (int r = 1; r < M; r++) {
                int mi = i + di[k] * r;
                int mj = j + dj[k] * r;
                if (0 <= mi && mi < N &&
                        0 <= mj && mj < N) {
                    temp += flies[mi][mj];
                }
            }
        }
        return temp;
    }

    public static int crossKill(int i, int j, int N, int M, int temp) {
        for (int k = 0; k < 4; k++) {
            for (int r = 1; r < M; r++) {
                int mi = i + xi[k] * r;
                int mj = j + xj[k] * r;
                if (0 <= mi && mi < N &&
                        0 <= mj && mj < N) {
                    temp += flies[mi][mj];
                }
            }
        }
        return temp;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();
        for (int tc = 1; tc <= T; tc++) {
            int N = scanner.nextInt(); // 배열 크기
            int M = scanner.nextInt(); // 분사 범위

            flies = new int[N][N];
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    flies[i][j] = scanner.nextInt();
                }
            }

            int result = 0;
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    int plusRst = plusKill(i, j, N, M, flies[i][j]);
                    int crossRst = crossKill(i, j, N, M, flies[i][j]);
                    int temp = 0;
                    if (plusRst < crossRst) {
                        temp = crossRst;
                    } else {
                        temp = plusRst;
                    }
                    if (result < temp) {
                        result = temp;
                    }
                }
            }
            System.out.println("#" + tc + " " + result);
        }
        scanner.close();
    }
}