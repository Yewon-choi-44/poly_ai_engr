import java.util.Scanner;
public class ArrayAccess {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
	
		int intArray[] = new int[5];
		int max=0;
		int min=1000;
		
		System.out.println("양수 5개를 입력하세요.");
		for(int i=0; i<5 ; i++) {
			intArray[i] = sc.nextInt();
			if(intArray[i] > max) {
				max = intArray[i];
			}
			if(intArray[i] <min) {
				min = intArray[i]; //else if로는 안되십니다. 왜 않돼는가?????
			}
		}
		System.out.println("가장 큰 수는 " + max + "입니다.");
		System.out.println("가장 작은 수는 "+ min + "입니다.");
		System.out.println("두 수의 차는 " + (max-min) + "입니다.");
		
		sc.close();
	}
	//(+)가장 큰 수와 가장 작은수의 차.
}
