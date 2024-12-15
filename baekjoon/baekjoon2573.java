package baekjoon;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.Deque;
import java.util.LinkedList;

public class baekjoon2573 {

    private static int N, M;

    private static int[] di = {0, 1, 0, -1};
    private static int[] dj = {1, 0, -1, 0};

    private static int[][] iceberg;
    private static int[][] visited;

    private static Deque<Integer> queue;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        iceberg = new int[N][M];
        visited = new int[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                iceberg[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int year = 0;
        while (true) {
            boolean check = oneYearLater();
            if (!check) {
                year = 0;
                break;
            }
            year++;

            resetVisited();

            int piece = 0;
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    if (iceberg[i][j] > 0 && visited[i][j] == 0) {
                        bfs(i, j);
                        piece++;
                    }
                }
            }

            if (piece >= 2) {
                break;
            }
        }

        sb.append(year);
        bw.write(sb.toString());
        bw.flush();
        sb.setLength(0);

        br.close();
        bw.close();
    }

    private static boolean oneYearLater() {
        queue = new LinkedList<>();

        int mi, mj, cnt;
        boolean check = false;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (iceberg[i][j] > 0) {
                    cnt = 0;
                    for (int k = 0; k < 4; k++) {
                        mi = i + di[k];
                        mj = j + dj[k];
                        if (0 <= mi && mi < N &&
                            0 <= mj && mj < M &&
                            iceberg[mi][mj] == 0) {
                            cnt++;
                        }
                    }
                    queue.offerLast(i);
                    queue.offerLast(j);
                    queue.offerLast(cnt);
                    check = true;
                }
            }
        }

        int i, j;
        while (!queue.isEmpty()) {
            i = queue.pollFirst();
            j = queue.pollFirst();
            cnt = queue.pollFirst();
            iceberg[i][j] = iceberg[i][j] - cnt;
            if (iceberg[i][j] <= 0) iceberg[i][j] = 0;
        }

        return check;
    }

    private static void bfs(int si, int sj) {
        queue = new LinkedList<>();
        queue.offerLast(si);
        queue.offerLast(sj);
        visited[si][sj] = 1;

        int i, j, mi, mj;
        while (!queue.isEmpty()) {
            i = queue.pollFirst();
            j = queue.pollFirst();
            for (int k = 0; k < 4; k++) {
                mi = i + di[k];
                mj = j + dj[k];
                if (0 <= mi && mi < N &&
                    0 <= mj && mj < M &&
                    iceberg[mi][mj] > 0 &&
                    visited[mi][mj] == 0) {
                    queue.offerLast(mi);
                    queue.offerLast(mj);
                    visited[mi][mj] = 1;
                }
            }
        }
    }

    private static void resetVisited() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                visited[i][j] = 0;
            }
        }
    }
}
