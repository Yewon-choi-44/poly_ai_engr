import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;

import javax.swing.ButtonGroup;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JRadioButton;

public class java0526_JPanel2 extends JFrame {
	JRadioButton[] radio = new JRadioButton[3];
	String[] names = {"사과", "배", "체리"};
	ImageIcon[] imgs = {new ImageIcon("images/apple.jpg"),
						new ImageIcon("images/pear.jpg"),
						new ImageIcon("images/cherry.jpg")};
	
	JLabel img;
	public java0526_JPanel2() {
		setTitle("라디오 버튼 이벤트");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setLayout(new BorderLayout());
		
		JPanel jp1 = new JPanel();
		JPanel jp2 = new JPanel();
		jp1.setBackground(Color.LIGHT_GRAY);		
		
		img = new JLabel("");
		ButtonGroup g = new ButtonGroup();
		
		for (int i = 0 ; i < radio.length ; i++) {
			radio[i] = new JRadioButton(names[i]);
			g.add(radio[i]);
			jp1.add(radio[i]);
			radio[i].addItemListener(new ItemListener() {				
				public void itemStateChanged(ItemEvent e) {
					if(radio[0].isSelected()) {
						img.setIcon(imgs[0]);} 
					else if(radio[1].isSelected()) {
						img.setIcon(imgs[1]);} 
					else {
						img.setIcon(imgs[2]);}
				}
			});
		}
		
		radio[2].setSelected(true);
		jp2.add(img);
		
		add(jp1, BorderLayout.NORTH);
		add(jp2, BorderLayout.CENTER);
		setSize(300, 250);
		setVisible(true);
	}
	
	public static void main(String[] args) {
		new java0526_JPanel2();
	}
}
