import java.util.Scanner;
public class java0331_quiz2_sol {
	public static void main(String[] args) {
		int[] money = {50000, 10000, 5000, 1000, 500, 100, 50, 10};
		Scanner sc = new Scanner(System.in);
		System.out.print("금액을 입력하세요: ");
		int pay = sc.nextInt();
		
		for(int i=0; i<money.length; i++) {
			int cnt=pay/money[i];
			int amount = money[i] * cnt;
			pay %= money[i];
			
			if(cnt!=0) {
				System.out.println(money[i] + "원: " + cnt + "개(" + amount + ")");
		}
		if(pay != 0) {
			System.out.println("원 단위 이하 금액: "+ pay + "원");
		}
		sc. close();
	}
}
}
