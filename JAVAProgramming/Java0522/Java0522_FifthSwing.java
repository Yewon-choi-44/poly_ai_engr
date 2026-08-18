import java.awt.Font;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

import javax.swing.JFrame;
import javax.swing.JLabel;

public class Java0522_FifthSwing extends JFrame {
	public Java0522_FifthSwing() {
		setTitle("keyListner");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setSize(300,150);
		
		Font f = new Font("돋움",  Font.BOLD, 30);
		String txt_m[] = {"getKeyCode", "getKeyChar","getKeyText"};
		JLabel key_m[] = new JLabel[3];
		for(int i=0; i < key_m.length; i++) {
			key_m[i] = new JLabel(txt_m[i]);
			key_m[i].setFont(f);
			add(key_m[i]);
		}
		
		addKeyListener(new KeyAdapter() {
			public void keyPressed(KeyEvent e) {
				key_m[0].setText(Integer.toString(e.getKeyCode()));
				key_m[1].setText(Character.toString(e.getKeyChar()));
				key_m[2].setText(e.getKeyText(e.getKeyCode()));
			}
		});
		
		setVisible(true);
	}
	
	public static void main(String[] args) {
		new Java0522_FifthSwing();
	}

}
