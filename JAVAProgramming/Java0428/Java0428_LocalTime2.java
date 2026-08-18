import java.time.LocalDateTime;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;

public class Java0428_LocalTime2 {
	public static void main(String[] args) {
		LocalDateTime now = LocalDateTime.now();
		LocalTime open = LocalTime.of(9, 0);
		LocalTime close = open.plusHours(10);
		
		DateTimeFormatter f = DateTimeFormatter.ofPattern("yy년 MM월 dd일 E hh시 mm분 a");
		//y년도 , M월, d일, E요일, H(24시각제), h(12시각제), m분, s초, a AM/PM
		//MM - 월, mm-분 대/소문자 구분 해야함
		
		System.out.println("현재 시간: " + now.format(f));
		System.out.println("오픈 시간: " + open);
		System.out.println("클로즈 시간: " + close);
	
	//오늘 날짜로부터 100일 후의 날짜를 구하여 yyyy-M-dd형식으로 출력하시오.
		LocalDateTime baek = now.plusDays(100);
		DateTimeFormatter b = DateTimeFormatter.ofPattern("yyyy-MM-dd(E)");
		
		System.out.println("100일 후: " + baek.format(b) );
	
	}
	
	
	

}
