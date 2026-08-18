public class Car_3 {
	private String color;
	private int speed;
	
	public void upSpeed(int value) {
		speed += value;
		System.out.println("현재 속도(슈퍼클래스): " + this.speed);
	}
	
	public void downSpeed(int value) {
		speed -= value;
	}

	
	public Car_3() {
		System.out.println("슈퍼클래스(Car) 생성자");
	}

	public final void upSpeed(int value) {
	//final 생성하라 하셨는데 내가 놓침 빨간줄뜨는게정상이라하셔음이거나중에다시봐야함
		speed += value;
		System.out.println(" ");
	}
	
	
	public String getColor() {
		return color;
	}

	public int getSpeed() {
		return speed;
	}

	
	public void setColor(String color) {
		this.color = color;
	}

	
	public void setSpeed(int speed) {
		this.speed = speed;
	}
	
	
	
	
	
	
	

}
