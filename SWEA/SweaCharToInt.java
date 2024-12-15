package ssafy.string;

import java.util.Scanner;

public class SweaCharToInt {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String input = scanner.nextLine();
        for (int i = 0; i < input.length(); i++) {
            System.out.print(((int) input.charAt(i) - 64) + " ");
        }
        System.out.println();
    }
}
