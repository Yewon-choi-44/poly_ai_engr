import java.util.Scanner;
public class Kcal_Sol {
	public static void calckacl(int n) {
		double g = 180;
		double kcal = 5.179;
		System.out.printf("삼겹살 %d인분의 칼로리: %.2f kcal", n, (n*g*kcal));
	}
	
	
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int n;
		
		System.out.println("삼겹살 몇 인분? ");
		n = s.nextInt();
		
		calckacl(n);
		
		s.close();
	}
}
