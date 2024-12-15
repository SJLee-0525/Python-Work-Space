package ssafy.stack;

public class Stack5Fibo {

    public static void main(String[] args) {
        int N = 150;

//        int result = fibonacci(N);
//        System.out.println("재귀: " + result);

        int result2 = fibonacci2(N);
        System.out.println("반복: " + result2);

        int result3 = memoFibonacci(N);
        System.out.println("메모: " + result3);
    }

    // 재귀를 이용한 피보나치 수열
    static int fibonacci(int N) {
        if (N <= 1) {
            return N;
        }
        return fibonacci(N - 1) + fibonacci(N - 2);
    }

    // 반복문
    static int fibonacci2(int N) {
        int[] memo = new int[N + 1];
        memo[0] = 0;
        memo[1] = 1;

        for (int i = 2; i <= N; i++) {
            memo[i] = memo[i - 1] + memo[i - 2];
        }
        return memo[N];
    }

    // 메모이제이션

    static int[] memo = new int[500];

    static {
        memo[0] = 0;
        memo[1] = 1;
    }

    static int memoFibonacci(int N) {
        if (N <= 1) {
            return N;
        }
        if (memo[N] > 0) {
            return memo[N];
        }

        return memo[N] = memoFibonacci(N - 1) + memoFibonacci(N - 2);
    }
}
