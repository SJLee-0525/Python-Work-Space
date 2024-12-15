package ssafy.arraydim;

import java.util.Scanner;
import java.util.Arrays;

public class SweaKillFly {

    public static void main(String[] args) {
        Scanner scanner= new Scanner(System.in);

        int T = scanner.nextInt();
        for (byte tc = 1; tc <= T; tc++) {
            int N = scanner.nextInt();  // 방 크기
            int M = scanner.nextInt();  // 파리채 크기
            scanner.nextLine();

            // 방 안의 파리 개수 2차원 배열에 담기
            int[][] room = new int[N][N];
            for (byte i = 0; i < N; i++) {
                for (byte j = 0; j < N; j++) {
                    room[i][j] = scanner.nextInt();
                }
                scanner.nextLine();
            }

            // System.out.println(Arrays.deepToString(room));
            // [[1, 3, 3, 6, 7], [8, 13, 9, 12, 8], [4, 16, 11, 12, 6], [2, 4, 1, 23, 2], [9, 13, 4, 7, 3]]

            int maxKill = 0;
            // 기준점 잡고
            for (int i = 0; i <= N - M; i++) {
                for (int j = 0; j <= N - M; j++) {

                    // 기준점에서 파리채 범위 만큼 순회하면서
                    int tempKill = 0;
                    for (int y = i; y < i + M; y++) {
                        for (int x = j; x < j + M; x++) {
                            tempKill += room[y][x];     // 잡은 개수 추가
                        }
                    }
                    // 최대값 비교
                    if (maxKill < tempKill) {
                        maxKill = tempKill;
                    }
                }
            }
            System.out.println("#" + tc + " " + maxKill);
        }
    }
}