package ssafy.array;

import java.util.Arrays;

public class CountingSort1 {

    public static void main(String[] args) {
        int[] arr = {0, 4, 1, 3, 1, 2, 4, 1};
        int maxValue = findMaxValue(arr);                   // 4

        int[] countingArr = counting(arr, maxValue);        // [1, 4, 5, 6, 8]

        int[] resultArr = countingSort(arr, countingArr);
        System.out.println(Arrays.toString(resultArr));     // [0, 1, 1, 1, 2, 3, 4, 4]
    }

    public static int findMaxValue(int[] inputArr) {
        int maxVal = inputArr[0];
        for (int i = 1; i < inputArr.length; i++) {
            if (maxVal < inputArr[i]) {
                maxVal = inputArr[i];
            }
        }
        return maxVal;
    }

    public static int[] counting(int[] inputArr, int maxValue) {
        int[] countingArr = new int[maxValue + 1];   // [0, 0, 0, 0, 0]
        for (int i = 0; i < inputArr.length; i++) {
            countingArr[inputArr[i]] += 1;
        }
        // [1, 3, 1, 1, 2]

        for (int i = 1; i < countingArr.length; i++) {
            countingArr[i] += countingArr[i - 1];
        }
        return countingArr;
        // [1, 4, 5, 6, 8]
    }

    public static int[] countingSort(int[] inputArr, int[] countingArr) {
        int[] resultArr = new int[inputArr.length];     // [0, 0, 0, 0, 0, 0, 0, 0]

        for (int i = inputArr.length - 1; i >= 0; i--) {
            countingArr[inputArr[i]] -= 1;
            resultArr[countingArr[inputArr[i]]] = inputArr[i];

            System.out.println(Arrays.toString(resultArr));
        }
        return resultArr;
    }
}

    /*
    [0, 0, 0, 1, 0, 0, 0, 0]
    [0, 0, 0, 1, 0, 0, 0, 4]
    [0, 0, 0, 1, 2, 0, 0, 4]
    [0, 0, 1, 1, 2, 0, 0, 4]
    [0, 0, 1, 1, 2, 3, 0, 4]
    [0, 1, 1, 1, 2, 3, 0, 4]
    [0, 1, 1, 1, 2, 3, 4, 4]
    [0, 1, 1, 1, 2, 3, 4, 4]
     */