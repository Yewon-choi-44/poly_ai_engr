public class mid_3 {
	public static void main(String[] args) {
		int[] arr = new int[5];
		int sum = 0;
		for(int i=0 ; i<arr.length ; i++) {
			arr[i]+=10;
		}
		for(int i=1; i<arr.length; i+=2) {
			sum+=arr[i];
		}
		System.out.println(sum);
	}

}
