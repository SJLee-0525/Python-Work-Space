package ssafy.testb;

import java.io.*;
import java.util.StringTokenizer;

public class no2 {

    private static int N, M, binN, result;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());

            binN = 0;
            for (int n = 0; n < N; n++) {
                binN = binN | (1 << n);
            }

            result = binN & M;
            if (result == binN) {
                sb.append('#').append(tc).append(" ON\n");
            } else {
                sb.append('#').append(tc).append(" OFF\n");
            }
        }
        bw.write(sb.toString());
        bw.flush();
        sb.setLength(0);
        bw.close();
        br.close();
    }
}
