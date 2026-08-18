public class Java0414_Animal_main {
	public static void main(String[] args) {
		Dog dog = new Dog("바둑이", 5);
		Cat cat = new Cat("나비", 3);
		
		dog.speak();
		dog.speak(3);
		cat.speak();
	}

}
