package ssafy.array;

import java.util.Arrays;

public class SelectionSort1 {

    public static void main(String[] args) {
        int[] arr = {10, 64, 25, 11, 28, 77, 34};

        int[] newArr = selectionSort(arr);
        System.out.println("결과: " + Arrays.toString(newArr));
    }

    public static int[] selectionSort(int[] inputArr) {
        // cycle 횟수: 배열 길이 - 1
        for (int i = 0; i < inputArr.length - 1; i++) {
            int minIndex = i;   // 최소 값의 인덱스를 저장할 변수

            // 최소 값을 찾는 반복문
            for (int j = i + 1; j < inputArr.length; j++) {
                if (inputArr[minIndex] > inputArr[j]) { // 만약 현재 최소 값보다 더 작은 값이 있다면
                    minIndex = j;                       // 최소 값 인덱스를 수정해줌
                }
            }
            // i와 minIndex의 위치 swap
            int temp = inputArr[i];
            inputArr[i] = inputArr[minIndex];
            inputArr[minIndex] = temp;

            System.out.println(Arrays.toString(inputArr));
        }
        return inputArr;
    }
}
