class Donut1{
	String name;
	int price;
	public Donut1(String name, int price) {
		this.name = name;
		this.price = price;
	}
	
	@Override
	public String toString() {
		return name + "도넛(" + price + "원)    ";
	}
}
public class Java_EqualsDonut {
	public static void main(String[] args) {
		Donut1 d1 = new Donut1("초코", 3900);
		System.out.println(d1);
		
	}
}
