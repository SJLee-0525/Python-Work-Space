package baekjoon;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.StringTokenizer;

public class baekjoon14719 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int H = Integer.parseInt(st.nextToken());
        int W = Integer.parseInt(st.nextToken());

        int[] ground = new int[W];
        st = new StringTokenizer(br.readLine());
        for (int w = 0; w < W; w++) {
            ground[w] = Integer.parseInt(st.nextToken());
        }

        int leftPointer = 0, rightPointer = W - 1, rain = 0;
        int leftMax = ground[leftPointer], rightMax = ground[rightPointer];

        while (leftPointer < rightPointer) {
            if (leftMax < rightMax) {
                leftMax = Math.max(leftMax, ground[++leftPointer]);
                if (leftMax > ground[leftPointer]) {
                    rain += leftMax - ground[leftPointer];
                }
            } else {
                rightMax = Math.max(rightMax, ground[--rightPointer]);
                if (rightMax > ground[rightPointer]) {
                    rain += rightMax - ground[rightPointer];
                }
            }
        }

        sb.append(rain);
        bw.write(sb.toString());
        bw.flush();
        sb.setLength(0);

        br.close();
        bw.close();
    }
}
