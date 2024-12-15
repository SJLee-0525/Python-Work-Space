package ssafy.array;

import java.util.Scanner;
import java.util.Arrays;

public class SweaAncientTemple {

    public static int N;
    public static int M;

    public static int[] di = new int[] {1, 0, -1, 0};
    public static int[] dj = new int[] {0, 1, 0, -1};

    public static int[][] picture;

    public static int detectTemple(int i, int j) {
        int cnt = 0;
        for (int k = 0; k < 4; k++) {
            int temp = 1;
            int mi = i + di[k];
            int mj = j + dj[k];
            while (0 <= mi && mi < N &&
                    0 <= mj && mj < M &&
                    picture[mi][mj] == 1) {
                temp++;
                mi += di[k];
                mj += dj[k];
            }
            if (cnt < temp) {
                cnt = temp;
            }
        }
        if (cnt > 1) {
            return cnt;
        }
        return 0;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();
        for (int tc = 1; tc <= T; tc++) {
            N = scanner.nextInt();
            M = scanner.nextInt();

            picture = new int[N][M];

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    picture[i][j] = scanner.nextInt();
                }
            }

            int result = 0;
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    if (picture[i][j] == 1) {
                        int temp = detectTemple(i, j);
                        if (result < temp) {
                            result = temp;
                        }
                    }
                }
            }
            System.out.println("#" + tc + " " + result);
        }
        scanner.close();
    }
}

