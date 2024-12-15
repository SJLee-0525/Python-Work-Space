package ssafy.arraydim;

import java.util.Scanner;
import java.util.Arrays;

public class SweaSnailNum {

    // 델타 우 하 좌 상
    public static int[] di = {0, 1, 0, -1};
    public static int[] dj = {1, 0, -1, 0};

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();
        for (int tc = 1; tc <= T; tc++) {
            int N = scanner.nextInt();
            int[][] resultArr = new int[N][N];

            int num = 0;
            int i = 0;
            int j = -1;
            int k = 0;
            while (num < N * N) {
                int mi = i + di[k];
                int mj = j + dj[k];
                if (0 <= mi && mi < N && 0 <= mj && mj < N && resultArr[mi][mj] == 0) {
                    resultArr[mi][mj] = ++num;
                    i = mi;
                    j = mj;
                } else {
                    k = (k + 1) % 4;
                }
            }
            // System.out.println(Arrays.deepToString(resultArr)); // [[1, 2, 3], [8, 9, 4], [7, 6, 5]]

            System.out.println("#" + tc);
            for (int dim1 = 0; dim1 < N; dim1++) {
                for (int dim2 = 0; dim2 < N; dim2++) {
                    System.out.print(resultArr[dim1][dim2] + " ");
                }
                System.out.println();
            }
        }
    }
}