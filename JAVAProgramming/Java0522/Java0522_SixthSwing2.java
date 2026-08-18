import java.awt.Color;
import java.awt.Container;
import java.awt.FlowLayout;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.SwingConstants;

public class Java0522_SixthSwing2 extends JFrame{
	public Java0522_SixthSwing2() {
		setTitle("키로 배경 바꾸기");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setLayout(new FlowLayout());
		
		Container c = getContentPane();
		JLabel lbl = new JLabel("F1 초록 / % 노랑");
		
		addKeyListener(new KeyAdapter() {
			public void keyPressed(KeyEvent e) {
				lbl.setText(e.getKeyText(e.getKeyCode()));
				if(e.getKeyCode()==112) {
					c.setBackground(Color.GREEN);
				}
				else if(e.getKeyCode() == 53) {
					c.setBackground(Color.YELLOW);
				}
				else if(e.getKeyCode() == 27) {
					c.setBackground(defaultColor);
				}
			}
			setSize(300,200);
			setVisible(true);
		});
		
	
		
	
	public static void main(String[] args) {
		new Java0522_SixthSwing2();

	}
	}
	
}
