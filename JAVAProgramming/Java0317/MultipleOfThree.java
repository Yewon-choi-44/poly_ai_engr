import java.util.Scanner;

public class MultipleOfThree {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		
		System.out.print("수를 입력하시오: ");
		int number = in.nextInt();
		
		System.out.print("몇의 배수임? ");
		int mult = in.nextInt();
		
		if(number % mult == 0) {
			System.out.println(mult+"의 배수임");
		}
		else {
			System.out.println(mult+"의 배수가 아님");
		}
		in.close();

	}

}
