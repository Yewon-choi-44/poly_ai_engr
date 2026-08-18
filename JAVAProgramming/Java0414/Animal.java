public class Animal {
	String name;
	int age;
	
	public Animal(){
		System.out.println("동물 생성");
	}
	
	public Animal(String name, int age){
		this.name = name;
		this.age = age;
	}
	
	void speak() {
		System.out.println("동물이 소리를 냅니다.");
	}
}
