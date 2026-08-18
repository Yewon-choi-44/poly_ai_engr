import java.awt.Color;
import java.awt.FlowLayout;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;

public class java0526_Swing extends JFrame{
	public java0526_Swing() {
		setTitle("공통 메소드");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setLayout(new FlowLayout());
		
		JButton btn1 = new JButton("Megenta/Yellow Button");
		JButton btn2 = new JButton("Disabled Button");
		JButton btn3 = new JButton("getX(), getY()");	
		
		btn1.setBackground(Color.YELLOW);
		btn1.setForeground(Color.MAGENTA);
		btn1.setFont(new Font("Arial", Font.ITALIC, 20));
		
		btn2.setEnabled(false);
		btn3.addActionListener(new ActionListener() {			
			public void actionPerformed(ActionEvent e) {
				JButton b = (JButton) e.getSource();
				setTitle(b.getX() + "," + b.getY());				
			}
		});
		
		add(btn1);
		add(btn2);
		add(btn3);
		setSize(260, 200);
		setVisible(true);
	}
	
	public static void main(String[] args) {
		new java0526_Swing();
	}
}
