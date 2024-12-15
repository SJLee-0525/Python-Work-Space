package ssafy.string;

import java.util.Scanner;
import java.util.Arrays;

public class Swea4831 {

    public static String palindrom(char[][] Arr, int N, int M) {
        for (byte t = 0; t < 2; t++) {
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N - M + 1; j++) {
                    int left = j;
                    int right = j + M - 1;
                    while (Arr[i][left] == Arr[i][right]) {
                        left++;
                        right--;
                        if (left >= right) {
                            String result = "";
                            for (int resultJ = j; resultJ < j + M; resultJ++) {
                                result += Arr[i][resultJ];
                            }
                            return result;
                        }
                    }
                }
            }
            // 전치
            Arr = transPosition(Arr, N);
        }
        return null;
    }

    public static char[][] transPosition(char[][] Arr, int N) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (i < j) {
                    char temp = Arr[i][j];
                    Arr[i][j] = Arr[j][i];
                    Arr[j][i] = temp;
                }
            }
        }
        return Arr;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();
        for (int tc = 1; tc <= T; tc++) {
            int N = scanner.nextInt();
            int M = scanner.nextInt();
            scanner.nextLine();

            char[][] Arr = new char[N][N];
            for (int i = 0; i < N; i++) {
                String inputStr = scanner.nextLine();
                for (int j = 0; j < N; j++) {
                    Arr[i][j] = inputStr.charAt(j);
                }
            }
            // System.out.println(Arrays.deepToString(Arr));

            String result = palindrom(Arr, N, M);
            System.out.println("#" + tc + " " + result);
        }
        scanner.close();
    }
}
