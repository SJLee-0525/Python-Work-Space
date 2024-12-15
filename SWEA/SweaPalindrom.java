package ssafy.string;

import java.lang.reflect.Array;
import java.util.Scanner;
import java.util.Arrays;

public class SweaPalindrom {

    public static int palindrom(char[][] Arr, int N) {
        int cnt = 0;

        for (byte t = 0; t < 2; t++) {
            for (byte i = 0; i < 8; i++) {
                for (int j = 0; j <= 8 - N; j++) {
                    int left = j;
                    int right = j + N - 1;
                    while (Arr[i][left] == Arr[i][right]) {
                        // System.out.println(left + " / " + right);
                        left++;
                        right--;
                        if (left >= right) {
                            cnt++;
                            break;
                        }
                    }
                }
            }
            // 전치
            Arr = transPosition(Arr);
        }
        return cnt;
    }

    public static char[][] transPosition(char[][] Arr) {
        for (byte i = 0; i < 8; i++) {
            for (byte j = 0; j < 8; j++) {
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

        for (byte tc = 1; tc <= 10; tc++) {
            int N = scanner.nextInt();
            scanner.nextLine();

            char[][] Arr = new char[8][8];
            for (byte i = 0; i < 8; i++) {
                String input = scanner.nextLine();
                for (byte j = 0; j < 8; j++) {
                    Arr[i][j] = input.charAt(j);
                }
            }
            // System.out.println(Arrays.deepToString(Arr));

            int result = palindrom(Arr, N);
            System.out.println("#" + tc + " " + result);
        }
        scanner.close();
    }
}
