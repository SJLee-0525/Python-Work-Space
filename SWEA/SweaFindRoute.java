package ssafy.stack;

import java.util.Scanner;
import java.util.Stack;
import java.util.Arrays;
import java.util.ArrayList;

public class SweaFindRoute {

    public static int DFS(ArrayList<Integer>[] adjList) {
        int[] visited = new int[100];
        Stack<Integer> stack = new Stack<>();

        int now = 0;    // 출발점은 0
        visited[0] = 1; // 출발 표시
        while (true) {
            boolean flag = true;
            for (int w : adjList[now]) { // 해당 위치의 인접 정점 순회
                if (visited[w] == 0) {   // 방문 안 한 곳이 있다면
                    flag = false;        // flag 표시
                    stack.push(now);     // 현위치 스택에 push
                    now = w;             // 이동
                    visited[now] = 1;    // 방문 표시
                    if (now == 99) {     // 희망 도착점은 99
                        return 1;        // 희망 지점에 도착하면 1 반환
                    }
                    break;
                }
            }
            if (flag) {                 // for문 내에서 방문한 적이 없으면
                if (!stack.isEmpty()) { // 스택이 비어있지 않으면
                    now = stack.pop();  // 스택에서 뽑아서 사용
                } else {                // 비어있으면
                    return 0;           // 0 반환
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        // 출발점은 0, 도착점은 99, 정점 개수는 최대 100, 단방향 노드
        for (byte t = 1; t <= 10; t++) {
            int tc = scanner.nextInt();
            int E = scanner.nextInt();

            // 2차원 인접 리스트 만들기
            ArrayList<Integer>[] adjList = new ArrayList[100];
            for (int i = 0; i < 100; i++) {
                adjList[i] = new ArrayList<Integer>();
            }

            // 인접 리스트에 값 넣기
            for (int e = 0; e < E; e++) {
                int V1 = scanner.nextInt();
                int V2 = scanner.nextInt();
                adjList[V1].add(V2);
            }
            // System.out.println(Arrays.deepToString(adjList));

            // DFS 호출
            int result = DFS(adjList);
            System.out.println("#" + tc + " " + result);

        }
        scanner.close();
    }
}
