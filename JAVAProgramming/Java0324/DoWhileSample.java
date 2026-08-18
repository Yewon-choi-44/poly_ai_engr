public class DoWhileSample {

	public static void main(String[] args) {
		char c = 'a';
		int a = 97; // == char c ='a'
		
		do {
			System.out.print(c);
			c=(char)(c+1);	
		} while(c<='z');
		
		System.out.println("\n");
		do {
			System.out.print((char) a); // == c
			a++; // ==c(char)(c+1)
		} while(a<123); // == c <= 'z'

	}

}
