import java.util.InputMismatchException;
import java.util.Scanner;
public class java0331_quiz3_sol {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n1,n2;
		String op;
		try {
			System.out.println("계산 입력(+ , - , * , / ): ");
			op = sc.next();
			System.out.println("첫 번째 숫자 입력: ");
			n1 = sc.nextInt();
			System.out.println("두 번째 숫자 입력: ");
			n2 = sc.nextInt();
			switch(op) {
				case "+":
					System.out.println("계산 결과: " + (n1 + n2));
					break;
				case "-":
					System.out.println("계산 결과: " + (n1 - n2));
					break;
				case "*":
					System.out.println("계산 결과: " + (n1 * n2));
					break;
				case "/":
					System.out.println("계산 결과: " + (n1 / n2));
					break;
				default:
					System.out.println("잘못된 연산자입니다.");
			}
		} catch (ArithmeticException a) {
			System.out.println("0으로 나눌 수 없습니다."); // 0인 경우 에러
		} catch (InputMismatchException i) {
			System.out.println("정수만 가능합니다. 다시 입력하세요."); //  입력 오류 에러
		}
		
		sc.close();
	}

}