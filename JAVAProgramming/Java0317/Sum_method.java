import java.util.Scanner;

public class Sum_method {
	public static int sum(int n, int m) {
		return n+m;
	}

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int i, j, result;
		
		System.out.print("숫자1 입력: ");
		i = s.nextInt();
		
		System.out.print("숫자2 입력: ");
		j = s.nextInt();
		
		result = sum(i, j);
		System.out.print(result);
		
		s.close();

	}

}
