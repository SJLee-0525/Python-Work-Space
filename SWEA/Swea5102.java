package ssafy.queue;

import java.util.Scanner;
import java.util.Deque;
import java.util.LinkedList;
import java.util.Arrays;
import java.util.ArrayList;

public class Swea5102 {

    public static ArrayList<Integer>[] adjList;

    public static int BFS(int S, int G, int V) {
        Deque<Integer> queue = new LinkedList<>();
        queue.offerLast(S);

        int[] visited = new int[V + 1];
        visited[S] = 1;

        while (!queue.isEmpty()) {
            int now = queue.pollFirst();
            for (int w : adjList[now]) {
                if (visited[w] == 0) {
                    visited[w] = visited[now] + 1;
                    if (w == G) {
                        return visited[w] - 1;
                    }
                    queue.offerLast(w);
                }
            }
        }
        return 0;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();
        for (int tc = 1; tc <= T; tc++) {
            int V = scanner.nextInt(); // 노드 개수
            int E = scanner.nextInt(); // 간선 개수

            // 2차원 인접 리스트 생성;
            adjList = new ArrayList[V + 1];
            for (int v = 0; v <= V; v++) {
                adjList[v] = new ArrayList<>();
            }

            // 인접 리스트에 인접 정보 추가
            for (int e = 0; e < E; e++) {
                int v1 = scanner.nextInt();
                int v2 = scanner.nextInt();
                adjList[v1].add(v2);
                adjList[v2].add(v1);
            }

            int S = scanner.nextInt(); // 시작 지점
            int G = scanner.nextInt(); // 도착 지점

            // System.out.println(Arrays.deepToString(adjList));

            System.out.println("#" + tc + " " + BFS(S, G, V));
        }
    }
}
