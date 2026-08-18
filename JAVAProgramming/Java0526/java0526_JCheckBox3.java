import java.awt.FlowLayout;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;

import javax.swing.ButtonGroup;
import javax.swing.ImageIcon;
import javax.swing.JCheckBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JRadioButton;

public class java0526_JCheckBox3 extends JFrame{	
	public java0526_JCheckBox3() {
		setTitle("라디오버튼");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setLayout(new FlowLayout());
		
		ImageIcon cherryicon = new ImageIcon("images/cherry.jpg");
		ImageIcon cherryselected = new ImageIcon("images/selectedCherry.jpg");
		
		ButtonGroup g = new ButtonGroup();
		JRadioButton apple = new JRadioButton("사과"); 
		JRadioButton pear = new JRadioButton("배"); 
		JRadioButton cherry = new JRadioButton("체리", cherryicon); 
		cherry.setBorderPainted(true);
		cherry.setSelectedIcon(cherryselected);
		
		g.add(apple);
		g.add(pear);
		g.add(cherry);
		
		add(apple);
		add(pear);
		add(cherry);

		setSize(250,150);
		setVisible(true);
		
		}
		
	public static void main(String[] args) {
		new java0526_JCheckBox3();
	}
}
