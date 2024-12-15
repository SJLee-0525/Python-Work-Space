package ssafy.string;

import java.util.Scanner;

public class SweaFastTyping {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();
        scanner.nextLine();
        for (int tc = 1; tc <= T; tc++) {
            String strInput = scanner.nextLine();
            String[] inputArr = strInput.split(" ");

            String pattern = inputArr[0];
            String target = inputArr[1];

            int result = check(pattern, target);
            System.out.println("#" + tc + " " + result);
        }
        scanner.close();
    }

    public static int check(String pattern, String target) {
        int cnt = 0;
        int pi = 0;
        int ti = 0;
        while (pi < pattern.length() && ti < target.length()) {
            // System.out.println(pattern.charAt(pi) + " / " + target.charAt(ti));
            if (pattern.charAt(pi) != target.charAt(ti)) {
                pi -= ti;
                ti = -1;
                cnt++;
            }
            pi++;
            ti++;
            if (pi == pattern.length() && ti < target.length()) {
                cnt += ti;
            }
            if (ti == target.length()) {
                cnt++;
                ti = 0;
            }

        }
        return cnt;
    }
}
