import java.awt.FlowLayout;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;

import javax.swing.ImageIcon;
import javax.swing.JCheckBox;
import javax.swing.JFrame;

public class java0526_JCheckBox2 extends JFrame{
	public java0526_JCheckBox2() {
		setTitle("체크박스");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setLayout(new FlowLayout());
		
		ImageIcon cherryicon = new ImageIcon("images/cherry.gif");
		ImageIcon cherryselected = new ImageIcon("images/selectedCherry.jpg");
		
		JCheckBox apple = new JCheckBox("사과");
		JCheckBox pear = new JCheckBox("배", true);
		JCheckBox cherry = new JCheckBox("체리", cherryicon);
		cherry.setBorderPainted(true);
		cherry.setSelectedIcon(cherryselected);
		
		apple.addItemListener(new ItemListener() {			
			public void itemStateChanged(ItemEvent e) {
				if(e.getStateChange() == ItemEvent.SELECTED) {
					System.out.println("사과가 선택됨.");}
				else { 
					System.out.println("사과가 선택 해제됨."); }
			}
		});
		
		add(apple);
		add(pear);
		add(cherry);
		
		setSize(300, 150);
		setVisible(true);
	}
	
	public static void main(String[] args) {
		new java0526_JCheckBox2();
	}
}
