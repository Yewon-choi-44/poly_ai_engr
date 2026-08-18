import java.util.Scanner;
public class lab_BaesuSumAverage {

	public static void main(String[] args) {
		//프로그램이 실행되면 다음과 같이 실행되는 프로그램을 작성해보세요.
		//배수의 값을 입력하면, 1부터 100까지의 수에서 입력된 배수의 값까지의 합과 평균을 구하시오.
		
		Scanner s =new Scanner(System.in);
		int num, sum = 0, cnt = 0;
		double avg = 0.0;
		
		System.out.print("배수 입력: ");
		num = s.nextInt(); //입력받은 건 어딘가에 들어가 있어야 사용이 가능하다.
		
		for(int i=1; i<=100 ; i++) {
			if(i%num==0) {
				sum += i;
				cnt++;
		}
		}
		
		//정수형과 정수형으로 평균을 구하게 되면 값도 당연히 정수형로 나온다.
		//평균을 소수형으로 얻으러면 아래와 같이.
				
		avg = (double) sum/cnt;
		
		System.out.println("입력한 수: "+num);
		System.out.println("배수의 개수: "+cnt);
		System.out.println("배수의 합: "+sum);
		System.out.println("배수의 평균: "+avg);
		System.out.println("배수의 평균: "+(double) sum/cnt);
		
		s.close();
	}

}
