package ssafy.string;

public class StringPattern {

    public static void main(String[] args) {
        String text = "This iss a book";
        String pattern = "iss";

        int result = bruteforce(text, pattern);
        System.out.println(result);
    }

    public static int bruteforce(String text, String pattern) {
        int ti = 0;
        int pi = 0;
        while (ti < text.length() && pi < pattern.length()) {
            if (text.charAt(ti) != pattern.charAt(pi)) {
                ti -= pi;
                pi = -1;
            }
            ti += 1;
            pi += 1;
        }
        if (pi == pattern.length()) {
            return (ti - pi);
        } else {
            return -1;
        }
    }
}
