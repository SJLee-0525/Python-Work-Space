package ssafy.stack;

import java.util.Stack;
import java.util.Map;
import java.util.HashMap;

public class Stack3InfixToPostfix {

    public static void main(String[] args){

        String expression = "(6+5*(2-8)/2)";
//        String expression = "(3+5)*8";

        String postfix = infixToPostfix(expression);
        System.out.println(postfix);

        int result = evalPostfix(postfix);
        System.out.println(result);
    }

    static Map<Character, Integer> map = new HashMap<>();

    static {
        // 문자와 숫자를 매핑
        map.put('+', 1);
        map.put('-', 1);
        map.put('*', 2);
        map.put('/', 2);
        map.put('(', 0);
    }

    public static String infixToPostfix(String infix) {
        String postfix = "";
        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < infix.length(); i++) {
            char c = infix.charAt(i);

            if ('0' <= c && c <= '9') {
                // 피연산자가 나오면 (숫자면) 바로 출력
                postfix += c;
            } else if (c == '(') {
                // 여는 괄호면 stack에 push
                stack.push(c);
            } else if (c == ')') {
                // 닫는 괄호면 여는 괄호가 나올 때까지 pop
                char popItem = stack.pop();
                while (popItem != '(') {
                    postfix += popItem;
                    popItem = stack.pop();
                }
            } else {
                // 연산자 스택의 마지막에 우선 수위가 낮은 연산자가 올 때 까지 pop
                while (!stack.isEmpty() &&
                        stack.peek() != '(' &&
                        map.get(stack.peek()) >= map.get(c)) {

                    char popItem = stack.pop();
                    postfix += popItem;
                }
                stack.push(c);

            }
        }
        while (!stack.isEmpty()) {
            postfix += stack.pop();
        }
        return postfix;
    }

    public static int evalPostfix(String postfix) {

        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < postfix.length(); i++) {
            char c = postfix.charAt(i);

            // 문자열을 숫자인지 판별
            if ('0' <= c && c <= '9') {
                stack.push(c - '0'); // 이러면 int로 변환되는 듯;
            } else {
                int num1 = stack.pop();
                int num2 = stack.pop();
                int result;

                if (c == '+') {
                    result = num2 + num1;
                } else if (c == '-') {
                    result = num2 - num1;
                } else if (c == '*') {
                    result = num2 * num1;
                } else {
                    result = num2 / num1;
                }
                stack.push(result);
            }
        }
        return stack.pop();
    }
}
