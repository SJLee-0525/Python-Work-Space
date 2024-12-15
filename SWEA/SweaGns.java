package ssafy.string;

import java.util.Scanner;
import java.util.Arrays;

public class SweaGns {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();
        scanner.nextLine();
        for (int t = 1; t <= T; t++) {
            String start = scanner.nextLine();
            String[] starts = start.split(" "); // [#1, 7041]

            int N = Integer.parseInt(starts[1]);      // 문자열 int로 바꾸기 : 7041

            String exPlanetInput = scanner.nextLine();
            String[] exoPlanetNums = exPlanetInput.split(" ");

            int[] earthNums = new int[N];
            for (int i = 0; i < N; i++) {
                if (exoPlanetNums[i].equals("ZRO")) {
                    earthNums[i] = 0;
                } else if (exoPlanetNums[i].equals("ONE")) {
                    earthNums[i] = 1;
                } else if (exoPlanetNums[i].equals("TWO")) {
                    earthNums[i] = 2;
                } else if (exoPlanetNums[i].equals("THR")) {
                    earthNums[i] = 3;
                } else if (exoPlanetNums[i].equals("FOR")) {
                    earthNums[i] = 4;
                } else if (exoPlanetNums[i].equals("FIV")) {
                    earthNums[i] = 5;
                } else if (exoPlanetNums[i].equals("SIX")) {
                    earthNums[i] = 6;
                } else if (exoPlanetNums[i].equals("SVN")) {
                    earthNums[i] = 7;
                } else if (exoPlanetNums[i].equals("EGT")) {
                    earthNums[i] = 8;
                } else if (exoPlanetNums[i].equals("NIN")) {
                    earthNums[i] = 9;
                }
            }

            // 카운팅 정렬 // [700, 716, 719, 734, 679, 737, 674, 654, 724, 704]
            int[] countingNums = new int[10];
            for (int earthNum : earthNums) {
                countingNums[earthNum] += 1;
            }

            // 누적합 구하기 // [700, 1416, 2135, 2869, 3548, 4285, 4959, 5613, 6337, 7041]
            for (byte i = 1; i < 10; i++) {
                countingNums[i] = countingNums[i - 1] + countingNums[i];
            }

            // 카운팅 정렬
            int[] earthNumsSort = new int[N];
            for (int i = N - 1; i >= 0; i--) {
                countingNums[earthNums[i]] -= 1;
                earthNumsSort[countingNums[earthNums[i]]] = earthNums[i];
            }

            // 출력
            System.out.println(starts[0]);
            for (int earthNum : earthNumsSort) {
                if (earthNum == 0) {
                    System.out.print("ZRO");
                } else if (earthNum == 1) {
                    System.out.print("ONE");
                } else if (earthNum == 2) {
                    System.out.print("TWO");
                } else if (earthNum == 3) {
                    System.out.print("THR");
                } else if (earthNum == 4) {
                    System.out.print("FOR");
                } else if (earthNum == 5) {
                    System.out.print("FIV");
                } else if (earthNum == 6) {
                    System.out.print("SIX");
                } else if (earthNum == 7) {
                    System.out.print("SVN");
                } else if (earthNum == 8) {
                    System.out.print("EGT");
                } else if (earthNum == 9) {
                    System.out.print("NIN");
                }
                System.out.print(" ");
            }
            System.out.println();
        }
    }
}
