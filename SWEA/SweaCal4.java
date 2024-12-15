package ssafy.tree;

import java.util.Scanner;
import java.util.Arrays;

public class SweaCal4 {

    public static int N;

    public static String[] tree;
    public static int[] left;
    public static int[] right;

    public static int inOrder(int node) {
        if (node > N) {
            return 0;
        } else if (tree[node].matches("[-+]?\\d*\\.?\\d+")) {
            return Integer.parseInt(tree[node]);
        } else {
            int leftSide = inOrder(left[node]);
            int rightSide = inOrder(right[node]);
            int temp = 0;
            if (tree[node].equals("+")) {
                temp = leftSide + rightSide;
            } else if (tree[node].equals("-")) {
                temp = leftSide - rightSide;
            } else if (tree[node].equals("*")) {
                temp = leftSide * rightSide;
            } else if (tree[node].equals("/")) {
                temp = leftSide / rightSide;
            }
            return temp;
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        for (byte tc = 1; tc <= 10; tc++) {
            N = scanner.nextInt();
            scanner.nextLine();

            tree = new String[N + 1];
            left = new int[N + 1];
            right = new int[N + 1];

            for (int n = 0; n < N; n++) {
                String[] inputStr = scanner.nextLine().split(" ");

                int node = Integer.parseInt(inputStr[0]);
                tree[node] = inputStr[1];
                if (inputStr.length == 3) {
                    left[node] = Integer.parseInt(inputStr[2]);
                } else if (inputStr.length == 4) {
                    left[node] = Integer.parseInt(inputStr[2]);
                    right[node] = Integer.parseInt(inputStr[3]);
                }
            }

            // System.out.println(Arrays.toString(tree));
            // System.out.println(Arrays.toString(left));
            // System.out.println(Arrays.toString(right));

            int result = inOrder(1);

            System.out.println("#" + tc + " " + result);
        }
        scanner.close();
    }
}
