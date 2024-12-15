/*
8
1 W 2 3
2 F 4 5
3 R 6 7
4 O 8
5 T
6 A
7 E
8 S
 */

package ssafy.tree;

import java.util.Scanner;
import java.util.Arrays;

public class SweaInorderTravel {

    public static int N;

    public static char[] val;
    public static int[] left;
    public static int[] right;

    public static void inOrder(int node) {
        if (node == 0) {
            return;
        }
        inOrder(left[node]);
        System.out.print(val[node]);
        inOrder(right[node]);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        for (byte tc = 1; tc <= 10; tc++) {
            N = scanner.nextInt();
            scanner.nextLine();

            val = new char[N + 1];
            left = new int[N + 1];
            right = new int[N + 1];

            for (short n = 0; n < N; n++) {
                String[] inputStr = scanner.nextLine().split(" ");

                int parent = Integer.parseInt(inputStr[0]);
                val[parent] = inputStr[1].charAt(0);
                if (inputStr.length == 3) {
                    left[parent] = Integer.parseInt(inputStr[2]);
                } else if (inputStr.length == 4) {
                    left[parent] = Integer.parseInt(inputStr[2]);
                    right[parent] = Integer.parseInt(inputStr[3]);
                }
            }
            // System.out.println(Arrays.toString(val));   // [ , W, F, R, O, T, A, E, S]
            // System.out.println(Arrays.toString(left));  // [0, 2, 4, 6, 8, 0, 0, 0, 0]
            // System.out.println(Arrays.toString(right)); // [0, 3, 5, 7, 0, 0, 0, 0, 0]

            System.out.print("#" + tc + " ");
            inOrder(1);
            System.out.println();
        }
        scanner.close();
    }
}
