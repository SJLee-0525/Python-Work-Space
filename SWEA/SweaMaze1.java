package ssafy.queue;

import java.util.Scanner;
import java.util.Arrays;
import java.util.Deque;
import java.util.LinkedList;

public class SweaMaze1 {

    public static int[][] maze;

    public static int[] di = {1, 0, -1, 0};
    public static int[] dj = {0, 1, 0, -1};

    public static int[] findStart() {
        for (int i = 0; i < 16; i++) {
            for (int j = 0; j < 16; j++) {
                if (maze[i][j] == 2) {
                    return new int[] {i, j};
                }
            }
        }
        return new int[]{-1, -1};
    }

    public static int BFS(int[] start) {
        Deque<int[]> queue = new LinkedList<>();
        queue.offerLast(start);

        int[][] visited = new int[16][16];
        int i = start[0];
        int j = start[1];
        visited[i][j] = 1;

        while (!queue.isEmpty()) {
            int[] now = queue.pollFirst();
            i = now[0];
            j = now[1];
            for (int k = 0; k < 4; k++) {
                int mi = i + di[k];
                int mj = j + dj[k];
                if (0 <= mi && mi < 16 &&
                        0 <= mj && mj < 16 &&
                        visited[mi][mj] == 0 &&
                        maze[mi][mj] != 1) {
                    if (maze[mi][mj] == 3) {
                        return 1;
                    }
                    visited[mi][mj] = 1;
                    queue.offerLast(new int[] {mi, mj});
                }
            }
        }
        return 0;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        for (int t = 0 ; t < 10; t++) {
            int tc = scanner.nextInt();
            scanner.nextLine();

            maze = new int[16][16];

            for (int i = 0; i < 16; i++) {
                String inputStr = scanner.nextLine();
                for (int j = 0; j < 16; j++) {
                    char temp = inputStr.charAt(j);
                    maze[i][j] = Character.getNumericValue(temp);
                }
            }

            int[] start = findStart();

            System.out.println("#" + tc + " " + BFS(start));
        }
        scanner.close();
    }
}
