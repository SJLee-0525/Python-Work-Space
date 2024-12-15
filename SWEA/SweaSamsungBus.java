package ssafy.array;

import java.util.Scanner;
import java.util.Arrays;

public class SweaSamsungBus {

    public static int[] stations;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        byte T = scanner.nextByte();
        for (byte tc = 1; tc <= T; tc++) {
            stations = new int[5001];
            short N = scanner.nextShort();
            for (short n = 0; n < N; n++) {
                short A = scanner.nextShort();
                short B = scanner.nextShort();
                for (short stop = A; stop <= B; stop++) {
                    stations[stop]++;
                }
            }
            System.out.print("#" + tc);
            short P = scanner.nextShort();
            for (short p = 0; p < P; p++) {
                short i = scanner.nextShort();
                System.out.print(" " + stations[i]);
            }
            System.out.println();
        }
        scanner.close();
    }
}
