package ssafy.string;

import java.util.Arrays;

public class StringSwap1 {

    public static void main(String[] args) {

        String str = new String("Algorithm");

        char[] charArr = new char[str.length()];

        for (int i = 0; i < str.length(); i++) {
            charArr[i] = str.charAt(i);
        }
        System.out.println(Arrays.toString(charArr)); // [A, l, g, o, r, i, t, h, m]

        // 새로운 배열을 만들어서 뒤집기

        char[] nextArr = new char[charArr.length];

        for (int i = 0; i < nextArr.length; i++) {
            nextArr[i] = charArr[charArr.length - i - 1];
        }
        System.out.println(Arrays.toString(nextArr)); // [m, h, t, i, r, o, g, l, A]

        // 원본 배열에서 Swap : 배열을 새로 만들 필요도 없고, 반복도 절반만 수행하면 됨
        char[] nextArr2 = str.toCharArray(); // 스트링에서 바로 리스트로 뽑아오는 메서드
        System.out.println(Arrays.toString((nextArr2))); // [A, l, g, o, r, i, t, h, m]

        for (int i = 0; i < nextArr2.length / 2; i++) {
            char temp = nextArr2[i];
            nextArr2[i] = nextArr2[nextArr2.length - 1 - i];
            nextArr2[nextArr2.length - 1 - i] = temp;
        }
        System.out.println(Arrays.toString(nextArr2)); // [m, h, t, i, r, o, g, l, A]

        // 문자열 합치기
        String nextStr2 = "";
        for (int i = 0; i < nextArr2.length; i++) {
            nextStr2 += nextArr2[i];
        }
        System.out.println(nextStr2); // mhtiroglA
    }
}
