package ssafy.array;

import java.util.Scanner;
import java.util.Arrays;

public class SweaSeqOne {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();
        for (int tc = 1; tc <= T; tc++) {
            int N = scanner.nextInt();
            scanner.nextLine();

            String inputStrNums = scanner.nextLine();
            int[] inputNums = new int[N];

            for (int s = 0; s < N; s++) {
                inputNums[s] = Character.getNumericValue(inputStrNums.charAt(s));
            }

            int result = 0;
            int temp = 0;
            for (int i = 0; i < N; i++) {
                if (inputNums[i] == 0) {
                    if (result < temp) {
                        result = temp;
                    }
                    temp = 0;
                } else if (inputNums[i] == 1) {
                    temp += 1;
                }
            }
            if (result < temp) {
                result = temp;
            }
            System.out.println("#" + tc + " " + result);
        }
    }
}
