public class mid_5 {
	public static void main(String[] args) {
		int[] arr = {1,2,3};
		int result =0;
		
		try {
			for(int i=0; i<=arr.length; i++) {
				result += arr[i];
			}
		} catch(ArrayIndexOutOfBoundsException e) {
			result += 10;
		} catch(Exception e) {
			result += 20;
		} finally {
			result += 2;
		}
		System.out.println(result);
	}

}
