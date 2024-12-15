package ssafy.array;

import java.util.Scanner;
import java.util.Arrays;

public class SweaFlatten {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        for (byte tc = 1; tc <= 10; tc++) {
            int targetCount = scanner.nextInt(); // 덤프 횟수
            int[] boxes = new int[100];
            for (byte i = 0; i < 100; i++) {
                boxes[i] = scanner.nextInt();
            }
            scanner.nextLine(); // 공백 빼주기...
//            System.out.println(Arrays.toString(boxes));

            int result = 0;
            for (short cnt = 1; cnt <= targetCount; cnt++) {
                byte minIndex = 0;
                byte maxIndex = 0;
                for (byte i = 0; i < 100; i++) {
                    if (boxes[minIndex] >= boxes[i]) {
                        minIndex = i;
                    } else if (boxes[maxIndex] < boxes[i]) {
                        maxIndex = i;
                    }
                }
                // 평탄화
                boxes[maxIndex] -= 1;
                boxes[minIndex] += 1;

                // 결과 확인
                int resultMin = 1001;
                int resultMax = -1;
                for (byte r = 0; r < 100; r++) {
                    if (resultMin > boxes[r]) {
                        resultMin = boxes[r];
                    } else if (resultMax < boxes[r]) {
                        resultMax = boxes[r];
                    }
                }
                // 만약 평탄화가 횟수 이내에 완료되면 즉시 종료
                if (resultMax - resultMin <= 1) {
                    result = resultMax - resultMin;
                    break;
                }
                // 결과 할당
                result = resultMax - resultMin;

//                System.out.println("#" + boxes[maxIndex] + " " + boxes[minIndex] + " " + result);
            }
            System.out.println("#" + tc + " " + result);
        }
    }
}
