package ssafy.array;

import java.util.Scanner;
import java.util.Arrays;

public class SweaBabyGin {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();
        scanner.nextLine();

        for (int tc = 1; tc <= T; tc++) {
            // java에서 연속된 숫자를 나누어서 배열에 저장하기
            int[] arr = new int[6];             // 배열 생성
            String input = scanner.nextLine();  // String으로 일단 입력 받음

            for (int i = 0; i < input.length(); i++) {
                // 순회하며 각 문자를 숫자로 변환해서 배열에 담음..
                arr[i] = Character.getNumericValue(input.charAt(i));
            }
//            System.out.println("arr: " + Arrays.toString(arr)); // arr: [3, 3, 3, 4, 5, 6]

            boolean result = checkBabyGin(arr);
            if (result == true) {
                System.out.println("#" + tc + " Baby Gin");
            } else {
                System.out.println("#" + tc + " Lose");
            }
        }
    }

    public static boolean checkBabyGin(int[] inputArr) {
        int[] countingArr = new int[10];
        for (int inputNum : inputArr) {
            countingArr[inputNum] += 1;
        }
        // System.out.println("countingArr: " + Arrays.toString(countingArr));
        // countingArr: [0, 0, 0, 3, 1, 1, 1, 0, 0, 0]

        // 같은 3장의 카드 제거
        for (int i = 0; i < 10; i++) {
            while (countingArr[i] >= 3) {
                countingArr[i] -= 3;
            }
        }

        // 연속된 카드 제거
        for (int i = 0; i <= 7; i++) {
            while (countingArr[i] >= 1 && countingArr[i + 1] >= 1 && countingArr[i + 2] >= 1) {
                countingArr[i] -= 1;
                countingArr[i + 1] -= 1;
                countingArr[i + 2] -= 1;
            }
        }

        // 베이비 진 여부 판별
        for (int c = 0; c < 10; c++) {
            if (countingArr[c] >= 1) {
                return false; // 카드가 남아있다면 false 반환
            }
        }
        return true;          // 문제 없으면 true 반환
    }
}
