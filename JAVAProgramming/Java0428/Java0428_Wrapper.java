public class Java0428_Wrapper {
	public static void main(String[] args) {
		Integer num1 = 100;
		System.out.println("오토박싱값: " + num1);
		
		int i = num1;
		System.out.println("언박싱값: "+i);
		
		String s = "123";
		int j = Integer.parseInt(s);
		System.out.println("문자열을 정수 변환: " + j);
		
		String str = Integer.toString(j);
		System.out.println("정수 문자열 변환: " + str);
		
		String yes = "true";
		Boolean flag = Boolean.parseBoolean(yes);
		if(flag)
			System.out.println("yes");
		else
			System.out.println("no");

	}

}
