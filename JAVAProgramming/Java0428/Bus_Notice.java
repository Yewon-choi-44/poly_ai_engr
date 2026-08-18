interface BusNotice{
	void announce();
	}


class VoiceNotice implements BusNotice{
	@Override
	public void announce() {
		System.out.println("다음 정류장은 시청입니다.");
	}
}

class ScreenNotice implements BusNotice{
	@Override
	public void announce() {
		System.out.println("곧 정류장에 도착합니다.");
	}
}

class VibrationNotice implements BusNotice{
	@Override
	public void announce() {
		System.out.println("버스가 정차 예정입니다.");
	}
}


public class Bus_Notice {
	public static void main(String[] args) {
		BusNotice[] bus = {new VoiceNotice(), new ScreenNotice(), new VibrationNotice()};
		for (BusNotice b : bus)
			b.announce();
		
		}

	}
