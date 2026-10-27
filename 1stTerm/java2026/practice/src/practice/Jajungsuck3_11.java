package practice;

import java.util.Scanner;

public class Jajungsuck3_11 {
	public static void main(String[] args) {
//	Ex3_11
		double pi = 3.141592;
		double shortPi = Math.round(pi*1000)/1000.0;
		System.out.println(shortPi);
		
//	Ex3_12
		int x = 10; int y = 8;
		
		System.out.printf("%d을 %d로 나누면, %n", x, y);
		System.out.printf("몫은 %d이고, 나머지는 %d입니다.%n", x/y, x%y);
		
//	Ex3_13
		System.out.println(-10%8);
		System.out.println(10%-8);
		System.out.println(-10%-8);
		
// Ex3_14
		String str1 = "abc";
		String str2 = new String("abc");
		
		System.out.printf("\"abc\"==\"abc\" ? %b%n" , "abc"=="abc");
		System.out.printf(" str1 == \"abc\" ? %b%n" , str1=="abc");
		System.out.printf(" str2 == \"abc\" ? %b%n" , str2=="abc");
		System.out.printf("str1.equals(\"abc\") ? %b%n" , str1.equals("abc"));
		System.out.printf("str2.equals(\"abc\") ? %b%n" , str2.equals("abc"));
		System.out.printf("str2.equals(\"ABC\") ? %b%n" , str2.equals("ABC"));
		System.out.printf("str2.equalsIgnoreCase(\"ABC\") ? %b%n" , str2.equalsIgnoreCase("ABC"));
		
//	Ex3_15
		Scanner sc = new Scanner(System.in);
		char ch =' ';
		
		System.out.printf("문자를 하나 입력하세오.> ");
		String input = sc.nextLine();
		
	}
}
