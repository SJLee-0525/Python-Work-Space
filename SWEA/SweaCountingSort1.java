package ssafy.array;

import java.util.Scanner;

public class SweaCountingSort1 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();
        for (int tc = 1; tc <= T; tc++) {
            int N = scanner.nextInt();
            int[] inputArr = new int[N];
            int maxVal = 0;
            for (int i = 0; i < N; i++) {
                inputArr[i] = scanner.nextInt();
                if (maxVal < inputArr[i]) {
                    maxVal = inputArr[i];
                }
            }
            scanner.nextLine();

            // 인덱스에 카운팅
            int[] counting = new int[maxVal + 1];
            for (int i = 0; i < N; i++) {
                counting[inputArr[i]] += 1;
            }
            // System.out.println(Arrays.toString(counting)); // [1, 1, 0, 0, 1, 0, 0, 1, 1]

            // 누적합 구하기
            for (int i = 1; i < counting.length; i++) {
                counting[i] = counting[i] + counting[i - 1];
            }
            // System.out.println(Arrays.toString(counting)); // [1, 2, 2, 2, 3, 3, 3, 4, 5]

            // 카운팅 정렬
            int[] countingSortArr = new int[N];
            for (int i = N - 1; i >= 0; i--) {
                counting[inputArr[i]] -= 1;
                countingSortArr[counting[inputArr[i]]] = inputArr[i];
            }
            // System.out.println(Arrays.toString(countingSortArr)); // [0, 1, 4, 7, 8]

            // 출력
            System.out.print("#" + tc);
            for (int cnt : countingSortArr) {
                System.out.print(" " + cnt);
            }
            System.out.println();
        }
    }
}
