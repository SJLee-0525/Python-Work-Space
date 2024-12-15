package ssafy.array;

import java.util.Scanner;

public class SweaWhereWordCan {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();
        for (int tc = 1; tc <= T; tc++) {
            int N = scanner.nextInt(); // 퍼즐 크기
            int K = scanner.nextInt(); // 단어 길이

            int[][] puzzle = new int[N][N];
            for (byte i = 0; i < N; i++) {
                for (byte j = 0; j < N; j++) {
                    puzzle[i][j] = scanner.nextInt();
                }
            }

            int resultCnt = 0;

            for (byte i = 0; i < N; i++) {
                int garoCheck = 0;
                int seroCheck = 0;
                for (byte j = 0; j < N; j++) {
                    if (puzzle[i][j] == 1) {
                        garoCheck++;
                        if (j == N - 1 && garoCheck == K) {
                            ++resultCnt;
                        }
                    } else {
                        if (garoCheck == K) {
                            ++resultCnt;
                        }
                        garoCheck = 0;
                    }

                    if (puzzle[j][i] == 1) {
                        seroCheck++;
                        if (j == N - 1 && seroCheck == K) {
                            ++resultCnt;
                        }
                    } else {
                        if (seroCheck == K) {
                            ++resultCnt;
                        }
                        seroCheck = 0;
                    }
                }
            }
            System.out.println("#" + tc + " " + resultCnt);
        }
    }
}
