import java.util.Scanner;
public class ForSample {
	public static void main(String[] args) {
		int sum = 0;
		Scanner sc = new Scanner(System.in);
		
		System.out.print("숫자를 입력하시오(1~50): ");
		int num = sc.nextInt();
		
		for(int i=1 ; i<=num ; i++) {
			sum+=i;
			System.out.print(i);
			
			if(i<num) {
				System.out.print("+");
			}
			else {
				System.out.print("=");
				System.out.print(sum);
			}
		}
	}
}
