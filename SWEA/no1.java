package ssafy.testb;

import java.io.*;

public class no1 {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {
            int N = Integer.parseInt(br.readLine());

            // 비트 연산을 통해 각 숫자가 저장됐는지 확인 (0~9까지 다 채우면 1111111111 = 1023)
            int cntNum = 0, sheepNum = 0;;

            while (cntNum < 1023) {
                sheepNum += N;              // 몇 번째 양인지
                int checkNum = sheepNum;    // 임시 변수 할당
                while (checkNum > 0) {
                    // cntNum | (1 << (checkNum % 10)) : cntNum에 해당 자릿수의 숫자가 나타났음을 기록: (1 << 3)은 숫자 3이 나왔음을 의미
                    cntNum = cntNum | (1 << (checkNum % 10));
                    checkNum /= 10; // 자릿수 감소
                }
            }
            sb.append('#').append(tc).append(' ').append(sheepNum).append('\n');
        }
        bw.write(sb.toString());
        bw.flush();
        sb.setLength(0);

        br.close();
        bw.close();
    }
}
