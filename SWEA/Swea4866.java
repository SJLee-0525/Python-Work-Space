package ssafy.stack;

import java.util.Scanner;
import java.util.ArrayDeque;
import java.util.Deque;


public class Swea4866 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();
        scanner.nextLine();

        for (byte tc = 1; tc <= T; tc++) {
            String inputStr = scanner.nextLine();
            Deque<Character> deque = new ArrayDeque<>();

            int result = 1;
            for (int i = 0; i < inputStr.length(); i++) {
                char c = inputStr.charAt(i);
                if (c == '{' || c == '(') {
                    deque.addLast(c);

                } else if (c == '}') {
                    if (!deque.isEmpty() && deque.getLast() == '{') {
                        deque.pollLast();
                    } else {
                        result = 0;
                        break;
                    }
                } else if (c == ')') {
                    if (!deque.isEmpty() && deque.getLast() == '(') {
                        deque.pollLast();
                    } else {
                        result = 0;
                        break;
                    }
                }
            }
            if (!deque.isEmpty()) {
                result = 0;
            }
            System.out.println("#" + tc + " " + result);
        }
        scanner.close();
    }
}