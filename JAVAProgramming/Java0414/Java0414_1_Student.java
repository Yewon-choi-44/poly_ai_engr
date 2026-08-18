public class Java0414_1_Student {
	public static void main(String[] args) {
		Student stObj1 = new Student();
	
//		stObj1.printInfo();
//		stObj1.inputData(20261001, "홍길동");
		stObj1.printInfo(); 
		
		
//		System.out.println("id: " + stObj1.id);
//		System.out.println("name: " + stObj1.name);

		Student stObj2 = new Student(20261002, "홍길훈");
		stObj2.printInfo();
		
	}
}
