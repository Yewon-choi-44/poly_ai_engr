import java.awt.Color;
import java.awt.Container;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.SwingConstants;

public class Java0522_SixthSwing extends JFrame{
	private JLabel la = new JLabel();
	private Container c;
	
	public Java0522_SixthSwing() {
		setTitle("Key Code 예제: F1: 초록색, % 키 노란색");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		c = getContentPane();
		
		c.addKeyListener(new KeyAdapter() {
		public  void keyPressed(KeyEvent e) {
			la.setText(e.getKeyText(e.getKeyCode()));
			
			if(e.getKeyChar() == '%') {
				c.setBackground(Color.YELLOW);
			}
			else if(e.getKeyCode() == KeyEvent.VK_F1) {
				c.setBackground(Color.GREEN);
			}
		}
		});
		c.add(la);
		
		setSize(300,150);
		setVisible(true);
		
		c.setFocusable(true);
		c.requestFocus();
	}
	
	public static void main(String[] args) {
		new Java0522_FifthSwing();

	}
}
