package ssafy.testa;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.Arrays;

public class SweaCafe {

    private static int N, result;

    private static int[] di = new int[]{1, 1, -1, -1};
    private static int[] dj = new int[]{1, -1, -1, 1};
    private static int[] ate;

    private static int[][] cafeRoad, visited;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {
            N = Integer.parseInt(br.readLine());

            cafeRoad = new int[N][N];
            for (int i = 0; i < N; i++) {
                StringTokenizer st  = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++) {
                    cafeRoad[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            result = 0;
            for (int i = 0; i < N - 2; i++) {
                for (int j = 1; j < N - 1; j++) {
                    ate = new int[101];
                    visited = new int[N][N];
                    exploreCafe(i, j, i, j, 0);
                }
            }

            if (result == 0) result = -1;

            sb.append('#').append(tc).append(' ').append(result).append('\n');
            bw.write(sb.toString());
            bw.flush();
            sb.setLength(0);
        }

        br.close();
        bw.close();
    }

    private static void exploreCafe(int i, int j, int si, int sj, int k) {
        if (k > 0 && i == si && j == sj) {
            int temp = Arrays.stream(ate).sum();
            if (result < temp) result = temp;
            return;
        }

        if (k >= 4 || i < si) return;

        int mi = i + di[k];
        int mj = j + dj[k];
        if (0 <= mi && mi < N &&
                0 <= mj && mj < N &&
                visited[mi][mj] == 0 &&
                ate[cafeRoad[mi][mj]] == 0) {

            visited[mi][mj] = 1;
            ate[cafeRoad[mi][mj]] = 1;
            exploreCafe(mi, mj, si, sj, k);
            visited[mi][mj] = 0;
            ate[cafeRoad[mi][mj]] = 0;
        }

        if (k < 3) {
            int ti = i + di[k + 1];
            int tj = j + dj[k + 1];
            if (0 <= ti && ti < N &&
                    0 <= tj && tj < N &&
                    visited[ti][tj] == 0 &&
                    ate[cafeRoad[ti][tj]] == 0) {

                visited[ti][tj] = 1;
                ate[cafeRoad[ti][tj]] = 1;
                exploreCafe(ti, tj, si, sj, k + 1);
                visited[ti][tj] = 0;
                ate[cafeRoad[ti][tj]] = 0;
            }
        }
    }
}
