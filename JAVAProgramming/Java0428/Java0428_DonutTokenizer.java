import java.util.StringTokenizer;

public class Java0428_DonutTokenizer {
	public static void main(String[] args) {
		String donutMenu = "초코,레몬,딸기,크림";
		StringTokenizer st = new StringTokenizer(donutMenu,",");
		
		System.out.println("메뉴에 있는 도넛 종류");
		
		while (st.hasMoreTokens()) {
			String donut = st.nextToken();
			System.out.println("-" + donut + " 도넛");
		}

	}
}
