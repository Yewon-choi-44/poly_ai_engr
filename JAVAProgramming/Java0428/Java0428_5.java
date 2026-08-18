interface Car{ // 여기에 정의되는 건 행동
	void move();
	void stop();
}

interface CarInfo { // 여기에 정의되는 건 특징
	void color();
}

class Sedan implements Car, CarInfo{
	@Override
	public void move() {
		System.out.println("나는 달릴 수 있습니다.");
	}
	
	@Override
	public void stop() {
		System.out.println("나는 멈출 수 있습니다.");
	}
	
	@Override
	public void color() {
		System.out.println("나는 검정 세단 자동차입니다.");
	}
}

public class Java0428_5 {

	public static void main(String[] args) {
		Sedan sedan = new Sedan();
		sedan.color();
		sedan.move();
		sedan.stop();
	}

}
