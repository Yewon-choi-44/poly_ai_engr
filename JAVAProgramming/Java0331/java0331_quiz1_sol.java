public class java0331_quiz1_sol {
	public static void main(String[] args) {
		String[] names = {"Elena", "Suzie","John","emily","neda","kate","alex","daniel","sam"};
		int[] scores = {65, 74, 23, 75, 68, 96, 88, 98, 54};
		
		int max = scores[0];
		int maxIdx = 0;
		//String maxname = names[0];
		
		for(int i=0 ; i<scores.length; i++) {
			if(max < scores[i]) {
				max = scores[i];
				maxIdx = i;
				//maxname = names[i];
			}
		}
		System.out.print("1등: "+ names[maxIdx] + "("+ max + ")");
	}
}
