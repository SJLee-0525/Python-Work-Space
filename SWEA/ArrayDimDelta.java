package ssafy.arraydim;

import java.util.Scanner;

public class ArrayDimDelta {

    // 델타배열 생성 (상하좌우)
    public static int[] di = {-1, 1, 0, 0};
    public static int[] dj = {0, 0, -1, 1};

    public static int[][] map = new int[5][5];

    public static int nowR = 2;
    public static int nowC = 2;

    public static void printMap() {
        for (int i = 0; i < map.length; i++) {
            for (int j = 0; j < map[i].length; j++) {
                if (i == nowR && j == nowC) {
                    System.out.print("X");
                } else {
                    System.out.print("O");
                }
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        printMap();
        while (true) {
            System.out.println("어디로 이동할까? 0: 상, 1: 하, 2: 좌, 3: 우");
            System.out.println("4를 입력하면 종료합니다.");
            int Direction = scanner.nextInt();

            if (Direction == 4) {
                break;
            }

            int mi = nowR + di[Direction];
            int mj = nowC + dj[Direction];

            if (0 <= mi && mi < 5 && 0 <= mj && mj < 5) {
                nowR = mi;
                nowC = mj;
                printMap();
            } else {
                System.out.println("배열 밖으로 벗어났습니다.");
                printMap();
            }
        }


    }
}
