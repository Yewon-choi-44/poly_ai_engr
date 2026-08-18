import java.awt.Color;
import java.awt.Container;
import java.awt.FlowLayout;
import javax.swing.JButton;
import javax.swing.JFrame;

public class Java0522_Swing0522_1 extends JFrame {
	public Java0522_Swing0522_1() {
		setTitle("스윙 프레임 만들기");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setSize(300, 300);
		
		Container c = getContentPane();
		c.setBackground(Color.ORANGE);
		c.setLayout(new FlowLayout());
		
//		setLayout(new FlowLayout());
		
		JButton jb1 = new JButton("ok");
		jb1.setBackground(Color.GRAY);
//		JButton jb2 = new JButton("cancel");
//		JButton jb3 = new JButton("ignore");
//		
		c.add(jb1);
		c.add(new JButton("cancel"));
		c.add(new JButton("ignore"));
		setVisible(true);
	}
	public static void main(String[] args) {
		new Java0522_Swing0522_1();
	}

}
