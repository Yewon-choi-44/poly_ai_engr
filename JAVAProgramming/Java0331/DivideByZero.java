import java.util.InputMismatchException;
import java.util.Scanner;
public class DivideByZero {
	public static void main(String[] args) {
		int dividend; // 나뉨수
		int divisor; // 나눗수
		Scanner sc = new Scanner(System.in);
		while(true) {
			try {
				
				System.out.print("\n나뉨수를 입력하시오.: ");
				dividend = sc.nextInt(); // 나뉨수 입력
				System.out.print("나눗수를 입력하시오: ");
				divisor = sc.nextInt(); // 나눗수 입력
				System.out.println(dividend + "를 " + divisor + "로 나누면 몫은 " + dividend/divisor + "입니다.");
				break;	
			} catch(ArithmeticException a) {
				//a.printStackTrace(); //어떤 에러가 났는지 보고 싶을대...
				System.out.println("0으로 나눌 수 없습니다. 다시 입력하세요.");
			} catch(InputMismatchException i) {
				System.out.println("정수만 입력 가능합니다. 다시 입력하세요.");
				sc.nextLine();
			}
		}
		sc.close();
	}
}
