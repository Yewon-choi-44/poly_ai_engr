import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Container;
import java.awt.FlowLayout;

import javax.swing.JButton;
import javax.swing.JFrame;

public class Java0522_Swing4 extends JFrame {
	public Java0522_Swing4() {
		setTitle("스윙 프레임 만들기");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setSize(300, 300);
		
		Container c = getContentPane();
		c.setBackground(Color.ORANGE);
		c.setLayout(new BorderLayout());
	
		
//		setLayout(new FlowLayout());
		
		JButton jb1 = new JButton("add");
		JButton jb2 = new JButton("sub");
		JButton jb3 = new JButton("mul");
		JButton jb4 = new JButton("div");
		JButton jb5 = new JButton("calculate");
		
//		jb1.setBackground(Color.GRAY);
		
		c.add(jb1, BorderLayout.NORTH);
		c.add(jb2, BorderLayout.SOUTH);
		c.add(jb3, BorderLayout.EAST);
		c.add(jb4, BorderLayout.WEST);
		c.add(jb5, BorderLayout.CENTER);
		setVisible(true);
	}
	public static void main(String[] args) {
		new Java0522_Swing4();
	}
}

