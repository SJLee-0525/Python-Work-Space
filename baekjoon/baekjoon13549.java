package baekjoon;

import java.io.BufferedWriter;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.Arrays;
import java.util.Deque;
import java.util.LinkedList;

public class baekjoon13549 {

    private static int N, K;

    private static int[] visited = new int[100001];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        int result = findBrother(N, K);

        sb.append(result);
        bw.write(sb.toString());
        bw.flush();
        sb.setLength(0);

        br.close();
        bw.close();
    }

    private static int findBrother(int me, int brother) {
        Deque<Integer> queue = new LinkedList<>();
        queue.offerLast(me);
        visited[me] = 1;

        while (!queue.isEmpty()) {
            me = queue.pollFirst();

            if (me == brother) return visited[me] - 1;

            if (me * 2 <= 100000 && (visited[me * 2] == 0 || visited[me * 2] > visited[me])) {
                visited[me * 2] = visited[me];
                queue.offerLast(me * 2);
            }
            if (me + 1 <= 100000 && (visited[me + 1] == 0 || visited[me + 1] > visited[me] + 1)) {
                visited[me + 1] = visited[me] + 1;
                queue.offerLast(me + 1);
            }
            if (me - 1 >= 0 && (visited[me - 1] == 0 || visited[me - 1] > visited[me] + 1)) {
                visited[me - 1] = visited[me] + 1;
                queue.offerLast(me - 1);
            }
        }
        return -1;
    }
}
