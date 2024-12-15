package ssafy.queue;

import java.util.Scanner;
import java.util.Deque;
import java.util.LinkedList;
import java.util.Arrays;

public class Swea5105 {

    public static int[][] maze;

    public static int[] di = {1, 0, -1, 0};
    public static int[] dj = {0, 1, 0, -1};

    public static int[] findStart(int N) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (maze[i][j] == 2) {
                    return new int[] {i, j};
                }
            }
        }
        return new int[] {-1, -1};
    }

    public static int BFS(int[] start, int N) {
        Deque<int[]> queue = new LinkedList<>();
        queue.offerLast(start);

        int i = start[0];
        int j = start[1];
        int[][] visited = new int[N][N];
        visited[i][j] = 1;

        while (!queue.isEmpty()) {
            int[] now = queue.pollFirst();
            i = now[0];
            j = now[1];
            for (int k = 0; k < 4; k++) {
                int mi = i + di[k];
                int mj = j + dj[k];
                if (0 <= mi && mi < N &&
                        0 <= mj && mj < N &&
                        visited[mi][mj] == 0 &&
                        maze[mi][mj] != 1) {
                    visited[mi][mj] = visited[i][j] + 1;
                    if (maze[mi][mj] == 3) {
                        return visited[mi][mj] - 2;
                    }
                    queue.offerLast(new int[] {mi, mj});
                }
            }
        }
        return 0;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();
        for (int tc = 1; tc <= T; tc++) {
            int N = scanner.nextInt();
            scanner.nextLine();

            maze = new int[N][N];
            for (int i = 0; i < N; i++) {
                String inputStr = scanner.nextLine();
                for (int j = 0; j < N; j++) {
                    char temp = inputStr.charAt(j);
                    maze[i][j] = Character.getNumericValue(temp);
                }
            }

            int[] start = findStart(N);
            int result = BFS(start, N);

            System.out.println("#" + tc + " " + result);
        }
        scanner.close();
    }
}
