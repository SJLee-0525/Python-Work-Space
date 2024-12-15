package ssafy.queue;

import java.util.Scanner;
import java.util.Deque;
import java.util.LinkedList;
import java.util.Arrays;

public class Swea5097 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();
        for (int tc = 1; tc <= T; tc++) {
            int N = scanner.nextInt(); // 수열 크기
            int M = scanner.nextInt(); // 반복 횟수

            Deque<Integer> queue = new LinkedList<>();
            for (int n = 0; n < N; n++) {
                queue.offer(scanner.nextInt());
            }

            for (int m = 0; m < M; m++) {
                queue.offer(queue.poll());
            }
            System.out.println("#" + tc + " " + queue.getFirst());
        }
        scanner.close();
    }
}
