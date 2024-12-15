package ssafy.testa;

//package ssafy.testa;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class SweaMaxinos2 {

    private static int N;
    private static int maxConnected;
    private static int minWireLen;

    private static int[] di = new int[]{1, 0, -1, 0};
    private static int[] dj = new int[]{0, 1, 0, -1};

    private static int[][] maxinos;

    private static ArrayList<int[]> cores;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {
            N = Integer.parseInt(br.readLine());
            maxinos = new int[N + 2][N + 2];

            for (int initJ = 0; initJ < N + 2; initJ++) {
                maxinos[0][initJ] = 9;
                maxinos[N + 1][initJ] = 9;
                maxinos[initJ][0] = 9;
                maxinos[initJ][N + 1] = 9;
            }
            for (int i = 0; i < N; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++) {
                    maxinos[i + 1][j + 1] = Integer.parseInt(st.nextToken());
                }
            }

            initConnect();

            maxConnected = -1;
            minWireLen = 10001;
            connectCore(0, 0, 0);

            sb.append('#').append(tc).append(' ').append(minWireLen).append('\n');
            bw.write(sb.toString());
            bw.flush();
            sb.setLength(0);
        }
        br.close();
        bw.close();
    }

    private static void initConnect() {
        cores = new ArrayList<>();
        for (int i = 0; i < N + 2; i++) {
            for (int j = 0; j < N + 2; j++) {
                if (maxinos[i][j] == 1) {
                    if (i == 1 || i == N ||
                            j == 1 || j == N) {
                        maxinos[i][j] = 5;
                    } else {
                        cores.add(new int[] {i, j});
                    }
                }
            }
        }
    }

    private static void connectCore(int lv, int connected, int wireLen) {
        if (lv == cores.size()) {
            if (maxConnected < connected) {
                maxConnected = connected;
                minWireLen = wireLen;
            } else if (maxConnected == connected && minWireLen > wireLen) {
                minWireLen = wireLen;
            }
            return;
        }

        if (connected + (cores.size() - lv) < maxConnected) {
            return;
        }

        connectCore(lv + 1, connected, wireLen);

        int i = cores.get(lv)[0];
        int j = cores.get(lv)[1];
        for (int k = 0; k < 4; k++) {
            int mi = i + di[k];
            int mj = j + dj[k];
            while (0 <= mi && mi < N + 2 &&
                    0 <= mj && mj < N + 2 &&
                    maxinos[mi][mj] == 0) {
                mi += di[k];
                mj += dj[k];
            }

            if (maxinos[mi][mj] == 9) {
                mi = i + di[k];
                mj = j + dj[k];
                int tempLen = 0;
                while (0 <= mi && mi < N + 2 &&
                        0 <= mj && mj < N + 2 &&
                        maxinos[mi][mj] == 0) {
                    maxinos[mi][mj] = 5;
                    mi += di[k];
                    mj += dj[k];
                    tempLen++;
                }

                connectCore(lv + 1, connected + 1, wireLen + tempLen);

                mi -= di[k];
                mj -= dj[k];
                while ((i != mi || j != mj) &&
                        0 <= mi && mi < N + 2 &&
                        0 <= mj && mj < N + 2 &&
                        maxinos[mi][mj] == 5) {
                    maxinos[mi][mj] = 0;
                    mi -= di[k];
                    mj -= dj[k];
                }
                //System.out.println(Arrays.deepToString(maxinos));
            }
        }
    }
}
