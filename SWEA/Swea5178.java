package ssafy.tree;

import java.util.Scanner;

public class Swea5178 {

    public static int N;
    public static int M;
    public static int L;

    public static int[] tree;

    public static int inOrder(int node) {
        if (node > N) {
            return 0;
        } else if (tree[node] != 0) {
            return tree[node];
        }
        tree[node] = inOrder(node * 2) + inOrder(node * 2 + 1);
        return tree[node];
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        byte T = scanner.nextByte();
        for (byte tc = 1; tc <= T; tc++) {
            N = scanner.nextInt(); // 노드 개수
            M = scanner.nextInt(); // 리프 노드 개수
            L = scanner.nextInt(); // 값을 출력할 번호

            tree = new int[N + 1];

            for (int m = 0; m < M; m++) {
                int leafNodeNum = scanner.nextInt();
                int leafNodeVal = scanner.nextInt();
                tree[leafNodeNum] = leafNodeVal;
            }

            inOrder(1);

            System.out.println("#" + tc + " " + tree[L]);
        }
        scanner.close();
    }
}
