package ssafy.queue;

import java.util.Deque;
import java.util.LinkedList;

public class Deque1 {

    public static void main(String[] args) {
        Deque<Integer> deque = new LinkedList<>();

        // 앞쪽에 원소 추가
        deque.addFirst(1);      // Deque의 앞쪽에 데이터를 삽입, 용량 초과시 Exception
        deque.offerFirst(1);    // Deque의 앞쪽에 데이터를 삽입 후 true, 용량 초과시 false
        deque.push(1);          // addFirst()와 동일

        // 뒤쪽에 원소 추가
        deque.addLast(1);       // Deque의 뒤쪽에 데이터를 삽입, 용량 초과시 Exception
        deque.add(1);              // addLast()와 동일
        deque.offerLast(1);     // Deque의 뒤쪽에 데이터를 삽입 후 true, 용량 초과시 false
        deque.offer(1);         // offerLast()와 동일

        // 앞쪽의 원소 삭제
        deque.removeFirst();        // Deque의 앞에서 제거, 비어있으면 예외
        deque.remove();             // removeFirst()와 동일
        deque.pop();                // removeFirst()와 동일
        deque.poll();               // Deque의 앞에서 제거, 비어있으면 null 리턴
        deque.pollFirst();          // poll()과 동일

        // 뒤쪽의 원소 삭제
        deque.removeLast();         // Deque의 뒤에서 제거, 비어있으면 예외
        deque.pollLast();           // Deque의 뒤에서 제거, 비어있으면 null 리턴

        // 값 확인
        deque.getFirst();           // 첫 번째 엘리먼트를 확인, 비어있으면 예외
        deque.peekFirst();          // 첫 번째 엘리먼트를 확인, 비어있으면 null 리턴
        deque.peek();               // peekFirst()와 동일

        deque.getLast();            // 마지막 엘리먼트를 확인, 비어있으면 예외
        deque.peekLast();           // 마지막 엘리먼트를 확인, 비어있으면 null 리턴

        deque.size();               // Deque에 들어있는 엘리먼트의 개수
    }
}
