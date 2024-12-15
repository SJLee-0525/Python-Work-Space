package ssafy.array;

import java.util.Scanner;
import java.util.Arrays;

public class Swea4843 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();
        for (byte tc = 1; tc <= T; tc++) {
            int N = scanner.nextInt();
            int maxValue = 0;
            int[] inputArr = new int[N];
            for (byte i = 0; i < N; i++) {
                inputArr[i] = scanner.nextInt();
                if (maxValue < inputArr[i]) {
                    maxValue = inputArr[i];
                }
            }
            // 값을 인덱스로 카운팅
            int[] counting = new int[maxValue + 1];
            for (int inputNum : inputArr) {
                counting[inputNum] += 1;
            }
            // System.out.println(Arrays.toString(counting)); // [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

            // 누적합
            for (byte i = 1; i < counting.length; i++) {
                counting[i] = counting[i] + counting[i - 1];
            }
            // System.out.println(Arrays.toString(counting)); // [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

            // 카운팅 정렬
            int[] sortedArr = new int[N];
            for (int i = N - 1; i >= 0; i--) {
                counting[inputArr[i]] -= 1;
                sortedArr[counting[inputArr[i]]] = inputArr[i];
            }
            // System.out.println(Arrays.toString(sortedArr));

            // 선택 정렬
            int[] resultArr = new int[10];
            for (int i = 0; i < 5; i++) {
                resultArr[i * 2] = sortedArr[N - 1 - i];
                resultArr[(i * 2) + 1] = sortedArr[i];
            }
            // System.out.println(Arrays.toString(resultArr)); // [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]

            System.out.print("#" + tc);
            for (int result : resultArr) {
                System.out.print(" " + result);
            }
            System.out.println();
        }
    }
}