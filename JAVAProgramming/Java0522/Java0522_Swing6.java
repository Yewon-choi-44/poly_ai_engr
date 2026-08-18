//import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Container;
//import java.awt.FlowLayout;
import java.awt.GridLayout;

//import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextField;

public class Java0522_Swing6 extends JFrame {
	public Java0522_Swing6() {
		setTitle("스윙 프레임 만들기");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setSize(300, 200);
		GridLayout grid = new GridLayout(4,2);
		
		grid.setVgap(5);
		Container c = getContentPane();
		c.setLayout(grid);
		
		String[] txts = {"이름", "학번", "학과", "과목"}; 
		for(int i=0 ; i < txts.length ; i++) {
			c.add(new JLabel(" "+txts[i]));
			c.add(new JTextField());
		}
		
		setVisible(true);
	}
	public static void main(String[] args) {
		new Java0522_Swing6();
	}
}

