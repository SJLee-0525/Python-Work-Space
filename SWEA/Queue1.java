package ssafy.queue;

import java.util.Arrays;
import java.util.Scanner;

public class Queue1 {

    // 배열 사이즈가 10이면 10번 삽입할 수 있음 (큐의 크기가 10이 아님)
    static String[] queue = new String[10];
    static int front = -1;
    static int rear = -1;

    // 공백상태 확인
    static boolean isEmpty() {
        return front == rear;
    }

    // 포화상태 확인
    static boolean isFull() {
        // rear가 배열의 마지막 index를 가리키면 포화 상태
        return rear == (queue.length - 1);
    }

    // 삽입
    static void enQueue(String item) {
        if (isFull()) {
            System.out.println("Queue가 가득 찼습니다.");
            return;
        }
        queue[++rear] = item;
        System.out.print("삽입 성공 ");
        System.out.println(Arrays.toString(queue));
    }

    // 삭제
    static String deQueue() {
        if (isEmpty()) {
            System.out.println("Queue가 비어있습니다.");
            return null;
        }
        System.out.println(Arrays.toString(queue));
        return queue[++front];
    }

    // 조회
    static String qPeek() {
        return queue[front + 1]; // 일시적으로 front를 1 늘려서 확인
    }

    // 큐에 들어있는 데이터 개수 조회
    static int qSize() {
        return rear - front;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 원소 넣기
        while (true) {
            String item = scanner.nextLine();
            if (item.equals("0")) {
                break;
            }
            enQueue(item);
        }

        // 원소 뽑기
        while (!isEmpty()) {
            System.out.println(deQueue());
        }
    }


}
