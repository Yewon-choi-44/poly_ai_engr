import java.util.Calendar;
public class Java0428_Calendar {

	public static void main(String[] args) {
		Calendar cal = Calendar.getInstance();
		//cal.add(Calendar.DATE, 7);
		int year = cal.get(Calendar.YEAR);
		int month = cal.get(Calendar.MONTH)+1;
		int day = cal.get(Calendar.DAY_OF_MONTH);
		int hour = cal.get(Calendar.HOUR_OF_DAY);
		int minute = cal.get(Calendar.MINUTE);
		
		System.out.println("오늘: " + year + "년 " + month + "월 " + day + "일");
		System.out.println("오늘: " +  hour + "시 " + minute + "분");
	}

}
