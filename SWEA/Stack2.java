package ssafy.stack;

public class Stack2 {

    // 스택 배열 생성
    public static String[] stack = new String[100];

    // 마지막에 들어간 데이터의 index를 가리키는 top
    public static int top = -1;

    public static boolean isEmpty() {
        // return (top == -1) ? true : false;
        return top == -1;
    }

    public static boolean isFull() {
        return (top == stack.length - 1) ? true : false;
        // return top == stack.length - 1;
    }

    public static void pushItem(String item) {
        if (isFull()) {
            System.out.println("스택이 가득 찼습니다.");
            return;
        }
        stack[++top] = item;
    }

    public static String popItem() {
        if (isEmpty()) {
            System.out.println("스택이 비어있습니다.");
            return null; // 스트링을 리턴해줘야 하니까
        }
        String popItem = stack[top];
        stack[top--] = null; // pop한 위치를 빈 것으로 되돌림
        return popItem;
    }

    // pop과 달리 마지막 원소만 확인하는 것
    public static String peek() {
        if (isEmpty()) {
            System.out.println("스택이 비어있습니다.");
            return null;
        }
        return stack[top];
    }

    public static void main(String[] args) {
        pushItem("고양이");
        pushItem("토끼");
        pushItem("쥐");

        // 스택이 비어있지 않은 동안 pop 호출
        while (!isEmpty()) {
            System.out.println(popItem());
        }

        // 비어있는 상태에서 pop해보기
        System.out.println(popItem());

        // 100개 다 채워보기
        for (int i = 1; i <= 100; i++) {
            pushItem(i + "");
        }

        // 초과해서 push해보기
        pushItem("101");

        System.out.println(isFull());
    }
}
