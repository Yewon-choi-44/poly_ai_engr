public class Java0428_Math {
	public static void main(String[] args) {
		int price = 3500;
		double discount = 0.15;
		double newprice = price * (1-discount);
		long rounded = Math.round(newprice);
		System.out.println("원래 가격: " + price + "원");
		System.out.println("할인율: " + (int)(discount*100) + "%");
		System.out.println("할인가(반올림): " + rounded + "원");
		
		
		int cnts = (int) (Math.random()*100)+1; //몇 개까지 추출할 건가는 뒤에 *붙이고 표시함.
		System.out.println("랜덤 갯수: " + cnts + "개");
		System.out.println("총 가격: " + (rounded*cnts) + "원");
	}

}
