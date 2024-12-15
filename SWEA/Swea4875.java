package ssafy.stack;

import java.util.Scanner;
import java.util.Arrays;
import java.util.Stack;


public class Swea4875 {

    // 델타 배열
    public static int[] di = {1, 0, -1, 0};
    public static int[] dj = {0, 1, 0, -1};

    // 시작지점 찾는 함수
    public static int[] findStart(int[][] maze, int N) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (maze[i][j] == 2) {
                    return new int[] {i, j};
                }
            }
        }
        return new int[] {-1, -1};
    }

    // DFS 탐색
    public static int DFS(int[][] maze, int N) {
        // 출발지 찾아서 반환받고 할당
        int[] start = findStart(maze, N);

        int i = start[0];
        int j = start[1];

        // 만약 출발 지점이 없으면 0 리턴
        if (i == -1 && j == -1) {
            return 0;
        }

        // DFS 사전 준비: Stack은 1차원 배열을 받도록 선언, visited는 2차원 배열로 선언
        Stack<int[]> stack = new Stack<>();
        int[][] visited = new int[N][N];
        visited[i][j] = 1; // 방문 표시

        // DFS
        while (true) {
            boolean flag = true;                    // 탐색 여부 확인용 flag
            for (int k = 0; k < 4; k++) {           // 델타 탐색
                int mi = i + di[k];                 // 임시로 이동 후
                int mj = j + dj[k];
                if (0 <= mi && mi < N               // 만약 인덱스 범위를 초과하지 않고
                    && 0 <= mj && mj < N
                    && maze[mi][mj] != 1            // 벽이 아니며
                    && visited[mi][mj] == 0) {      // 방문한 적이 없다면
                    flag = false;                   // 탐색했다고 표시 후
                    stack.push(new int[]{i, j});    // 스택에 현 위치 삽입
                    i = mi;                         // 이동
                    j = mj;
                    visited[i][j] = 1;              // 이동한 위치 방문 표시
                    if (maze[mi][mj] == 3) {        // 만약 도착지라면 1 리턴
                        return 1;
                    }
                    break;                          // for문 중단
                }
            }
            if (flag == true) {                     // 만약 for문 내에서 탐색한 적이 없었다면
                if (!stack.isEmpty()) {             // 만약 스택이 비어있지 않으면
                    int[] temp = stack.pop();       // 스택에서 pop해서 되돌아감
                    i = temp[0];
                    j = temp[1];
                } else {                            // 만약 비었다면
                    return 0;                       // 탐색할 수 있는 곳이 없으니 0 반환
                }
            }
        }
    }

    // MAIN
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt(); // 테케 개수
        for (int tc = 1; tc <= T; tc ++) {
            int N = scanner.nextInt();
            scanner.nextLine();

            // 미로 배열 선언 후 값 할당
            int[][] maze = new int[N][N];
            for (int i = 0; i < N; i++) {
                String inputStr = scanner.nextLine();
                for (int j = 0; j < N; j++) {
                    char inputChar = inputStr.charAt(j);
                    maze[i][j] = Character.getNumericValue(inputChar);
                }
            }
            // System.out.println(Arrays.deepToString(maze));

            // DFS 호출 후 결과 값 반환
            int result = DFS(maze, N);

            // 결과 출력
            System.out.println("#" + tc + " " + result);
        }
        scanner.close();
    }
}
