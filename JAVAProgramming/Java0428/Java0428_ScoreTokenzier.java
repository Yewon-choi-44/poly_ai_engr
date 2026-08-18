import java.util.Scanner;
import java.util.StringTokenizer;

public class Java0428_ScoreTokenzier {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		System.out.println("성명과 점수를 입력하시오(쉼표구분): ");
		String nameScore = sc.nextLine();
		StringTokenizer st = new StringTokenizer(nameScore,",");
		
		String name;
		int cnt=0;
		int sum = 0; 
		
		name = st.nextToken();
		while(st.hasMoreTokens()) {
			sum += Integer.parseInt(st.nextToken());
			cnt++;
//			String score = st.nextToken();
//			System.out.println("성명: "+score);
			
		}
		System.out.print("성명: " + name + " / 평균: " + (double)(sum/cnt) );
		

		
// 입력 받은 점수를 분리하여 평균을 구하여 예시 형태와 같이 출력하시오.
// 성명과 점수를 입력하시오(쉼표구분): 홍길동,90,80,70
// 출력예시 성명: 홍길동 / 평균: 80.0
	}
	}	
