package ssafy.testa;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.Deque;
import java.util.List;
import java.util.LinkedList;
import java.util.Objects;
import java.util.StringTokenizer;

public class SweaUniqueMagnetic {

    private static int[] promptList;
    private static Deque<Integer>[] gearList;

    private static void promptCal(int startTarget, int startDir) {
        List<Integer> targetGear;
        List<Integer> nextGear;

        promptList = new int[4];
        promptList[startTarget] = startDir;

        int nowPrompt = startDir;
        int now = startTarget;
        int next = startTarget + 1;
        while (next < 4) {
            targetGear = new LinkedList<>(gearList[now]);
            nextGear = new LinkedList<>(gearList[next]);
            if (Objects.equals(targetGear.get(2), nextGear.get(6))) {
                break;
            } else {
                nowPrompt *= -1;
                promptList[next] = nowPrompt;
                now++;
                next++;
            }
        }
        nowPrompt = startDir;
        now = startTarget;
        next = startTarget - 1;
        while (next >= 0) {
            targetGear = new LinkedList<>(gearList[now]);
            nextGear = new LinkedList<>(gearList[next]);
            if (Objects.equals(targetGear.get(6), nextGear.get(2))) {
                break;
            } else {
                nowPrompt *= -1;
                promptList[next] = nowPrompt;
                now--;
                next--;
            }
        }
//        System.out.println(Arrays.toString(promptList));
        rotateGear(promptList);
    }

    private static void rotateGear(int[] inputPromptList) {
        for (int tar = 0; tar < 4; tar++) {
            // 시계 방향: 뒤에 거가 앞으로
            if (inputPromptList[tar] == 1) {
                gearList[tar].offerFirst(gearList[tar].pollLast());
            } else if (inputPromptList[tar] == -1) {
                gearList[tar].offerLast(gearList[tar].pollFirst());
            }
//            System.out.println(gearList[tar]);
        }
    }

    private static int calScore() {
        int result = 0;
        List<Integer> targetGear;
        for (int std = 0; std < 4; std++) {
            // N: 0, S: 1
            targetGear = new LinkedList<>(gearList[std]);
            if (targetGear.get(0) == 1) {
                result += (int) Math.pow(2, std);
            }
        }
        return result;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {
            int K = Integer.parseInt(br.readLine());

            gearList = new Deque[4];

            for (int g = 0; g < 4; g++) {
                gearList[g] = new LinkedList<>();
                st = new StringTokenizer(br.readLine());
                for (int s = 0; s < 8; s++) {
                    gearList[g].offerLast(Integer.parseInt(st.nextToken()));
                }
//                System.out.println(gearList[g]);
            }

            for (int k = 0; k < K; k++) {
                st = new StringTokenizer(br.readLine());
                int target = Integer.parseInt(st.nextToken()) - 1;
                int dir = Integer.parseInt(st.nextToken());
                promptCal(target, dir);
            }

            int result = calScore();

//            for (int g = 0; g < 4; g++) {
//                System.out.println(gearList[g]);
//            }

            StringBuilder sb = new StringBuilder();
            sb.append('#').append(tc).append(' ').append(result).append('\n');
            bw.write(sb.toString());
            bw.flush();
            sb.setLength(0);
        }
        br.close();
        bw.close();
    }
}
