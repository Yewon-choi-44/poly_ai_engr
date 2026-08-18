import java.awt.Color;
import java.awt.Container;
import java.awt.FlowLayout;

import javax.swing.JButton;
import javax.swing.JFrame;

public class Java0522_Swing3 extends JFrame {
	public Java0522_Swing3() {
		setTitle("스윙 프레임 만들기");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setSize(300, 300);
		
		Container c = getContentPane();
		c.setBackground(Color.ORANGE);
		c.setLayout(new FlowLayout(FlowLayout.LEFT, 30, 40));
		
		
		String txts[] = {"add", "sub", "mul", "div", "calculate"};
		JButton btns[] = new JButton[5];
		for (int i=0 ; i<btns.length ; i++) {
			btns[i] = new JButton(Integer.toString(i+1));
			c.add(btns[i]);
		}
		
		setLayout(new FlowLayout());
		
		JButton jb1 = new JButton("add");
		JButton jb2 = new JButton("sub");
		JButton jb3 = new JButton("mul");
		JButton jb4 = new JButton("div");
		JButton jb5 = new JButton("calculate");
		
		jb1.setBackground(Color.GRAY);
		
		c.add(jb1);
		c.add(jb2);
		c.add(jb3);
		c.add(jb4);
		c.add(jb5);
		setVisible(true);
	}
	public static void main(String[] args) {
		new Java0522_Swing3();
	}
}

