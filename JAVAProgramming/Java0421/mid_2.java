public class mid_2 {
	public static void main(String[] args) {
		int sum = 0;
		for(int i=1; i<=10; i++) {
			if(i%4 == 0) continue;
			if(i>5) break;
			sum+=i;
		}
		System.out.println(sum);

	}

}
