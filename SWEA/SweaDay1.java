package ssafy.array;

import java.util.Scanner;

public class SweaDay1 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        for (int tc = 1; tc <= 10; tc++) {
            int N = scanner.nextInt(); // 건물 개수
            int[] skyLine = new int[N];
            for (int n = 0; n < N; n++) {
                skyLine[n] = scanner.nextInt();
            }

            int view = 0;
            for (int building = 2; building < N - 2; building++) {
                int highestNearby = 0;
                for (int nearby = building - 2; nearby <= building + 2; nearby++) {
                    if (nearby == building) {
                        continue;
                    }
                    if (highestNearby < skyLine[nearby]) {
                        highestNearby = skyLine[nearby];
                    }
                }
                int temp = skyLine[building] - highestNearby;
                if (temp > 0) {
                    view += temp;
                }
            }
            System.out.println("#" + tc + " " + view);
        }
    }
}
