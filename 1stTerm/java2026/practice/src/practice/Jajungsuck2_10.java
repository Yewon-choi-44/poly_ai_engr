package practice;

import java.util.Scanner;

public class Jajungsuck2_10 {
	public static void main(String[] args) {
//		#Ex2_10
		Scanner sc = new Scanner(System.in);
		System.out.print("두 자리 정수를 하나 입력해주세요.> ");
		String input = sc.nextLine();
		int num = Integer.parseInt(input);
		
		System.out.println("입력내용 : " + input);
		System.out.printf("num = %d%n", num);
		
		sc.close();
		
//		#Ex2_11
		short sMin = -32768, sMax = 32767;
		char cMin = 0, cMax = 65535;
		
		System.out.println("sMin = " + sMin);
		System.out.println("sMin - 1 = " + (short)(sMin-1));
		System.out.println("sMax = " + sMax);
		System.out.println("sMin + 1 = " + (short)(sMin+1));
		System.out.println("cMin = " + (int)(cMin));
		System.out.println("cMin - 1 = " + (int)--cMin);
		System.out.println("cMax = " + (int)cMax);
		System.out.println("cMax + 1= " + (int)++cMax);
		
		
//		#Ex2_12
		String str = "3";
		
		System.out.println(str.charAt(0)-'0');				// 문자열을 문자로 변환 - charAt(0)을 사용
		System.out.println('3' - '0' + 1);					// 문자를 숫자로 변환 - 문자에서 '0'을 뺀다
		System.out.println(Integer.parseInt("3") + 1);		// 문자열을 숫자로 변환 - Integer.parseInt() 또는 Double.parseDouble()
		System.out.println("3" + 1);
		System.out.println((char)(3 + '0'));			
		
	}
}
