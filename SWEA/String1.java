package ssafy.string;

public class String1 {
    // 문자열의 초기화 2가지 방법
    public static void main(String[] args) {

        // 문자열 상수 풀에 1개만 저장을 하고 이후부터는 같은 주소로 할당
        String lStr1 = "Hello";
        String lStr2 = "Hello";

        // 힙 공간에 다른 주소를 가진 스트링을 생성
        String str1 = new String("Hello");
        String str2 = new String("Hello");

        // == 은 주소값을 비교하는 연산자
        System.out.println(lStr1 == lStr2); // true
        System.out.println(str1 == str2);   // false

        // 값을 비교하는 메서드
        System.out.println(lStr1.equals(lStr2));
        System.out.println(str1.equals(str2));

        //length(), replace(), split(), substring()
    }
}