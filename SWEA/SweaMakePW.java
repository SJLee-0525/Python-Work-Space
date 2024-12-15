package ssafy.queue;

import java.util.Scanner;
import java.util.Deque;
import java.util.LinkedList;

public class SweaMakePW {

    static Deque<Integer> queue;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        for (int t = 0; t < 10; t++) {
            int tc = scanner.nextInt();
            queue = new LinkedList<>();
            for (int i = 0; i < 8; i++) {
                queue.offer(scanner.nextInt());
            }

            while (queue.peekLast() > 0) {
                for (int i = 1; i <= 5; i++) {
                    if (queue.peekLast() == 0) {
                        break;
                    }
                    int temp = queue.poll();
                    temp -= i;
                    if (temp < 0) {
                        temp = 0;
                    }
                    queue.offer(temp);
                }
            }
            System.out.print("#" + tc);
            for (int a = 0; a < 8; a++) {
                System.out.print(" " + queue.pop());
            }
            System.out.println();
        }
        scanner.close();
    }
}
