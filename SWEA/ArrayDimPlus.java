package ssafy.arraydim;

import java.util.Arrays;

public class ArrayDimPlus {

    public static void main(String[] args){
        int[][][] ThreeDimArrNull = new int[3][][]; // 초기화시 맨 앞의 요소 외에는 필수 값은 아님
        System.out.println(Arrays.deepToString(ThreeDimArrNull));
        // [null, null, null]

        int[][][] ThreeDimArr = new int[3][2][3];
        System.out.println(Arrays.deepToString(ThreeDimArr));
        // [[[0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0]]]
    }
}
