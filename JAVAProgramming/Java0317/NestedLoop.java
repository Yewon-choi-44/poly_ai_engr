public class NestedLoop {

	public static void main(String[] args) {
		for(int i=2 ; i<10 ; i++) { // 1단에서 9단
			for(int j=1 ; j<10 ; j++) { // 각 단의 구구셈 출력
				System.out.print(i + "*" + j + "=" + i*j); //구구셈 출력
				System.out.print('\t'); 
				System.out.print(' ');//하나씩 탭으로 띄우기
			}
			System.out.println(); // 한 단이 끝나면 다음 줄로 커서 이동
		}
		//System.out.println("와~넘~신기하다~");
	}
}
