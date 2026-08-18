import java.awt.BorderLayout;
import java.awt.FlowLayout;
import java.awt.Image;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.ImageIcon;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;

public class Java0529_JComboBox4 extends JFrame {
	String[]  fruits = {"apple", "banana", "kiwi","mango","pear", "cherry"};
	ImageIcon[] imgs = {new ImageIcon("images/apple.jpg"), new ImageIcon("images/banana.jpg"), new ImageIcon("images/kiwi.jpg"), new ImageIcon("images/mango.jpg"), new ImageIcon("images/pear.jpg"), new ImageIcon("images/cherry.jpg")};
	JComboBox<String> strCmb1;
	JLabel imglbl = new JLabel();
	
	public Java0529_JComboBox4() {
		setTitle("콤보박스 만들기");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setLayout(new FlowLayout());
		
		strCmb1 = new JComboBox<String>(fruits);
		imglbl.setIcon(new ImageIcon(
				imgs[strCmb1.getSelectedIndex()].getImage().getScaledInstance(250, 200, Image.SCALE_SMOOTH)));
		
		strCmb1.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				imglbl.setIcon(new ImageIcon(imgs[strCmb1.getSelectedIndex()].getImage().getScaledInstance(250, 200, Image.SCALE_SMOOTH)));
			}
		});

		add(strCmb1);
		add(imglbl);
		
		setSize(300, 300);
		setVisible(true);
	}
	public static void main(String[] args) {
		new Java0529_JComboBox4();
		
	}
}
