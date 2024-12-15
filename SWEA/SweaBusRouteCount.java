package ssafy.array;

import java.util.Scanner;
import java.util.Arrays;

public class SweaBusRouteCount {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();
        for (int tc = 1; tc <= T; tc++) {
            int N = scanner.nextInt();
            scanner.nextLine();

            int[] stationList = new int[5000];
            for (int n = 0; n < N; n++) {
                String[] promptStrs = scanner.nextLine().split(" ");

                for (int station = Integer.parseInt(promptStrs[0]); station <= Integer.parseInt(promptStrs[1]); station++) {
                    stationList[station - 1] += 1;
                }
            }

            int promptCnt = scanner.nextInt();
            System.out.print("#" + tc);
            for (int c = 0; c < promptCnt; c++) {
                int prompt = scanner.nextInt();
                System.out.print(" " + stationList[prompt - 1]);
            }
            System.out.println();
        }
    }
}
