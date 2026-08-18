public class Student {
	int id; //해당 클래스에서만 사용할 수 있는 지역변수...
			//전체적으로 사용하려거든 public으로.
	String name;
	
	public Student() {
		this(20261003, "홍길동");
		System.out.println("기본 생성자 호출");
	}
	
	
	
	public Student(int id, String name) {
		System.out.println("매개변수 생성자 호출");
		this.id = id;
		this.name = name;
	}



	void inputData(int id, String name) {
//		id = parm1;
//		name = parm2;	
		this.id = id;
		this.name = name;	
	}
	
	
	void printInfo() {
		System.out.println("id: " + id);
		System.out.println("name: " + name);
		
	}
}
