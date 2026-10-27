package practice;
public class Jajungsuck3_1 {
	public static void main(String[] args) {
//	#Ex3_1
		int x,y;
		
		x = y = 3;
		System.out.println("x = " + x);
		System.out.println("y = " + y);

//	#Ex3_2	
		int i = 5, j = 0;
		
		j=i++;
		System.out.println("j=i++; 실행 후 , i=" + i + ", j="+ j);
		
		i=5; j=0;
		
		j = ++i;
		System.out.println("j=++i; 실행 후, i=" + i + ", j=" + j);
		
//	#Ex3_3
		i = 5; j=5;
		System.out.println(i++);
		System.out.println(++j);
		System.out.println("i = "+i+", j= "+j);
		
//	#Ex3_4
		i = -10;
		i = +i;
		System.out.println(i);
		
		i=-10;
		i=-i;
		System.out.println(i);
		
//	#Ex3_5
		double d =  85.4;
		int score = (int) d;
		System.out.println("score= " + score);
		System.out.println("d= "+d);
		
		
		
//	#Ex3_6
		int a = 10; int b = 4;
		
		System.out.printf("%d + %d = %d%n", a, b, a+b);
		System.out.printf("%d - %d = %d%n", a, b, a-b);
		System.out.printf("%d * %d = %d%n", a, b, a*b);
		System.out.printf("%d / %d = %d%n", a, b, a/b);
		System.out.printf("%d / %f = %f%n", a, (float)b, a/(float)b);
		
//	#Ex3_7
		System.out.println(5/2);
		System.out.println(5/(float)2);
		
//	Ex3_8
		byte aa = 10;
		byte bb = 30;
		byte cc = (byte)(aa*bb);
		System.out.println(cc);
		
//	Ex3_9
		a = 1_000_000;
		b = 2_000_000;
		
		long c = a * b;
		
		System.out.println(c);
		
//	Ex3_10
		long aaa = 1_000_000 * 1_000_000;
		long bbb =  1_000_000 * 1_000_000L;
		
		System.out.println("a="+aaa);
		System.out.println("b="+bbb);
	}
}
