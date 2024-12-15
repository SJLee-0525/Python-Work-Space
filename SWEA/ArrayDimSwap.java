package ssafy.arraydim;

import java.util.Arrays;

public class ArrayDimSwap {

    public static void main(String[] args) {
        int[][] arr = {
                {1, 2, 3},
                {4, 5, 6},
                {7, 8, 9}
        };

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (i < j) {
                    int temp = arr[i][j];
                    arr[i][j] = arr[j][i];
                    arr[j][i] = temp;
                }
            }
        }
        System.out.println(Arrays.deepToString(arr));
        //[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    }
}