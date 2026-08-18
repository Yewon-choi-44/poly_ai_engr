import java.awt.FlowLayout;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;

import javax.swing.ImageIcon;
import javax.swing.JCheckBox;
import javax.swing.JFrame;
import javax.swing.JLabel;

public class java0526_JCheckBox4 extends JFrame{
	JCheckBox[] fruits = new JCheckBox[3];
	String[] names = {"사과", "배", "체리"};
	JLabel sumLabel;
	int sum = 0;
	
	public java0526_JCheckBox4() {
		setTitle("체크박스");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setLayout(new FlowLayout());
		
		JLabel lbl1 = new JLabel("사과 100원, 배 500원, 체리 20,000원");
		
		for(int i = 0 ; i < fruits.length ; i++) {
			fruits[i] = new JCheckBox(names[i]);
			fruits[i].setBorderPainted(true);
			add(fruits[i]);
			fruits[i].addItemListener(new ItemListener() {
				public void itemStateChanged(ItemEvent e) {
					if(e.getStateChange() == ItemEvent.SELECTED) {
						if(e.getItem() == fruits[0]) {
							sum += 100;
						} else if(e.getItem() == fruits[1]) {
							sum += 500;
						} else {
							sum += 20000;
						}}
					else { 
						if(e.getItem() == fruits[0]) {
							sum -= 100;
						} else if (e.getItem() == fruits[1]) {
							sum -= 500;
						} else {
							sum -= 20000;
						}
					}
					sumLabel.setText("현재" + sum + "원 입니다.");
				}
			});
		}
		sumLabel = new JLabel("현재 0원 입니다.");
		add(sumLabel);
		setSize(250,200);
		setVisible(true);
		
		}
		
	public static void main(String[] args) {
		new java0526_JCheckBox4();
	}
}
