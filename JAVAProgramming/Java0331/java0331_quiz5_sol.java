import java.util.Scanner;
public class java0331_quiz5_sol {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] nums = new int[5];
		
		System.out.print("숫자 5개 입력: ");
		for(int i=0; i<nums.length; i++) {
			nums[i]=sc.nextInt();
		}
		
		for(int i=0; i<5 ; i++) {
			for(int j=i+1; j<5; j++) {
				if(nums[i] > nums[j]) {
					int temp = nums[i];
					nums[i] = nums[j];
					nums[j] = temp;			
				}
			}
			
			for (int x = 0 ; x<nums.length; x++) {
				System.out.print(nums[x]+" ");
			}
			System.out.println(i + 1 + "회");
			
		}
		System.out.print("정렬 결과: ");
		for(int i=0; i<nums.length; i++) {
			System.out.print(nums[i] + " ");
		}
		sc.close();
	}
}
