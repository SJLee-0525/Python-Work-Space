package ssafy.testa;

import java.io.BufferedWriter;
import java.io.BufferedReader;
import java.io.OutputStreamWriter;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class SweaSwimmingPool {

    private static int minFare;

    private static int[] priceList;
    private static int[] plan;

    private static void calPrice(int month, int tempFare) {
        if (month >= 12) {
            if (minFare > tempFare) {
                minFare = tempFare;
            }
            return;
        }

        if (tempFare >= minFare) {return;}

        if (priceList[0] * plan[month] < priceList[1]) {
            calPrice(month + 1, tempFare + priceList[0] * plan[month]);
        } else {
            calPrice(month + 1, tempFare + priceList[1]);
        }
        calPrice(month + 3, tempFare + priceList[2]);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int T = Integer.parseInt(st.nextToken());
        for (int tc = 1; tc <= T; tc++) {
            st = new StringTokenizer(br.readLine());
            priceList = new int[4];
            for (int p = 0; p < 4; p++) {
                priceList[p] = Integer.parseInt(st.nextToken());
            }

            st = new StringTokenizer(br.readLine());
            plan = new int[12];
            for (int p = 0; p < 12; p++) {
                plan[p] = Integer.parseInt(st.nextToken());
            }

            minFare = priceList[3];
            calPrice(0, 0);

            StringBuilder sb = new StringBuilder();
            sb.append('#').append(tc).append(' ').append(minFare).append('\n');
            bw.write(sb.toString());
            bw.flush();
            sb.setLength(0);
        }
        br.close();
        bw.close();
    }
}
