package ssafy.array;

import java.util.Scanner;

public class SweaMagnetic {

    public static int[][] table;

    // 1: N / 2: S
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        for (int tc = 1; tc <= 10; tc++) {
            int N = scanner.nextInt();
            table = new int[N][N];

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    table[i][j] = scanner.nextInt();
                }
            }

            // 1: N / 2: S

            int cnt = 0;
            for (int i = 0; i < N; i++) {
                boolean status = false;
                for (int j = 0; j < N; j++) {
                    if (table[j][i] == 1) {
                        status = true;
                    } else if (status == true && table[j][i] == 2) {
                        cnt++;
                        status = false;
                    }
                }
            }
            System.out.println("#" + tc + " " + cnt);
        }
        scanner.close();
    }
}
