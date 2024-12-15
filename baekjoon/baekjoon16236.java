package baekjoon;

import java.io.BufferedWriter;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.Arrays;
import java.util.Deque;
import java.util.LinkedList;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

public class baekjoon16236 {

    private static int N, babyShark;

    private static int[] di = {-1, 0, 1, 0};
    private static int[] dj = {0, -1, 0, 1};

    private static int[][] space, visited;

    private static Deque<int[]> queue = new LinkedList<>();
    private static ArrayList<int[]> possible = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(br.readLine()); // 공간 크기
        space = new int[N][N];

        int[] babySharkLocation = new int[2];
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                space[i][j] = Integer.parseInt(st.nextToken());
                if (space[i][j] == 9) {
                    babySharkLocation[0] = i;
                    babySharkLocation[1] = j;
                }
            }
        }

        babyShark = 2;
        visited = new int[N][N];
        int time = 0, eatCnt = 0; // 경과 시간, 먹은 횟수
        int i = babySharkLocation[0], j = babySharkLocation[1];
        while (true) {
            bfs(i, j); // bfs 탐색을 통해 최단 거리로 먹을 수 있는 물고기 목록을 생성 (possible)

            // 만약 possible이 비어있으면: 먹을 수 있는 물고기가 없으므로 중단 (엄마 호출)
            if (possible.isEmpty()) break;

            // 거리가 가까운 물고기가 여럿이라면, 그 중 가장 위에 있는 물고기가 되도록: i 값이 작도록
            // i 값이 작은 좌표를 가진 물고기가 여럿이라면, 그중 가장 왼쪽에 있는 물고기가 되도록: j 값이 작도록 정렬
            Collections.sort(possible, new Comparator<int[]>() {
                @Override
                public int compare(int[] a, int[] b) {
                    // 두 번째 원소를 비교
                    if (a[1] != b[1]) {
                        return Integer.compare(a[1], b[1]);
                    }
                    // 세 번째 원소를 비교
                    return Integer.compare(a[2], b[2]);
                }
            });

            space[i][j] = 0;            // 현 위치는 0으로
            time += possible.get(0)[0]; // bfs 경로 길이만큼 시간 추가
            i = possible.get(0)[1];     // i 값 할당
            j = possible.get(0)[2];     // j 값 할당
            space[i][j] = 9;            // 새로운 좌표로 이동

            eatCnt++;                   // 이동했다는 건, 물고기를 먹었다는 뜻: 먹은 횟수 카운트
            if (eatCnt == babyShark) {  // 만약 아기 상어의 크기만큼 물고기를 먹었다면
                babyShark++;            // 아기 상어 성장
                eatCnt = 0;             // 먹은 카운트 초기화
            }
        }
        sb.append(time);
        bw.write(sb.toString());
        bw.flush();
        sb.setLength(0);

        bw.close();
        br.close();
    }

    private static void bfs(int si, int sj) {
        possible.clear();   // bfs 탐색 시작 전 possible Arraylist clear
        clearVisited();     // visited 배열 초기화

        visited[si][sj] = 1;                // 시작점 방문 표시
        queue.offerLast(new int[]{si, sj}); // queue에 좌표 삽입

        int i, j, mi, mj;
        int minDistance = 0;                // 최단 거리 발견 여부 확인과 최단 거리 길이 확인용 변수
        while (!queue.isEmpty()) {          // bfs 탐색
            int[] now = queue.pollFirst();
            i = now[0];
            j = now[1];
            if (minDistance != 0) { // 만약 최단 거리 발견을 한 적이 있다면
                // 해당 좌표의 visited 값이 최단 거리보다 크다면: 탐색할 필요 없음. 어차피 더 멀기 때문
                if (visited[i][j] > minDistance) continue;
            }

            // 델타 순회
            for (int k = 0; k < 4; k++) {
                mi = i + di[k];
                mj = j + dj[k];
                // 범위를 벗어나지 않고, 이동할 수 있으며 (자기랑 크기가 같은 물고기도 가능), 방문한 적이 없다면
                if (0 <= mi && mi < N && 0 <= mj && mj < N &&
                0 <= space[mi][mj] && space[mi][mj] <= babyShark && visited[mi][mj] == 0) {
                    // 만약 먹을 수 있는 물고기를 발견했는데 (0이 아니며, 자기보다 작은 물고기)
                    if (0 < space[mi][mj] && space[mi][mj] < babyShark) {
                        // 만약 최단 거리 발견을 한 적이 없다면 최단 거리 기록 후
                        // 최단 거리로 먹을 수 있는 물고기 목록에 추가 (최단 거리(시간), 좌표)
                        if (minDistance == 0) minDistance = visited[i][j];
                        possible.add(new int[] {visited[i][j], mi, mj});
                    }
                    // 방문 표시 및 queue에 좌표 삽입
                    visited[mi][mj] = visited[i][j] + 1;
                    queue.offerLast(new int[] {mi, mj});
                }
            }
        }
    }

    private static void clearVisited() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                visited[i][j] = 0;
            }
        }
    }
}
