package ssafy.string;

import java.util.Scanner;
import java.util.Arrays;

public class SweaCutStick {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();
        scanner.nextLine();
        for (int tc = 1; tc <= T; tc++) {
            String inputTable = scanner.nextLine();

            int cutCnt = 0;
            int stickCnt = 0;
            for (int c = 0; c < inputTable.length(); c++) {
                if (inputTable.charAt(c) == '(') {
                    stickCnt++;
                } else {
                    if (inputTable.charAt(c - 1) == '(') { // 레이저
                        stickCnt--;
                        cutCnt += stickCnt;
                    } else {
                        stickCnt--;
                        cutCnt++;
                    }
                }
            }
            System.out.println("#" + tc + " " + cutCnt);
        }
    }
}
