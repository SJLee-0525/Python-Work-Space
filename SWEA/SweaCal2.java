package ssafy.stack;

import java.util.Scanner;
import java.util.Stack;
import java.util.Arrays;
import java.util.Map;
import java.util.HashMap;

public class SweaCal2 {

    // 연산자 우선순위를 매핑 (문자 , 숫자)
    public static Map<Character, Integer> operatorValue = new HashMap<>();

    static {
        operatorValue.put('+', 1);
        operatorValue.put('-', 1);
        operatorValue.put('*', 2);
        operatorValue.put('/', 2);
    }

    // 중위 표기식을 후위 표기식으로 변환
    public static String infixToPostfix(String infix) {
        Stack<Character> stack = new Stack<>(); // 스택 생성

        String postfix = "";                    // 빈 문자열로 후위표기식 생성

        for (int i = 0; i < infix.length(); i++) {  // 중위 표기식 순회하면서
            char elem = infix.charAt(i);
            if ('0' <= elem && elem <= '9') {       // 만약 숫자면
                postfix += elem;                    // 후위 표기식에 바로 추가
            } else {                                // 숫자가 아니면 : 연산자면
                while (!stack.isEmpty() &&          // 연산자 스택의 마지막에 위치한 요소의 우선 수위가 더 낮을 때 까지
                        operatorValue.get(stack.peek()) >= operatorValue.get(elem)) {
                    char popItem = stack.pop();     // pop하고
                    postfix += popItem;             // 후위 표기식에 추가
                }
                stack.push(elem);                   // while 탈출하면 해당 연산자 스택에 추가
            }
        }
        while (!stack.isEmpty()) {                  // 다 돌아도 스택에 연산자가 남아있을 수 있음
            postfix += stack.pop();                 // 스택이 빌 때까지 pop하고 후위 표기식에 추가
        }
        return postfix;                             // 후위 표기식 리턴
    }

    // 후위 표기식을 받아 연산 수행
    public static int calPostfix(String postfix) {
        Stack<Integer> stack = new Stack<>();        // 스택 생성

        for (int i = 0; i < postfix.length(); i++) { // 후위 표기식을 순회
            char elem = postfix.charAt(i);
            if ('0' <= elem && elem <= '9') {        // 만약 숫자면 정수로 바꿔 스택에 추가
                stack.push(Character.getNumericValue(elem));
            } else {                                 // 숫자가 아니면 : 연산자면
                int num1 = stack.pop();              // 숫자 2개를 스택에서 뽑고
                int num2 = stack.pop();              // 연산자에 따라 연산 수행 후 스택에 다시 삽입
                if (elem == '+') {
                    stack.push(num2 + num1);
                } else if (elem == '-') {
                    stack.push(num2 - num1);
                } else if (elem == '*') {
                    stack.push(num2 * num1);
                } else {
                    stack.push(num2 / num1);
                }
            }
        }
        return stack.peek();    // 연산이 다 끝나면 스택에 남아있는 값 반환
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        for (int tc = 1; tc <= 10; tc++) {
            int N = scanner.nextInt();                  // 중위 표기식 길이
            scanner.nextLine();
            String strInfix = scanner.nextLine();       // 중위 표기식 입력 받음

            String postfix = infixToPostfix(strInfix);  // 중위 표기식을 후위 표기식으로 변환
            // System.out.println(postfix);

            int result = calPostfix(postfix);           // 후위 표기식을 연산
            System.out.println("#" + tc + " " + result);
        }
        scanner.close();
    }
}
