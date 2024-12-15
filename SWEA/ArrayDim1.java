package ssafy.arraydim;

import java.util.Arrays;

public class ArrayDim1 {

    public static void main(String[] args) {
        // 2차원 배열의 선언 및 초기화
        int[][] arr1 = {
                {1, 2, 3},
                {4, 5, 6},
                {7 ,8, 9}
        };

        // 정방향 행 우선순회 하면서 초기화
        int num = 1;
        int[][] arr2 = new int[3][3];
        for (int r = 0; r < arr2.length; r++) {
            for (int c = 0; c < arr2[r].length; c++) {
                arr2[r][c] = num++;
            }
        }
        // 2차원 배열 출력하기
        System.out.println(Arrays.deepToString(arr2));
        // [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        // 2차원 배열 역방향 출력
        for (int r = 0; r < arr2.length; r++) {
            for (int c = arr2[r].length - 1; c >= 0; c--) {
                System.out.print(arr2[r][c] + " ");
            }
            System.out.println();
        }
        /*
        3 2 1
        6 5 4
        9 8 7
         */
    }
}
