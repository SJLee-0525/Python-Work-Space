package ssafy.testa;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.Deque;
import java.util.LinkedList;

public class SweaChangyong {

    private static int N; // 살고 있는 사람의 수
    private static int M; // 알고 있는 관계 수

    private static int[] check;

    private static ArrayList<Integer>[] adjList;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int T = Integer.parseInt(st.nextToken());
        for (int tc = 1; tc <= T; tc++) {
            st = new StringTokenizer(br.readLine());

            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());

            adjList = new ArrayList[N + 1];
            for (int n = 0; n <= N; n++) {
                adjList[n] = new ArrayList<Integer>();
            }

            for (int m = 0; m < M; m++) {
                st = new StringTokenizer(br.readLine());
                int v1 = Integer.parseInt(st.nextToken());
                int v2 = Integer.parseInt(st.nextToken());
                adjList[v1].add(v2);
                adjList[v2].add(v1);
            }

//            System.out.println(Arrays.toString(adjList));

            int result = 0;
            check = new int[N + 1];
            for (int person = 1; person <= N; person++) {
                if (check[person] == 0) {
                    BfsCheck(person);
                    result++;
                }
            }
            StringBuilder sb = new StringBuilder();
            sb.append('#').append(tc).append(' ').append(result).append('\n');
            bw.write(sb.toString());
            bw.flush();

            sb.setLength(0);
        }
        br.close();
        bw.close();
    }

    private static void BfsCheck(int inputPerson) {
        check[inputPerson] = 1;

        Deque<Integer> queue = new LinkedList<>();
        queue.offerLast(inputPerson);

        while (!queue.isEmpty()) {
            int nowPerson = queue.pollFirst();
            for (int adjPerson : adjList[nowPerson]) {
                if (check[adjPerson] == 0) {
                    check[adjPerson] = 1;
                    queue.offerLast(adjPerson);
                }
            }
        }
        return;
    }

}