package ssafy.arraydim;

import java.util.Scanner;

public class SweaSum {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        for (byte t = 0; t < 10; t++) {
            int tc = scanner.nextInt();
            int[][] arr = new int[100][100];

            // 배열 입력받기
            for (byte i = 0; i < 100; i++) {
                for (byte j = 0; j < 100; j++) {
                    arr[i][j] = scanner.nextInt();
                }
                scanner.nextLine();
            }
            int result = 0;
            int cross1 = 0;
            int cross2 = 0;
            for (byte i = 0; i < 100; i++) {
                int garo = 0;
                int sero = 0;
                for (byte j = 0; j < 100; j++) {
                    garo += arr[i][j];
                    sero += arr[j][i];
                    if (i == j) {
                        cross1 += arr[i][j];
                    }
                    if (i + j == 99) {
                        cross2 += arr[i][j];
                    }
                }
                if (result < garo) {
                    result = garo;
                }
                if (result < sero) {
                    result = sero;
                }
            }
            if (result < cross1) {
                result = cross1;
            }
            if (result < cross2) {
                result = cross2;
            }
            System.out.println("#" + tc + " " + result);
        }
    }
}