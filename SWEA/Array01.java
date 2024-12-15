package ssafy.array;

public class Array01 {

    public static void main(String[] args) {
        int[] arr = {3, 4, 5, 1, 2, 6};

        System.out.println("정방향 순회");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]);
            if (i < arr.length - 1) {
                System.out.print(", ");
            }
        }

        System.out.println();
        System.out.println("역방향 순회");
        for (int i = arr.length - 1; i >= 0; i--) {
            System.out.print(arr[i]);
            if (i != 0) {
                System.out.print(", ");
            }
        }
    }
}
