public class mid_4 {
	public static void main(String[] args) {
		int arr[] = make_array();
		for (int i=0; i< arr.length; i++) {
			System.out.println(arr[i]+"/");
		}
		
		

	}
	private static int[] make_array(){
		int temp[] = new int[5];
		for(int i=0; i<temp.length; i++) {
			temp[i]+=(i++);
		}
		return temp;
	}
}

