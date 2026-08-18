public class Dog extends Animal {
//	public String speak;
//	private int times;

	public Dog(String name, int age) {
		super(name, age);
	}
	
	void speak() {
		System.out.println(name + "가 멍멍 짖습니다. ");
	}
	
	void speak(int times) {
		for (int i = 0 ; i < times ; i++) {
			System.out.println("멍멍");
		}
	}
}
