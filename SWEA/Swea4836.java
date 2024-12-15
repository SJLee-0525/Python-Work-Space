package ssafy.arraydim;

import java.util.Scanner;
import java.util.Arrays;

public class Swea4836 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();
        for (byte tc = 1; tc <= T; tc++) {
            int[][] board = new int[10][10];

            int N = scanner.nextInt();      // N번 만큼 색칠하기
            for (int n = 0; n < N; n++) {
                int[] colors = new int[5];  // [r1, c1, r2, c2, color] 색칠 정보 담음
                for (int c = 0; c < 5; c++) {
                    colors[c] = scanner.nextInt();
                }

                // 받은 색칠 정보로 색칠하기
                for (int i = colors[0]; i <= colors[2]; i++) {
                    for (int j = colors[1]; j <= colors[3]; j++) {
                        board[i][j] += colors[4];
                    }
                }
            }

            // 보라색 찾기
            byte cnt = 0;
            for (int i = 0; i < 10; i++) {
                for (int j = 0; j < 10; j++) {
                    if (board[i][j] == 3) {
                        cnt += 1;
                    }
                }
            }
            System.out.println("#" + tc + " " + cnt);
        }
    }
}