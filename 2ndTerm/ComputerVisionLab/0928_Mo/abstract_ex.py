"""
abstract class: 추상화 클래스
구현 코드 없이 메서드의 선언만 있는 추상 메서드를 포함한 클래스
선언(declaration): 반환 타입, 메서드 이름, 매개변수만 있는 것
정의(definition): 메서드 (선언부를 포함해서 구현이 되어 있는 것)
int add(int x, int y); //declaration
int add(int x, int y) { } //definition

추상화 메서드 또는 클래스에 "abstract" 예약어 사용(으로 선언)
*

public abstract class Computer {

}

    
public class Desktop extends Computer{
    @Override
    public void display() {}
    @Override
    public void typing() {}
    @Override
    public void turnOn() {
        System.out.println("Turn On the Desktop");
    }
    }
"""

from abc import * #파일명 또는 폴더 명에 abc는 사용 금지
class Computer(metaclass=ABCMeta):
    @abstractmethod
    def display(self):
        pass
    @abstractmethod
    def typing(self):
        pass
    def turnOn(self):
        print("Turn On a Computer")

class Desktop(Computer):
    def display(self):
        print('Desktop display')
    def typing(self):
        print('Desktop typing')
    def turnOn(self):
        print('Turn On the Desktop')

if __name__ == "__main__":
    desktop = Desktop()

    desktop.display()
    desktop.typing()
    desktop.turnOn()

# 다중 상속(상속-->상속 코드도 확인해볼 것)
# 20분동안 Notebook 클래스를 컴퓨터 추상화 클래스를 상속 받아
# 메서드 저으이 및 메서드 오버라이딩 해서 테스트 해보세요