package ssafy.array;

import java.util.Arrays;

public class BubbleSort1 {
    // 버블 정렬 (오름차순)
    public static void main(String[] args) {

        int[] arr = {55, 7, 78, 12, 42};

        for (int i = arr.length - 1; i >= 1; i--) {    // i: 각 사이클마다 최대 데이터가 정렬될 위치
            for (int j = 0; j < i; j++) {              // j: 인접한 데이터와 비교할 index
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
            System.out.println(Arrays.toString(arr));
        }
    }
}
