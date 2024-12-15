package ssafy.testa;

import java.io.BufferedWriter;
import java.io.BufferedReader;
import java.io.OutputStreamWriter;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.Deque;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class SweaBlock {

    private static int N;  // 쏘는 횟수
    private static int W;  // 배열 너비
    private static int H;  // 배열 높이
    private static int result;

    private static int[] di = new int[]{1, 0, -1, 0};
    private static int[] dj = new int[]{0, 1, 0, -1};

    private static int[][] initBlock;

    private static void mainDef(int lv, int[][] mainInputBlock) {
        if (lv == N) {
            countBlock(mainInputBlock);
            return;
        }
        // System.out.println(Arrays.deepToString(mainInputBlock));

        int c = 0;
        for (int j = 0; j < W; j++) {
            boolean flag = false;
            for (int i = 0; i < H; i++) {
                // System.out.println(lv + ", "  + i + ", " + j);
                if (mainInputBlock[i][j] > 0) {
                    flag = true;
                    c++;
                    int[][] copyBlock = new int[H][W];
                    for (int ci = 0; ci < H; ci++) {
                        for (int cj = 0; cj < W; cj++) {
                            copyBlock[ci][cj] = mainInputBlock[ci][cj];
                        }
                    }
                    int[][] newBlock = bomb(i, j, copyBlock);
                    mainDef(lv + 1, newBlock);
                }
                if (flag) {
                    break;
                }
            }
        }
        if (c == 0) {
            mainDef(N, mainInputBlock);
        }
    }

    private static int[][] bomb(int si, int sj, int[][] inputBlock) {
        Deque<int[]> queue = new LinkedList<>();
        queue.offerLast(new int[]{si, sj});

        int[][] check = new int[H][W];
        check[si][sj] = 1;

        int[] now;
        while (!queue.isEmpty()) {
            now = queue.pollFirst();
            int i = now[0];
            int j = now[1];
            int val = inputBlock[i][j];
            if (val > 1) {
                for (int k = 0; k < 4; k++) {
                    for (int v = 1; v < val; v++) {
                        int mi = i + (di[k] * v);
                        int mj = j + (dj[k] * v);
                        if (0 <= mi && mi < H &&
                                0 <= mj && mj < W &&
                                check[mi][mj] == 0 &&
                                inputBlock[mi][mj] >= 1) {
                            check[mi][mj] = 1;
                            queue.offerLast(new int[]{mi, mj});
                        }
                    }
                }
            }
            inputBlock[i][j] = 0;
        }
        return getDownBlock(inputBlock);
    }

    private static int[][] getDownBlock(int[][] inputBlock) {
        int[][] newBlock = new int[H][W];
        for (int j = 0; j < W; j++) {
            ArrayList<Integer> temp = new ArrayList<>();
            for (int i = 0; i < H; i++) {
                if (inputBlock[i][j] > 0) {
                    temp.add(inputBlock[i][j]);
                }
            }
            int t_len = temp.size();
            for (int t = 0; t < t_len; t++) {
                newBlock[H - t_len + t][j] = temp.get(t);
            }
        }
        return newBlock;
    }

    private static void countBlock(int[][] inputBlock) {
        int cnt = 0;
        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {
                if (inputBlock[i][j] > 0) {
                    cnt++;
                }
            }
        }
        if (result > cnt) {
            result = cnt;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            W = Integer.parseInt(st.nextToken());
            H = Integer.parseInt(st.nextToken());

            initBlock = new int[H][W];
            for (int i = 0; i < H; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < W; j++) {
                    initBlock[i][j] = Integer.parseInt(st.nextToken());
                }
            }
            result = 1001;
            mainDef(0, initBlock);

            StringBuilder sb = new StringBuilder();
            sb.append('#').append(tc).append(' ').append(result).append('\n');
            bw.write(sb.toString());
            bw.flush();

            sb.setLength(0);
        }
        br.close();
        bw.close();
    }
}
