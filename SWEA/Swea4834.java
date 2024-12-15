package ssafy.array;

import java.util.Scanner;
import java.util.Arrays;

public class Swea4834 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();
        for (int tc = 1; tc <= T; tc++) {
            int N = scanner.nextInt();  // 카드 장수
            scanner.nextLine();         // 줄바꿈 빼는 용도

            // 카드 입력 받기
            String inputStr = scanner.nextLine();
            int[] arr = new int[N];
            for (int s = 0; s < N; s++) {
                arr[s] = Character.getNumericValue(inputStr.charAt(s));
            }
            // System.out.println(Arrays.toString(arr)); // [4, 9, 6, 7, 9]

            // 카드 정보를 인덱스로 카운트
            int[] countingArr = new int[10];
            for (int i = 0; i < N; i++) {
                countingArr[arr[i]] += 1;
            }

            int mostCards = 0;
            for (int c = 0; c < 10; c++) {
                if (countingArr[mostCards] <= countingArr[c]) {
                    mostCards = c;
                }
            }

            System.out.println("#" + tc + " " + mostCards + " " + countingArr[mostCards]);
        }
    }
}
