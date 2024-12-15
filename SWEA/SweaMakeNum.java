package ssafy.testa;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.Arrays;
import java.util.ArrayList;

public class SweaMakeNum {

    private static int N; // 숫자의 개수

    private static int maxResult;
    private static int minResult;

    private static int[] numList;
    private static int[] used;
    private static int[] operPath;

    private static ArrayList<Integer> operatorList;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int T = Integer.parseInt(st.nextToken());
        for (int tc = 1; tc <= T; tc++) {
            N = Integer.parseInt(br.readLine());

            int[] operatorCount = new int[4];
            st = new StringTokenizer(br.readLine());
            for (int o = 0; o < operatorCount.length; o++) {
                operatorCount[o] = Integer.parseInt(st.nextToken());
            }

            makeValidOperator(operatorCount);

            numList = new int[N];
            st = new StringTokenizer(br.readLine());
            for (int n = 0; n < N; n++) {
                numList[n] = Integer.parseInt(st.nextToken());
            }
//            System.out.println(Arrays.toString(numList));

            maxResult = -100000001;
            minResult = 100000001;

            operPath = new int[operatorList.size()];
            used = new int[operatorList.size()];
            perm(0);

            int result = maxResult - minResult;

            StringBuilder sb = new StringBuilder();
            sb.append('#').append(tc).append(' ').append(result).append('\n');
            bw.write(sb.toString());
            bw.flush();
            sb.setLength(0);
        }
        br.close();
        bw.close();
    }

    private static void makeValidOperator(int[] inputOperatorCount) {
        operatorList = new ArrayList<>();

        for (int k = 0; k < 4; k++) {
            for (int r = 0; r < inputOperatorCount[k]; r++) {
                operatorList.add(k);
            }
        }
//        System.out.println(operatorList);
    }

    //[0, 0, 1, 3]
    private static void perm(int lv) {
        if (lv == operatorList.size()) {
//            System.out.println(Arrays.toString(operPath));
            calculate(operPath);
            return;
        }

        int[] nowUsed = new int[4];
        for (int i = 0; i < operatorList.size(); i++) {
            if (nowUsed[operatorList.get(i)] == 1 || used[i] == 1) {
                continue;
            }
            operPath[lv] = operatorList.get(i);
            used[i] = 1;
            nowUsed[operatorList.get(i)] = 1;
            perm(lv + 1);
            used[i] = 0;
        }
    }

    private static void calculate(int[] inputOperPath) {
        int result = numList[0];

        for (int i = 0; i < inputOperPath.length; i++) {
            int target = numList[i + 1];
            switch (inputOperPath[i]) {
                case 0:
                    result += target;
                    break;
                case 1:
                    result -= target;
                    break;
                case 2:
                    result *= target;
                    break;
                case 3:
                    result /= target;
                    break;
            }
        }
        if (maxResult < result) {
            maxResult = result;
        }
        if (minResult > result) {
            minResult = result;
        }
    }
}