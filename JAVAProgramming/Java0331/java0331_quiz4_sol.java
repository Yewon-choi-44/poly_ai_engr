import java.util.InputMismatchException;
import java.util.Scanner;
public class java0331_quiz4_sol {
	public static void main(String[] args) {
		/*int arr[]= {0,1,2,3,4,5,6,7,8,9};
		
		System.out.println("정수 10개를 입력하시오: ");
		Scanner sc = new Scanner(System.in);
		for(int i = 0; i<10 ; i++) {
			arr[i]=sc.nextInt();
		}*/
		
		Scanner sc = new Scanner(System.in);
		int[] nums = new int[10];
		
		try {
				System.out.print("정수 10개 입력: ");
				for(int i=0; i<nums.length; i++) { 
					nums[i] = sc.nextInt();
				}
				System.out.print("결과: ");
				for(int i=0; i<nums.length;i++) {
					boolean d=false;
					for(int j=0; j<i ; j++) {
						if(nums[i]==nums[j]) {
							d=true;
							break;
						}
					}
					if(!d)
						System.out.print(nums[i] + " ");
				}
				
		} catch(InputMismatchException e) {
			System.out.println("입력 값 오류");
		}			
		sc.close();
	}
	
		
}


