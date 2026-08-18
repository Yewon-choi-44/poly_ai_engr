public class Student { //클래스에서 가장 먼저 선언 되는게 생성자...
 	int id;
	String name;
	
	void inputData(int parm1 , String parm2) {
		id = parm1;
		name = parm2;
	}
	
	void printInfo() {
		System.out.println("학번: " + id);
		System.out.println("성명: " + name);
	}
}