package ssafy.stack;

import java.util.Stack;

public class Stack1 {

    public static void main(String[] args) {
        Stack<String> stack = new Stack<> ();

        stack.push("고양이");
        stack.push("토끼");
        stack.push("쥐");

        for (int i = 0; i < 3; i++) {
            System.out.println(stack.pop());
        }
    }
}
