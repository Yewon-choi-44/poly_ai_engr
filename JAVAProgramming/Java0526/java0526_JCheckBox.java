import java.awt.FlowLayout;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;

import javax.swing.ImageIcon;
import javax.swing.JCheckBox;
import javax.swing.JFrame;

public class java0526_JCheckBox extends JFrame{
	public java0526_JCheckBox() {
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
		
	
		
		
		add(apple);
		add(pear);
		add(cherry);
		
		setSize(300, 150);
		setVisible(true);
	}
	
	public static void main(String[] args) {
		new java0526_JCheckBox();
	}

}
