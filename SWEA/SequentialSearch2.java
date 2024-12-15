package ssafy.array;

import java.util.Arrays;

public class SequentialSearch2 {

    public static void main(String[] args) {
        int[] arr = {4, 9, 11, 23, 2, 19, 17};

        Arrays.sort(arr);   // 정렬하기
        System.out.println(Arrays.toString(arr)); // [2, 4, 9, 11, 17, 19, 23]
        int targetKey = 23;

        int result = searchWhileSort(arr, targetKey);
        System.out.println(result);
    }

    public static int searchForSort(int[] inputArr, int key) {
        for (int i = 0; i < inputArr.length; i++) {
            if (inputArr[i] == key) {
                return i;
            }
            if (inputArr[i] > key) {
                return -1;
            }
        }
        return -1;
    }

    public static int searchWhileSort(int[] inputArr, int key) {
        int i = 0;
        while (i < inputArr.length) {
            if (inputArr[i] == key) {
                return i;
            }
            if (inputArr[i] > key) {
                return -1;
            }
            i++;
        }
        return -1;
    }
}
