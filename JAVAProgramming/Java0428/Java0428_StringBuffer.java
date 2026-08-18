public class Java0428_StringBuffer {
	public static void main(String[] args) {
		StringBuffer sb = new StringBuffer("도넛");
		
		System.out.println("초기 문자열: "+sb);
		sb.append(" 가게");
		
		System.out.println("append 후: "+sb);
		sb.insert(2, "맛있는");
		
		System.out.println("insert 후: "+sb);
		sb.delete(2, 6);
		
		System.out.println("delete 후: "+sb);
		sb.replace(0, 2, "초코");
		
		System.out.println("replace 후: "+sb);
		sb.reverse();
		
		System.out.println("reverse 후: "+sb);
		
		String result = sb.toString();
		System.out.println("최종 문자열(String): "+result);
	}

}
