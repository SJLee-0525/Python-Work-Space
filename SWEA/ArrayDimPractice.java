package ssafy.arraydim;

import java.util.Arrays;

public class ArrayDimPractice {

    public static int[] di = {1, 0, -1, 0};
    public static int[] dj = {0, 1, 0, -1};

    public static void main(String[] args) {
        int[][] arr = new int [5][5];
        int num = 0;
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                arr[i][j] = ++num;
            }
        }
        System.out.println(Arrays.deepToString(arr));
        // [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]

        int[][] resultArr = new int [5][5];
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                int tempResult = 0;
                for (int k = 0; k < 4; k++) {
                    int mi = i + di[k];
                    int mj = j + dj[k];
                    if (0 <= mi && mi < 5 && 0 <= mj && mj < 5) {
                        tempResult += Math.abs(arr[i][j] - arr[mi][mj]); // 절대값 매서드
                    }
                }
                resultArr[i][j] = tempResult;
            }
        }
        System.out.println(Arrays.deepToString(resultArr));
        // [[6, 7, 7, 7, 6], [11, 12, 12, 12, 11], [11, 12, 12, 12, 11], [11, 12, 12, 12, 11], [6, 7, 7, 7, 6]]
    }
}
