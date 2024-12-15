package ssafy.array;

import java.util.Arrays;

public class BinarySearch1 {

    public static void main(String[] args) {
        int[] arr = {4, 9, 11, 23, 2, 19, 17};
        Arrays.sort(arr);
        // System.out.println(Arrays.toString(arr)); // [2, 4, 9, 11, 17, 19, 23]

        int targetKey = 2;

        int result = binarySearch(arr, targetKey);
        System.out.println(result);
    }

    public static int binarySearch(int[] inputArr, int key) {
        int start = 0;                  // 구간의 시작 index
        int end = inputArr.length - 1;  // 구간의 끝 index
        while (start <= end) {          // start와 end가 같아도 검색해야할 데이터는 하나가 남은 상태: 역전돼야 모든 데이터를 검사한 것
            int mid = (start + end) / 2;

            if (inputArr[mid] == key) {
                return mid;
            } else if (inputArr[mid] > key) {
                end = mid - 1;
            } else {                    // == (inputArr[mid] < key)
                start = mid + 1;
            }
        }
        return -1;
    }
}
