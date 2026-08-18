//abstract class Car{
//	String name;
//	int speed;
//	void setSpeed(int speed) {
//		this.speed = speed;
//	}
//	abstract void show();	
//}
//
//
//class Sedan2 extends Car{
//	@Override
//	void show() {
//		System.out.println("나는 세단 자동차이며, 시속 " + speed + "km로 달립니다.");
//	}
//}
//class Sedan extends Car {
//	@Override
//	void show() {
//		System.out.println("나는 세단 자동차이며, 시속 " + speed +"km로 달립니다.");
//	}
//	
//}
//
//class Truck extends Car{
//	@Override
//	void show() {
//		System.out.println("나는 트럭 자동차이며, 시속 " + speed + "km로 달립니다.");
//	}
//}
//
//public class Java0428_4 {
//	public static void main(String[] args) {
////	Car car = new Car; 추상클래스로 선언되었기 때문에 이렇게 객체 생성이 불가하다.
//	Car sedan = new Sedan();
//	sedan.setSpeed(100);
//	sedan.show();
//}
//}