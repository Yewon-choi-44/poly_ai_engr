public class Hello {
	public static void main(String[] args) {
		int i = 20; //정수형 변수 선언
		int s; //s는 변수 선언 했으나 초깃값이 없는 상태
		char a; //문자형 변수
		String b; //문자열 변수
		
		//s = sum(i,10);
		s = i+10;
		a = '?'; //캐릭터형은 '' <를 사용해야 사용 가능
		b= "Hello";
		
		System.out.println(a); //ln을 사용하면 줄바꿈
		System.out.println(b); //""는 문자열.
		System.out.println(s);
	}

	private static int sum(int i, int j) {
		return i + j;
	}
}