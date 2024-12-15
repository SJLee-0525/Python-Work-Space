package ssafy.testa;

import java.io.BufferedWriter;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class SweaChef {

    private static int N, result;
    private static int[] used, groupA, groupB;
    private static int[][] scoreBoard;

    private static void combi(int lv, int cnt) {
        if (cnt > N / 2) return;

        if (lv == N) {
            if (cnt == N / 2) result = Math.min(result, calScore());
            return;
        }

        used[lv] = 1;
        combi(lv + 1, cnt + 1);
        used[lv] = 0;
        combi(lv + 1, cnt);
    }

    private static int calScore() {
        groupA = new int[N / 2];
        groupB = new int[N / 2];

        int indexA = 0, indexB = 0;
        for (int i = 0; i < N; i++) {
            if (used[i] == 1) groupA[indexA++] = i;
            else groupB[indexB++] = i;
        }

        int tempA = 0, tempB = 0;
        for (int i = 0; i < N / 2; i++) {
            for (int j = 0; j < N / 2; j++) {
                tempA += scoreBoard[groupA[i]][groupA[j]];
                tempB += scoreBoard[groupB[i]][groupB[j]];
            }
        }
        return Math.abs(tempA - tempB);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {
            N = Integer.parseInt(br.readLine());

            scoreBoard = new int[N][N];
            used = new int[N];
            for (int i = 0; i < N; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++) {
                    scoreBoard[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            result = 10000001;
            combi(0, 0);

            sb.append('#').append(tc).append(' ').append(result).append('\n');
            bw.write(sb.toString());
            bw.flush();
            sb.setLength(0);
        }
        br.close();
        bw.close();
    }
}
