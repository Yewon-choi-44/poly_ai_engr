import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

public class java0526_JPanel extends JFrame {
	JButton btn;
	JLabel img;
	public java0526_JPanel() {
		setTitle("샘플");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setLayout(new BorderLayout());
		
		JPanel jp1 = new JPanel();
		JPanel jp2 = new JPanel();
		jp1.setBackground(Color.LIGHT_GRAY);
		
		btn = new JButton("클릭");
		img = new JLabel("");
		
		btn.addActionListener(new ActionListener() {			
			public void actionPerformed(ActionEvent e) {
				ImageIcon imgicon = new ImageIcon("images/banana.jpg");
				img.setIcon(imgicon);
			}
		});
		
		jp1.add(btn);
		jp2.add(img);
		add(jp1, BorderLayout.NORTH);
		add(jp2, BorderLayout.CENTER);
		setSize(300, 250);
		setVisible(true);
	}
	
	public static void main(String[] args) {
		new java0526_JPanel();
	}

}
