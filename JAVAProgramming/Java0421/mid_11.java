class Radar{
	int limit = 60;
	
	int check(int s) {
		if(s > limit) {
			return 1;
		}
		else {
			return 0;
		}
	}
}

class HighwayRadar extends Radar{
	public HighwayRadar() {
		this.limit = 100;
	}
	
	int check(int s) {
		int stateCode = super.check(s);
		if(stateCode == 1) {
			return 1000000;}
		else {
			return 0;}
	}
}

public class mid_11 {
	public static void main(String[] args) {
		HighwayRadar hr = new HighwayRadar();
		System.out.println(hr.check(110));
	}
}
