public class Car {
//	자동차(Car) 클래스는 색상(Color)과 속도(Speed)의 필드를 가지고 있으며.
//	또한 자동차 클래스에는 색상과 속도를 입력 받는 carDataInput()메서드와 carDataPrint() 메서드를 가지고 있다.
//	다음과 같이 입력값이 주어질 때 다음과 같은 결과가 출력되도록 프로그램을 객체지향형으로 작성해보세요.
//	입력예				출력 예
//	검정, 100	->		검정색 차량이 시속 100km로 달린다.
	
	String Color;
	int Speed;
	
	
	public String getColor() {
		return Color;
	}

	public void setColor(String color) {
		Color = color;
	}

	public int getSpeed() {
		return Speed;
	}

	public void setSpeed(int speed) {
		Speed = speed;
	}		
}

