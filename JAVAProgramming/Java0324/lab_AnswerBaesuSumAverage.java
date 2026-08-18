import java.util.Scanner;
public class lab_AnswerBaesuSumAverage {

	public static void main(String[] args) {
		//프로그램이 실행되면 다음과 같이 실행되는 프로그램을 작성해보세요.
		//배수의 값을 입력하면, 1부터 100까지의 수에서 입력된 배수의 값까지의 합과 평균을 구하시오.
		
		int sum = 0;
		double avg = 0;
		int mul = 0;
		int cnt=0;
		int i=0;
		int num=0;
		
		Scanner sc = new Scanner(System.in);
		
		System.out.print("배수입력: ");
		num = sc.nextInt();
		
		/*for(i=1; i<=100; i++) {
			if (i%num==0){
				sum+=i;
				cnt++;
			}
			//System.out.print(i);
		}
		*/
		while(i<=100) {
			i++;
			if (i%num==0) {
				sum+=i;
				cnt++;
			}
		}
		avg = (double)sum/cnt;
		
		System.out.println("1부터 100까지의 5의 배수 합: " +  sum);
		System.out.println("1부터 100까지의 5의 배수 평균:  " + avg);
		
		sc.close();

	}

}
