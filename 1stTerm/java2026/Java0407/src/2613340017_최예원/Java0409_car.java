//	자동차(Car) 클래스는 색상(Color)과 속도(Speed)의 필드를 가지고 있으며.
//	또한 자동차 클래스에는 색상과 속도를 입력 받는 carDataInput()메서드와 carDataPrint() 메서드를 가지고 있다.
//	다음과 같이 입력값이 주어질 때 다음과 같은 결과가 출력되도록 프로그램을 객체지향형으로 작성해보세요.
//	입력예				출력 예
//	검정, 100	->		검정색 차량이 시속 100km로 달린다.

import java.util.Scanner;
public class Java0409_car {
	public static void main(String[] args) {
		Car_2 carObj1 = new Car_2();
		
		String c; int s;
		Scanner sc = new Scanner(System.in);
		System.out.print("차량 색깔: ");
		c = sc.nextLine();
		System.out.print("시속 몇 km: ");
		s = sc.nextInt();
		
		carObj1.carDataInput(c , s);
		carObj1.carDataPrint();
		
		sc.close();
	}
}
