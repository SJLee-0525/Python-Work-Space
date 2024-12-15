package ssafy.array;

import java.util.Scanner;

public class SweaFishBread {

    public static int[] persons;
    public static int[] personTimeTable;
    public static int[] breadTimeTable;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();
        for (int tc = 1; tc <= T; tc++) {
            int N = scanner.nextInt(); // N명의 사람
            int M = scanner.nextInt(); // M초의 시간
            int K = scanner.nextInt(); // K개의 붕어빵

            persons = new int[N];

            int maxTime = 0;
            for (int n = 0; n < N; n++) {
                persons[n] = scanner.nextInt();
                if (maxTime < persons[n]) {
                    maxTime = persons[n];
                }
            }

            personTimeTable = new int[maxTime + 1];
            for (int person:persons) {
                personTimeTable[person] += 1;
            }
            for (int p = 0; p < maxTime; p++) {
                personTimeTable[p + 1] += personTimeTable[p];
            }

            breadTimeTable = new int[maxTime + 1];
            for (int time = M; time <= maxTime; time += M) {
                breadTimeTable[time] += K;
            }
            for (int b = 0; b < maxTime; b++) {
                breadTimeTable[b + 1] += breadTimeTable[b];
            }

            boolean canDo = true;
            for (int t = 0; t <= maxTime; t++) {
                if (personTimeTable[t] > breadTimeTable[t]) {
                    canDo = false;
                }
            }

            if (canDo == true) {
                System.out.println("#" + tc + " Possible");
            } else {
                System.out.println("#" + tc + " Impossible");
            }
        }
        scanner.close();
    }
}