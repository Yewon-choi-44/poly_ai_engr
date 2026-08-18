import java.time.LocalDate;
import java.util.Scanner;

public class Java0428_LocalDate {

	public static void main(String[] args) {
		LocalDate today = LocalDate.now();
		Scanner sc = new Scanner(System.in);
		System.out.print("태어난 년도를 입력하세요: ");
		int Bday = sc.nextInt();
		System.out.println("나이: " + ((today.getYear()-Bday)+1) + "세");
		
		
		
		
//		System.out.println("오늘 날짜: " + today);
//		System.out.println("일주일 후: " + today.plusWeeks(1));
//		System.out.println("한달 전: " + (today.minusMonths(1)-Bday));
//		System.out.println("현재 년도: " + today.getYear());
//		System.out.println("현재 월: " + today.getMonth());
//		System.out.println("현재 월: " + today.getMonthValue());
//		System.out.println("현재 일: " + today.getDayOfMonth());
		
		
		sc.close();
	}

}

//태어난 년도를 입력받아 현재 연도를 기준으로 나이를 계산하여 출력하시오.
//--출력시--
//태어난 년도를 입력하세요: 2000
//나이: 27세