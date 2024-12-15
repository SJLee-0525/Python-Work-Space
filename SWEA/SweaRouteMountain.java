package ssafy.testa;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class SweaRouteMountain {

    private static int N;
    private static int K;
    private static int result;

    private static int[][] map;

    private static int[] di = new int[]{1, 0, -1, 0};
    private static int[] dj = new int[]{0, 1, 0, -1};

    private static int calSummitHeight() {
        int temp = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (temp < map[i][j]) {
                    temp = map[i][j];
                }
            }
        }
        return temp;
    }

    private static ArrayList<int[]> findSummit() {
        int summitHeight = calSummitHeight();
        ArrayList<int[]> summitList = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (map[i][j] == summitHeight) {
                    summitList.add(new int[] {i, j});
                }
            }
        }
        return summitList;
    }

    private static void dfs(int i, int j, int cnt, boolean cut, int[][] inputMap, int[][] visited) {
        if (result < cnt + 1) {
            result = cnt + 1;
        }

        visited[i][j] = 1;
        for (int k = 0; k < 4; k++) {
            int mi = i + di[k];
            int mj = j + dj[k];
            if (0 <= mi && mi < N &&
                    0 <= mj && mj < N &&
                    visited[mi][mj] != 1) {
                if (inputMap[i][j] > inputMap[mi][mj]) {
                    dfs(mi, mj, cnt + 1, cut, inputMap, visited);
                } else if (cut == false &&
                        visited[mi][mj] == 0 &&
                        inputMap[i][j] + K > inputMap[mi][mj]) {
                    int temp = inputMap[mi][mj];
                    inputMap[mi][mj] = inputMap[i][j] - 1;
                    dfs(mi, mj, cnt + 1,true, inputMap, visited);
                    inputMap[mi][mj] = temp;
                }
            }
        }
        visited[i][j] = 0;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= T; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            K = Integer.parseInt(st.nextToken());

            map = new int[N][N];
            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++) {
                    map[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            result = 0;
            ArrayList<int[]> summitList = findSummit();
            for (int i = 0; i < summitList.size(); i++) {
                int si = summitList.get(i)[0];
                int sj = summitList.get(i)[1];
                int[][] visited = new int[N][N];
                dfs(si, sj, 0, false, map, visited);
            }
            sb.append('#').append(tc).append(' ').append(result).append('\n');
            bw.write(sb.toString());
            bw.flush();
            sb.setLength(0);
        }
        br.close();
        bw.close();
    }
}