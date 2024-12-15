package ssafy.stack;

import java.util.Scanner;
import java.util.Stack;
import java.util.ArrayList;
import java.util.Arrays;

public class Swea4871 {

    public static int DFS(ArrayList<Integer>[] adjList, int S, int G, int V) {
        Stack<Integer> stack = new Stack<> ();  // 스택 생성
        int[] visited = new int[V + 1];         // 방문 정보 생성

        int now = S;
        visited[now] = 1; // 방문 표시
        while (true) {
            boolean flag = true;        // python for-else 구문과 비슷한 걸 모르겠어서 flag 사용
            for (int w:adjList[now]) {  // 해당 위치의 인접 정보 확인
                if (visited[w] == 0) {  // 방문하지 않았다면
                    flag = false;       // flag 표시
                    stack.push(now);    // 스택에 현위치 push
                    now = w;            // 방문
                    visited[now] = 1;   // 방문 표시
                    if (now == G) {     // 방문한 곳이 도착지라면
                        return 1;       // 1 반환
                    }
                    break;
                }
            }
            if (flag == true) {         // 만약 인접한 곳 중에서 방문할 수 있는 곳이 없었다면
                if (!stack.isEmpty()) { // 스택이 비어있지 않다면
                    now = stack.pop();  // 스택에서 pop
                } else {                // 스택이 비어있다면
                    return 0;           // 0 반환
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();
        for (int tc = 1; tc <= T; tc++) {
            int V = scanner.nextInt(); // V개 이내의 노드
            int E = scanner.nextInt(); // E 간선 개수

            // 인접 2차원 리스트 만들기
            ArrayList<Integer>[] adjList = new ArrayList[V + 1];
            for (int i = 0; i <= V; i++) {
                adjList[i] = new ArrayList<Integer>();
            }

            // 인접 리스트에 연결 정보 삽입
            for (int e = 0; e < E; e++) {
                int V1 = scanner.nextInt();
                int V2 = scanner.nextInt();
                adjList[V1].add(V2);
            }

            // 시작 도착점 지정
            int S = scanner.nextInt();
            int G = scanner.nextInt();

            // System.out.println(Arrays.deepToString(adjList));

            // DFS 호출 후 결과 출력
            int result = DFS(adjList, S, G, V);
            System.out.println("#" + tc + " " + result);
        }
        scanner.close();
    }
}
