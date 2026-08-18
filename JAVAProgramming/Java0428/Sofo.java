abstract class Delivery{
	abstract void delivery();
}

class BoxDelivery extends Delivery{
	@Override
	void delivery() {
		System.out.println("택배 상자를 배송합니다.");
	}
	
}

class FoodDelivery extends Delivery{
	@Override
	void delivery() {
		System.out.println("음식을 배송합니다.");
	}
}

public class Sofo {
	public static void main(String[] args) {
		Delivery[] delivery = {new BoxDelivery(), new FoodDelivery()};
		for(Delivery d: delivery)
			d.delivery();
		
	}
}
