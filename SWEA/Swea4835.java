package ssafy.array;

import java.util.Arrays;
import java.util.Scanner;

public class Swea4835 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();
        for (int tc = 1; tc <= T; tc++) {
            int N = scanner.nextInt();  // 정수 개수
            int M = scanner.nextInt();  // 구간 개수
            int[] arr = new int[N];
            for (int i = 0; i < N; i++) {
                arr[i] = scanner.nextInt();
            }
//            System.out.println(Arrays.toString(arr));

            int maxVal = 0;
            int minVal = 10000001;
            for (int i = 0; i <= N - M; i++) {
                int temp = 0;
                for (int j = i; j < i + M; j++) {
                    temp += arr[j];
                }
                if (maxVal < temp) {
                    maxVal = temp;
                }
                if (minVal > temp) {
                    minVal = temp;
                }
            }
            int result = maxVal - minVal;
            System.out.println("#" + tc + " " + result);
        }
    }
}