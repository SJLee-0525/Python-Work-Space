package ssafy.arraydim;

import java.util.Scanner;
import java.util.Arrays;

public class SweaBalloon {

    // 델타
    public static int[] di = {1, 0, -1, 0};
    public static int[] dj = {0, 1, 0, -1};

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();
        for (byte tc = 1; tc <= T; tc++) {
            int N = scanner.nextInt(); // 세로 크기
            int M = scanner.nextInt(); // 가로 크기
            scanner.nextLine();

            // 배열에 종이 꽃가루 정보 받기
            int[][] arr = new int[N][M];
            for (byte i = 0; i < N; i++) {
                for (byte j = 0; j < M; j++) {
                    arr[i][j] = scanner.nextInt();
                }
                scanner.nextLine();
            }

            // 배열을 순회하며 델타 탐색 후 결과 할당
            int result = 0;
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    int temp = arr[i][j];
                    for (byte k = 0; k < 4; k++) {
                        int mi = i + di[k];
                        int mj = j + dj[k];
                        if (0 <= mi && mi < N && 0 <= mj && mj < M) {
                            temp += arr[mi][mj];
                        }
                    }
                    if (result < temp) {
                        result = temp;
                    }
                }
            }
            System.out.println("#" + tc + " " + result);
        }
    }
}