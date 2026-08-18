//import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Container;
//import java.awt.FlowLayout;
import java.awt.GridLayout;

//import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextField;

public class Java0522_Swing5 extends JFrame {
	public Java0522_Swing5() {
		setTitle("스윙 프레임 만들기");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setSize(300, 300);
		
		Container c = getContentPane();
//		c.setBackground(Color.ORANGE);
		GridLayout grid = new GridLayout(4,2);
		c.setLayout(grid);
		
		JLabel[] lb = new JLabel[4];
		JTextField[] jf = new JTextField[4];
		
		for (int i=0 ; i < jf.length ; i++) {
			lb[i] = new JLabel("레이블"+Integer.toString(i+1));
			jf[i] = new JTextField();
			c.add(jf[i]);
			c.add(jf[i]);
			grid.setVgap(10);
		}
		setVisible(true);
	}
	public static void main(String[] args) {
		new Java0522_Swing5();
	}
}

