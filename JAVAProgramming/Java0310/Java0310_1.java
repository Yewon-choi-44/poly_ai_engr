import java.util.Scanner;
public class Java0310_1 {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in); 
		//ctrl+space 사용으로 import
		
		int n = s.nextInt(); //선언된 객체변수 뒤 점 찍어서 함수를 불러주기
		String str = s.nextLine();
		
		System.out.println();
		System.out.println(n);
		System.out.println(str);
		
		s.close(); //마지막엔 닫아줘야함
	}
}
