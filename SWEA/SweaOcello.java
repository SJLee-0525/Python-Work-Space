package ssafy.array;

import java.util.Scanner;
import java.util.Arrays;

public class SweaOcello {

    public static int N;
    public static int[][] board;

    public static int[] di = new int[] {1, 0, -1, 0, 1, 1, -1, -1};
    public static int[] dj = new int[] {0, 1, 0, -1, 1, -1, -1, 1};

    public static void initBoard() {
        for (int i = (N / 2) - 1; i <= N / 2; i++) {
            for (int j = (N / 2) - 1; j <= N / 2; j++) {
                if (i == j) {
                    board[i][j] = 2;
                } else {
                    board[i][j] = 1;
                }
            }
        }
    }

    public static void myTurn(int i, int j, int color) {
        board[i][j] = color;
        for (int k = 0; k < 8; k++) {
            boolean flag = false;
            int mi = i + di[k];
            int mj = j + dj[k];
            while (0 <= mi && mi < N &&
                    0 <= mj && mj < N &&
                    board[mi][mj] != color && board[mi][mj] != 0) {
                flag = true;
                mi += di[k];
                mj += dj[k];
                // System.out.println(mi + " " + mj);
            }
            if (flag == true &&
                    0 <= mi && mi < N &&
                    0 <= mj && mj < N &&
                    board[mi][mj] == color) {
                while (i != mi || j != mj) {
                    mi -= di[k];
                    mj -= dj[k];
                    board[mi][mj] = color;
                }
                // System.out.println(Arrays.deepToString(board));
            }
        }
    }

    public static int[] calResult() {
        int black = 0;
        int white = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (board[i][j] == 1) {
                    black++;
                } else if (board[i][j] == 2) {
                    white++;
                }
            }
        }
        return new int[]{black, white};
    }

    // 흑돌 1 / 백돌 2
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();
        for (int tc = 1; tc <= T; tc++) {
            N = scanner.nextInt(); // 보드 한 변 기링
            int M = scanner.nextInt(); // M개의 줄

            board = new int[N][N];
            initBoard();

            for (int m = 0; m < M; m++) {
                // 실제 index보다 1 높음
                // System.out.println(m + 1);
                int i = scanner.nextInt() - 1;
                int j = scanner.nextInt() - 1;
                int color = scanner.nextInt();

                myTurn(i, j, color);
            }
            // System.out.println(Arrays.deepToString(board));
            int[] result = calResult();
            System.out.println("#" + tc + " " + result[0] + " " + result[1]);
        }
        scanner.close();
    }
}

