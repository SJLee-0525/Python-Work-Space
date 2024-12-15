package ssafy.array;

import java.util.Scanner;

public class SweaOmok {

    public static char[][] board;

    public static int[] di = new int[] {1, 0, -1, 0, 1, 1, -1, -1};
    public static int[] dj = new int[] {0, 1, 0, -1, 1, -1, -1, 1};

    public static boolean check(int i, int j, int N) {
        for (int k = 0; k < 8; k++) {
            int cnt = 1;
            int mi = i + di[k];
            int mj = j + dj[k];
            while (0 <= mi && mi < N &&
                    0 <= mj && mj < N &&
                    board[mi][mj] == 'o') {
                cnt++;
                if (cnt >= 5) {
                    return true;
                }
                mi += di[k];
                mj += dj[k];
            }
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();
        for (int tc = 1; tc <= T; tc++) {
            int N = scanner.nextInt();
            scanner.nextLine();

            board = new char[N][N];
            for (int i = 0; i < N; i++) {
                String inputStr = scanner.nextLine();
                for (int j = 0; j < N; j++) {
                    char elem = inputStr.charAt(j);
                    board[i][j] = elem;
                }
            }

            boolean result = false;
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (board[i][j] == 'o') {
                        boolean temp = check(i, j, N);
                        if (temp == true) {
                            result = temp;
                            break;
                        }
                    }
                }
            }
            if (result) {
                System.out.println("#" + tc + " YES");
            } else {
                System.out.println("#" + tc + " NO");
            }

        }
        scanner.close();
    }
}