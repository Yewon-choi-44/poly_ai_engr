public class Java0414_2_Car_3 {
	public static void main(String[] args) {
		Sedan sedan = new Sedan();
	//	Car_3 car = new Car_3();
		Truck truck = new Truck();
		
		sedan.upSpeed(300);
//		sedan.seatNum = 5;
	
		sedan.setSeatNum(5);
		sedan.setColor("검정");
		
//		car.color = "노란색";
//		sedan.color = "검정";		
//		truck.capacity = 50;
		
		truck.setCapacity(50);
		truck.upSpeed(100);
		
//		System.out.println("승용차 속도는 " + sedan.speed + "km, 차량 색상은 " + sedan.color + ", 좌석수는 "  + sedan.getSeatNum() + "개 입니다.");
		System.out.println("승용차 속도는 " + sedan.getSpeed() + "km, 차량 색상은 " + sedan.getColor() + ", 좌석 수는 " + sedan.getSeatNum() + "개 입니다.");
//		트럭 속도는 100km, 적재량은 50톤 입니다. < 도 출력해보기.
//		System.out.println("트럭 속도는 " + truck.speed + "km, 적재량은 " + truck.capacity + "톤 입니다.");
//		System.out.println("트럭 속도는 " + truck.speed + "km, 적재량은 " + truck.getCapacity() + "톤 입니다.");
		System.out.println("트럭 속도는 " + truck.getSpeed() + "km, 적재량은 " + truck.getCapacity() + "톤 입니다.");
		
		

	}

}
