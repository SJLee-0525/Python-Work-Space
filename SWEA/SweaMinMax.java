package ssafy.array;

import java.util.Scanner;
import java.util.Arrays;

public class SweaMinMax {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();
        for (byte tc = 1; tc <= T; tc++) {
           int N = scanner.nextInt();
           int[] arr = new int[N];

           for (byte i = 0; i < N; i++) {
               arr[i] = scanner.nextInt();
           }

           int minIndex = 0;
           int maxIndex = 0;
           for (byte i = 0; i < N; i++) {
               if (arr[minIndex] > arr[i]) {
                   minIndex = i;
               } else if (arr[maxIndex] <= arr[i]) {
                   maxIndex = i;
               }
           }

           int result = maxIndex - minIndex;
           if (result < 0) {
               result *= -1;
           }
            System.out.println("#" + tc + " " + result);
        }
    }
}
