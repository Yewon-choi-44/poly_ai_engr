public class LogicalOperator {

	public static void main(String[] args) {
		//비교 연산
		System.out.println('a'>'b');
		System.out.println(3 >= 2);
		System.out.println(-1 < 0);
		System.out.println(3.45 <= 2); 
		System.out.println(3 == 2); // 같으면 참
		System.out.println(3 != 2); // 다르면 참
		System.out.println(!(3 != 2)); //괄호 안이 참이면 거짓, 거짓이면 참
		
		//비교 연산과 논리 연산 복합
		System.out.println((3 > 2) && (3 > 4)); // 모두 맞아야 참
		System.out.println((3 != 2) || (-1 > 0)); // 하나라도 맞으면 참
		System.out.println((3 != 2)^(-1 > 0)); //서로 다를 때 참
		
		System.out.print((int)'a');
//		System.out.print((int)'b');
		
		
	}

}
