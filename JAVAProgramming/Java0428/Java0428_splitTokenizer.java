import java.util.Scanner;
import java.util.StringTokenizer;
public class Java0428_splitTokenizer {
		public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		System.out.println("날짜를 입력하시오: ");
		String input_date = sc.next();
		StringTokenizer st = new StringTokenizer(input_date,"-");
		String[] date_txt= {"년 ","월 ", "일"};
		
		int i=0; 
		while(st.hasMoreTokens()) {
			System.out.print(st.nextToken());
			System.out.print(date_txt[i]);
			i++;
		}
			
//		사용자로부터 날짜를 입력받아 split로 분리하여 출력하는 프로그램을 구현하시오.
//		실행 시 날짜를 입력하시오.: (yyyy-MM-dd 형식 유지) 2026-4-28
	//  출력시 2026년 4월 28일
		
		sc.close();
		}

	}