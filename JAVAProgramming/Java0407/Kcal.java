import java.util.Scanner;

public class Kcal {
	public static void calckcal(int n) {
		System.out.println("삼겹살" + n + "인분의 칼로리: " + (180*n)*5.179 + "kcal");
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n;
		
		System.out.print("삼겹살 몇 인분: ");
		n = sc.nextInt();
		
		calckcal(n);
		
		sc.close();

	}

}
