public class Sedan extends Car_3{
	private int seatNum;

	
	
//	public Sedan() {
//		System.out.println("서브클래스(Sedan) 생성자");
//	}

	
	public void upSpeed(int speed) {
//		speed += speed;
		super.upSpeed(speed);
		System.out.println("현재 속도 (서브클래스) " + speed);
	}

	public int getSeatNum() {
		return seatNum;
	}

	
	public void setSeatNum(int seatNum) {
		this.seatNum = seatNum;
	}
	
	
}
