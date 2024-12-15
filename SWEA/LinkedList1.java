package ssafy.linkedlist;

class Node {
    String data;
    Node link;
}

class SinglyLinkedList {
    Node head;
    int size;
    SinglyLinkedList() {
        head = new Node();
    }

    // 삽입
    void addData(int i, String data) {
        // i 인덱스에 데이터 삽입
        // 0 이면 제일 앞에 추가
        // size와 같으면 제일 뒤에 추가

        if (i < 0 || i > size) {
            System.out.println("삽입할 범위를 확인해 주세요.");
            return;
        }

        size++;

        // 새 노드 생성
        Node newNode = new Node();
        newNode.data = data;

        // 삽입할 위치 앞에 있는 노드 찾기
        Node curr = head;
        for (int k = 0; k < i; k++) {
            curr = curr.link;
        }

        // 새 노드부터 연결
        newNode.link = curr.link;
        curr.link = newNode;
    }

    // 삭제
    void removeData(int i) {
        // 0이면 제일 앞에 있는 삭제
        // (size - 1)번: 마지막 데이터 삭제

        if (i < 0 || i >= size) {
            System.out.println("삭제할 수 없는 범위입니다.");
            return;
        }

        size--;

        // 삭제할 노드의 앞 노드로 이동
        Node curr = head;
        for (int k = 0; k < i; k++) {
            curr = curr.link;
        }

        curr.link = curr.link.link;
    }

    // 조회
    void printAll() {
        Node curr = head.link;

        while (curr != null) {
            System.out.print(curr.data + " -> ");
            curr = curr.link;
        }
        System.out.println();
    }


    // 사이즈 확인
}

public class LinkedList1 {

    public static void main(String[] args) {
        SinglyLinkedList list = new SinglyLinkedList();

        list.addData(0, "1번째 삽입");
        list.printAll();
        list.addData(0, "2번째 삽입");
        list.addData(0, "3번째 삽입");
        list.printAll();
        list.addData(0, "4번째 삽입");
        list.addData(0, "5번째 삽입");
        list.addData(0, "6번째 삽입");
        list.printAll();

    }
}
