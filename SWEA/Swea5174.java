package ssafy.tree;

import java.util.Scanner;

public class Swea5174 {

    public static int count;

    public static int[] left;
    public static int[] right;

    public static void order(int node) {
        if (node == 0) {
            return;
        }
        order(left[node]);
        order(right[node]);
        count++;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        byte T = scanner.nextByte();
        for (byte tc = 1; tc <= T; tc++) {
            short E = scanner.nextShort(); // 간선의 개수
            short N = scanner.nextShort(); // 루트 노드

            count = 0;
            left = new int[E + 2];
            right = new int[E + 2];

            for (short e = 0; e < E; e++) {
                int parent = scanner.nextInt();
                int child = scanner.nextInt();

                if (left[parent] == 0) {
                    left[parent] = child;
                } else {
                    right[parent] = child;
                }
            }
            order(N);
            System.out.println("#" + tc + " " + count);
        }
        scanner.close();
    }
}
