import java.time.LocalTime;

public class Java0428_LocalTime {

	public static void main(String[] args) {
		LocalTime now = LocalTime.now();
		LocalTime open = LocalTime.of(9, 0);
		LocalTime close = open.plusHours(10);
		
		System.out.println("현재 시간: " + now);
		System.out.println("오픈 시간: " + open);
		System.out.println("클로즈 시간: " + close);
	}

}
