package ssafy.stack;

import java.util.Scanner;
import java.util.Stack;
import java.util.Arrays;

public class Swea4874 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();
        scanner.nextLine();
        for (int tc = 1; tc <= T; tc++) {
            String inputStr = scanner.nextLine();
            String[] strArr = inputStr.split(" ");
            // System.out.println(Arrays.toString(strArr));

            Stack<Integer> stack = new Stack<>();
            boolean flag = true;
            int result = 0;
            for (int i = 0; i < strArr.length; i++) {
                if (strArr[i].matches("[-+]?\\d*\\.?\\d+")) {
                    int num = Integer.parseInt(strArr[i]);
                    stack.push(num);
                } else if (strArr[i].equals(".")) {
                    if (stack.size() == 1) {
                        result = stack.pop();
                    } else {
                        flag = false;
                        break;
                    }
                } else {
                    if (stack.size() >= 2) {
                        int num2 = stack.pop();
                        int num1 = stack.pop();
                        int temp = 0;
                        if (strArr[i].equals("+")) {
                            temp = num1 + num2;
                        } else if (strArr[i].equals("-")) {
                            temp = num1 - num2;
                        } else if (strArr[i].equals("*")) {
                            temp = num1 * num2;
                        } else {
                            temp = num1 / num2;
                        }
                        stack.push(temp);
                    } else {
                        flag = false;
                        break;
                    }
                }
            }
            if (flag) {
                System.out.println("#" + tc + " " + result);
            } else {
                System.out.println("#" + tc + " error");
            }
        }
        scanner.close();
    }
}