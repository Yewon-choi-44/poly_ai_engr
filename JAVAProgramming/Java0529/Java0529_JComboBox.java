import java.awt.FlowLayout;

import javax.swing.JComboBox;
import javax.swing.JFrame;

public class Java0529_JComboBox extends JFrame {
	String[]  fruits = {"apple", "banana", "kiwi","mango","pear","peach","berry","berry","strawberry","balckberry"};
	String[] names = {"kitae", "jaemoon", "hyosoo","namyun"};
	
	public Java0529_JComboBox() {
		setTitle("콤보박스 만들기");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setLayout(new FlowLayout());
		
		JComboBox<String> strCmb1 = new JComboBox<String>(fruits);
		
		
		JComboBox<String> strCmb2 = new JComboBox<String>();
		for (int i=0; i<names.length;i++) {
			strCmb2.addItem(names[i]);
		}
		add(strCmb1)
	}
	public static void main(String[] args) {
		
	}
}
