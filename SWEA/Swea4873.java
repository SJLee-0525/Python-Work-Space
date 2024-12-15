package ssafy.stack;

import java.util.ArrayList;
import java.util.Scanner;

public class Swea4873 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();
        scanner.nextLine();

        for (byte tc = 1; tc <= T; tc++) {
            String inputStr = scanner.nextLine();

            ArrayList<Character> arr = new ArrayList<>();

            for (int i = 0; i < inputStr.length(); i++) {
                arr.add(inputStr.charAt(i));
            }

            boolean flag = true;
            while (flag == true) {
                flag = false;
                for (int i = 0; i < arr.size() - 1; i++) {
                    if (arr.get(i) == arr.get(i + 1)) {
                        arr.remove(i + 1);
                        arr.remove(i);
                        flag = true;
                    }
                }
            }
            System.out.println("#" + tc + " " + arr.size());
        }
        scanner.close();
    }
}
