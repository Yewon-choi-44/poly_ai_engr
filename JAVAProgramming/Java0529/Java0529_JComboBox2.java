import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JComboBox;
import javax.swing.JFrame;

public class Java0529_JComboBox2 extends JFrame {
	String[]  fruits = {"apple", "banana", "kiwi","mango","pear", "cherry"};
//	String[] names = {"kitae", "jaemoon", "hyosoo","namyun"};
	JComboBox<String> strCmb1;
//	JComboBox<String> strCmb2;
	
	public Java0529_JComboBox2() {
		setTitle("콤보박스 만들기");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setLayout(new FlowLayout());
		
		strCmb1 = new JComboBox<String>(fruits);
//		strCmb2 = new JComboBox<String>();
		
		
		strCmb1.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				strCmb2.addItem(strCmb1.getSelectedItem().toString());
			}
		});

		add(strCmb1);
		add(strCmb2);
	}
	public static void main(String[] args) {
		new Java0529_JComboBox();
		
	}
}
