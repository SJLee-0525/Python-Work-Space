package ssafy.testa;

import java.io.BufferedWriter;
import java.io.BufferedReader;
import java.io.OutputStreamWriter;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.Arrays;

public class Swea5207 {

    private static int N, M, resultCnt;

    private static int[] A, B;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());

            A = new int[N];
            B = new int[M];

            st = new StringTokenizer(br.readLine());
            for (int a = 0; a < N; a++) {
                A[a] = Integer.parseInt(st.nextToken());
            }
            Arrays.sort(A);

            st = new StringTokenizer(br.readLine());
            for (int b = 0; b < N; b++) {
                B[b] = Integer.parseInt(st.nextToken());
            }

            resultCnt = 0;
            for (int numB : B) {
                bSearch(0, N - 1, 0, numB);
            }

            sb.append('#').append(tc).append(' ').append(resultCnt).append('\n');
            bw.write(sb.toString());
            bw.flush();
            sb.setLength(0);
        }

        br.close();
        bw.close();
    }

    // 배열 A에서 B를 찾는 것
    private static void bSearch(int left, int right, int dir, int target) {
        int mid = (left + right) / 2;

        if (target == A[mid]) {
//            System.out.println(dir + " , " + mid);
            resultCnt++;
            return;
        }

        if (target < A[mid] && dir != 1) {
            bSearch(left, mid - 1, 1, target);
        } else if (target > A[mid] && dir != 2) {
            bSearch(mid + 1, right, 2, target);
        }
    }
}
