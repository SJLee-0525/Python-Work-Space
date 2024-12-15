package ssafy.array;

public class SequentialSearch1 {

    public static void main(String[] args) {
        int[] arr = {4, 9, 11, 23, 2, 19, 17};
        int targetKey = 19;

        int result = searchWhileNoSort(arr, targetKey);
        System.out.println(result);
    }

    // for문 사용
    public static int searchForNoSort(int[] inputArr, int key) {
        for (int i = 0; i < inputArr.length; i++) {
            if (inputArr[i] == key) {
                return i;   // 찾는 대상이 있을 경우 index를 리턴
            }
        }
        return -1;          // 찾는 대상이 없을 경우 -1 return;
    }

    // while문 사용
    public static int searchWhileNoSort(int[] inputArr, int key) {
        int i = 0;
        while(i < inputArr.length) {
            if (inputArr[i] == key) {
                return i;
            }
            i++;
        }
        return -1;
    }
}
