package ssafy.stack;

public class Stack4Factorial {

    public static void main(String[] args) {
        int N = 10;

        int result1 = factorial(N);
        int result2 = factorial2(N);

        System.out.println("for 팩토리얼: " + result1);
        System.out.println("재귀 팩토리얼: " + result2);
    }

    // for문 이용한 factorial
    static int factorial(int N) {
        // 1부터 n까의 곱
        int result = 1;
        for (int i = 1; i <= N; i++) {
            result *= i;
        }
        return result;
    }

    // 재귀를 이용한 factorial
    static int factorial2(int N) {
        if (N == 1) {
            return 1;
        }
        return N * factorial2(N - 1);
    }
}
