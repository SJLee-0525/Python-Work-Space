package ssafy.queue;

import java.util.Queue;
import java.util.LinkedList;

public class Queue2 {

    public static void main(String[] args) {
        Queue<Integer> queue = new LinkedList<>();

        // 삽입
        queue.add(1);       // 원소를 추가할 수 없으면 예외 발생 (프로그램 중단)
        queue.offer(1);  // 추가에 성공하면 true, 실패하면 false 반환 (프로그램 유지)

        // 삭제
        queue.remove();     // 원소를 삭제할 수 없으면 예외 발생 (프로그램 중단)
        queue.poll();       // 삭제할 수 없으면 null 반환 (프로그램 유지)

        // 조회
        queue.element();    // 원소를 조회할 수 없으면 예외 발생 (프로그램 중단)
        queue.peek();       // 원소를 조회할 수 없으면 null 반환 (프로그램 유지)
    }
}
