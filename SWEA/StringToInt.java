package ssafy.string;

public class StringToInt {
    // Integer.parseInt()
    public static void main(String[] args) {

        String str1 = "12345";

        String str2 = str1 + 25;
        System.out.println(str2); // 1234525

        int int1 = Integer.parseInt(str1);
        System.out.println(int1); // 12345

        int sum = int1 + 15;
        System.out.println(sum);  // 12360
    }
}
