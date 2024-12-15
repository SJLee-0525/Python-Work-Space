package ssafy.array;

import java.util.Scanner;

public class Swea4828 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();
        for (int tc = 1; tc <= T; tc++) {
            int N = scanner.nextInt();
            int[] arr = new int[N];

            for (int n = 0; n < N; n++) {
                arr[n] = scanner.nextInt();
            }

            int maxVal = arr[0];
            int minVal = arr[0];
            for (int index = 1; index < N; index++) {
                if (maxVal < arr[index]) {
                    maxVal = arr[index];
                }
                if (minVal > arr[index]) {
                    minVal = arr[index];
                }
            }
            int result = maxVal - minVal;
            System.out.println("#" + tc + " " + result);
        }
    }
}