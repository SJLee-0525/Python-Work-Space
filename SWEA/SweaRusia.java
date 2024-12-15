package ssafy.array;

import java.util.Scanner;
import java.util.Arrays;

public class SweaRusia {

    public static char[][] flag;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();
        for (int tc = 1; tc <= T; tc++) {
            int N = scanner.nextInt(); // N개의 줄
            int M = scanner.nextInt(); // M개의 문자
            scanner.nextLine();

            flag = new char[N][M];

            for (int i = 0; i < N; i++) {
                String inputStr = scanner.nextLine();
                for (int j = 0; j < M; j++) {
                    flag[i][j] = inputStr.charAt(j);
                }
            }
            // System.out.println(Arrays.deepToString(flag));

            int result = 1000001;
            int cnt1 = 0;
            for (int std1 = 0; std1 < N - 2; std1++) {
                for (int i = 0; i < M; i++) {
                    if (flag[std1][i] != 'W') {
                        cnt1++;
                    }
                }
                int cnt2 = 0;
                for (int std2 = std1 + 1; std2 < N - 1; std2++) {
                    for (int i = 0; i < M; i++) {
                        if (flag[std2][i] != 'B') {
                            cnt2++;
                        }
                    }
                    int cnt3 = 0;
                    for (int std3 = std2 + 1; std3 < N; std3++) {
                        for (int i = 0; i < M; i++) {
                            if (flag[std3][i] != 'R') {
                                cnt3++;
                            }
                        }
                    }
                    int temp = cnt1 + cnt2 + cnt3;
                    if (result > temp) {
                        result = temp;
                    }
                }
            }
            System.out.println("#" + tc + " " + result);
        }
        scanner.close();
    }
}
