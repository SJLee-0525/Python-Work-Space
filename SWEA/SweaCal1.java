package ssafy.stack;

import java.util.Scanner;
import java.util.Arrays;
import java.util.Stack;

public class SweaCal1 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        for (byte tc = 1; tc <= 10; tc++) {
            int N = scanner.nextInt();
            scanner.nextLine();
            String infix = scanner.nextLine();

            String postfix = infixToPostfix(infix, N);
            // System.out.println(postfix);

            int result = calPostfix(postfix);
            System.out.println("#" + tc + " " + result);
        }
        scanner.close();
    }

    public static String infixToPostfix(String infix, int N) {
        Stack<Character> stack = new Stack<>();

        String postfix = "";
        for (int i = 0; i < N; i++) {
            char elem = infix.charAt(i);
            if ('0' <= elem && elem <= '9') {
                postfix += elem;
            } else {
                stack.push(elem);
            }
        }
        while (!stack.isEmpty()) {
            postfix += stack.pop();
        }
        return postfix;
    }

    public static int calPostfix(String postfix) {
        Stack<Integer> stack = new Stack<>();
        int result = 0;

        for (int i = 0; i < postfix.length(); i++) {
            char elem = postfix.charAt(i);
            if ('0' <= elem && elem <= '9') {
                stack.push(Character.getNumericValue(elem));
            } else {
                int num2 = stack.pop();
                int num1 = stack.pop();
                int temp = num1 + num2;
                stack.push(temp);
            }
        }
        return stack.peek();
    }
}
