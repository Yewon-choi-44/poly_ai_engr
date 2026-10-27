package practice;
public class Jajungsuck2_1 {
	public static void main(String[] args) {
//		#Ex2_1
		System.out.println("Hello World"); //화면에 문자열을 출력하고 줄바꿈한다.
		System.out.print("Hello"); // 화면에 문자열을 출력하고 줄바꿈 안한다.
		System.out.println("world");
		
//		#Ex2_2
		System.out.println("Hello world");
		System.out.print("3+5=");
		System.out.println(3+5);
		
//		#EX2_3
		System.out.println(5+3);
		System.out.println(5-2);
		System.out.println(5*3);
		System.out.println(5/3);
	
//		#Ex2_4
		int x = 5;
		System.out.println(x);
		
		x = 10;
		System.out.println(x);
		
//		#Ex2_5
		int xx = 10;
		int y = 5;
		System.out.println(xx+y);
		System.out.println(xx-y);
		System.out.println(xx*y);
		System.out.println(xx/y);
		
//		#Ex2_6
		x = 100;
		double pi = 3.14;
		char ch = 'a';
		String str = "abc";
		
		System.out.println(x);
		System.out.println(pi);
		System.out.println(ch);
		System.out.println(str);
		
//		#Ex2_7
		String name = "Ja"+"va";
		String str1 = name + 8.0;
		
		System.out.println(name);
		System.out.println(str1);
		System.out.println(7 + " ");
		System.out.println(" " + 7);
		System.out.println(7 + "");
		System.out.println("" + 7);
		System.out.println("" + "");
		System.out.println(7 + 7 + "");
		System.out.println("" + 7 + 7);
		
		
//		#Ex2_8
		x=10; y=5;
		System.out.println("x=" + x);
		System.out.println("y=" + y);
		
		int tmp = x;
		x = y;
		y = tmp;
		
		System.out.println("x=" + x);
		System.out.println("y=" + y);

		
//		#Ex2_9
		String url = "www.codechobo.com";
		float f1 = .10f;
		float f2  = 1e1f;
		float f3 = 3.14e3f;
		double d =1.23456789;
		
		System.out.printf("f1 = %f , %e , %g%n" , f1, f1, f1);
		System.out.printf("f2 = %f , %e , %g%n" , f2, f2, f2);
		System.out.printf("f2 = %f , %e , %g%n" , f3, f3, f3);
		System.out.printf("d = %f%n" , d);
		System.out.printf("d = %14.10f%n" , d); 	// 전체 14자리 중 소수점 아래 10자리
		System.out.printf("[12345678901234567890]%n");
		System.out.printf("[%s]%n", url); 			// 문자열의 길이만큼 출력공간을 확보.
		System.out.printf("[%20s]%n", url); 		// 최소 20글자 출력공간 확보.(우측정렬)
		System.out.printf("[%-20s]%n", url);		// 최소 20글자 출력공간 확보.(좌측정렬)
		System.out.printf("[%.8s]%n", url); 		// 왼쪽에서 8글자만 출력.
		// %전체자리.소수점아래자리f
		
	}
}
