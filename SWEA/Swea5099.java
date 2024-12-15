package ssafy.queue;

import java.util.Deque;
import java.util.LinkedList;
import java.util.Scanner;
import java.util.Arrays;

public class Swea5099 {

    public static Deque<int[]> oven;
    public static Deque<int[]> pizzas;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();
        for (int tc = 1; tc <= T; tc++) {
            int N = scanner.nextInt(); // 화덕 크기
            int M = scanner.nextInt(); // 피자 개수

            pizzas = new LinkedList<>(); // 피자 목록 생성 {치즈, 피자번호}
            for (int m = 1; m <= M; m++) {
                int pizza = scanner.nextInt();
                pizzas.offer(new int[]{pizza, m});
            }

            // 초기 화덕 상태 지정
            oven = new LinkedList<>();
            for (int n = 0; n < N; n++) {
                oven.offer(pizzas.poll());
            }

            // 결과 변수 미리 지정
            int[] result = new int[] {0, 0};

            // 오븐에 피자가 있는 동안 계속 반복
            while (!oven.isEmpty()) {
                int[] output = oven.poll();     // 오븐에 있는 피자 중 먼저 들어간 애를 뽑아서
                int tempPizza = output[0] / 2;  // 치즈 녹이고
                if (tempPizza != 0) {           // 치즈가 0이 아니라면
                    output[0] = tempPizza;
                    oven.offer(output);         // 다시 넣음
                } else {                        // 치즈가 0이라면
                    if (!pizzas.isEmpty()) {    // 만약 더 넣을 피자가 남아있다면 새 피자 넣음
                        oven.offer(pizzas.poll());
                    } else {
                        result = output;        // 만약 더 넣을 애가 없다면 걔가 마지막 피자
                    }
                }
            }
            System.out.println("#" + tc + " " + result[1]); // 피자 번호 출력
        }
        scanner.close();
    }
}
