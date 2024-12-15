package ssafy.arraydim;

import java.util.Scanner;
import java.util.Arrays;

public class SweaLadder {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        for (byte t = 0; t < 10; t++) {
            int tc = scanner.nextInt();
            int[][] ladder = new int[100][100];

            for (byte i = 0; i < 100; i++) {
                for (byte j = 0; j < 100; j++) {
                    ladder[i][j] = scanner.nextInt();
                }
            }
            int result = 0;
            for (int j = 0; j < 100; j++) {
                if (ladder[99][j] == 2) {
                    result = clibing(99, j, ladder);
                }
            }
            System.out.println("#" + tc + " " + result);
        }
    }

    public static int clibing(int i, int j, int[][] ladder) {
        int ni = i;
        int nj = j;
        while (ni > 0) {
            while (nj + 1 < 100 && ladder[ni][nj + 1] == 1) {
                ladder[ni][nj] = 0;
                nj += 1;
            }
            while (nj - 1 >= 0 && ladder[ni][nj - 1] == 1) {
                ladder[ni][nj] = 0;
                nj -= 1;
            }
            if (ladder[ni - 1][nj] == 1) {
                ladder[ni][nj] = 0;
                ni -= 1;
            }
        }
        return nj;
    }
}
