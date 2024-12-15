package ssafy.tree;

import java.util.Scanner;

public class Swea5176 {

    public static int N;

    public static int seqIndex;
    public static int root;
    public static int tar;

    public static void inOrder(int node) {
        if (node > N) {
            return;
        }
        inOrder(node * 2);
        seqIndex++;
        if (node == 1) {
            root = seqIndex;
        } else if (node == N / 2) {
            tar = seqIndex;
        }
        inOrder(node * 2 + 1);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        byte T = scanner.nextByte();
        for (byte tc = 1; tc <= T; tc++) {
            N = scanner.nextInt();

            seqIndex = 0;
            root = 0;
            tar = 0;

            inOrder(1);

            System.out.println("#" + tc + " " + root + " " + tar);
        }
        scanner.close();
    }
}