class Donut{
	String name;
	
	public Donut(String name) {
		this.name = name;
	}
	
	@Override
	public boolean equals(Object obj) {
		if(obj instanceof Donut) {
			Donut other = (Donut) obj;
			return this.name.equals(other.name);
		}
		return false;
	}
}
public class JavaEquals {

	public static void main(String[] args) {
		Donut d1 = new Donut("초코"); 
		Donut d2 = new Donut("초코"); 
		System.out.println("equals 결과: " + d1.equals(d2));
		System.out.println("==결과== : " + (d1==d2));
	}

}
