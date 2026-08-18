import java.awt.Color;
import java.awt.Container;
import java.awt.Dimension;
import java.awt.FlowLayout;

import javax.swing.BorderFactory;
import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.SwingConstants;

public class java0526_JLabelLove extends JFrame{
	public java0526_JLabelLove() {
		setTitle("레이블 예제");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setLayout(new FlowLayout());
		
		JLabel lbl1 = new JLabel("사랑합니다.");
		ImageIcon image = new ImageIcon("images/beauty.jpg");
		
		JLabel lbl2 = new JLabel(image);
		ImageIcon icon = new ImageIcon("images/normalIcon.gif");
		
		JLabel lbl3 = new JLabel("보고 싶으면 전화하세요.", icon, SwingConstants.CENTER);
		lbl3.setBorder(BorderFactory.createLineBorder(Color.BLUE));
//		lbl3.setSize(new Dimension(350, 100));
		lbl3.setPreferredSize(new Dimension(350, 100));
		
		
		add(lbl1);
		add(lbl2);
		add(lbl3);
		setSize(400, 600);
		setVisible(true);	
	}
	
	public static void main(String[] args) {
		new java0526_JLabelLove();
	}
}
