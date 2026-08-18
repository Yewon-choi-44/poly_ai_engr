abstract class Payment{
	abstract void pay();
}


class CardPayment extends Payment{
	@Override
	void pay() {
		System.out.println("카드로 결제합니다.");
	}
}

class SimplePayment extends Payment{
	@Override
	void pay() {
		System.out.println("간편결제로 결제합니다.");
	}
}

public class Pay {
	public static void main(String[] args) {
		Payment[] payments = {new CardPayment(), new SimplePayment()};
		for(Payment py: payments)
			py.pay();
	}
}
