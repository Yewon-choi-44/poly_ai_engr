import java.util.Scanner;

public class Volume {

	public static void Volumn(int n) {
		System.out.println("한 변의 길이가  "+n+"인 정육면체의 부피: "+(n*n*n));
	}
	
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n;
		
		System.out.print("한 변 길이: ");
		n=sc.nextInt();
		
		Volumn(n);
		sc.close();

	}

}
