import java.util.Scanner;
public class Java0428_split {
	public static void main(String[] args) {
		
	Scanner sc = new Scanner(System.in);
	System.out.println("날짜를 입력하시오: ");
	String ddd = sc.next();
	String[] dddParts = ddd.split("-");
	
	int i=0; 
	String[] DDate= {"년 ","월 ", "일"};
	
	for(i = 0 ; i<dddParts.length ; i++)
		System.out.print(dddParts[i]+DDate[i]);
//		System.out.print(dddParts[i]+"월 ");
//		System.out.print(dddParts[i]+"일");
		
		
//	사용자로부터 날짜를 입력받아 split로 분리하여 출력하는 프로그램을 구현하시오.
//	실행 시 날짜를 입력하시오.: (yyyy-MM-dd 형식 유지) 2026-4-28
//  출력시 2026년 4월 28일
	
	sc.close();
	}

}
