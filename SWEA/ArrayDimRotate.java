package ssafy.arraydim;

import java.util.Arrays;

public class ArrayDimRotate {

    public static void main(String[] args) {
        int[][] arr = {
                {1, 2, 3},
                {4, 5, 6},
                {7, 8, 9}
        };

        int[][] rotateArr = new int[3][3];

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                rotateArr[i][j] = arr[2 - j][i];
            }
        }
        System.out.println(Arrays.deepToString(rotateArr));
        //[[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        /*
        [7, 4, 1]
        [8, 5, 2]
        [9, 6, 3]
         */
    }
}