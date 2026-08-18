import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;

import javax.swing.JFrame;
import javax.swing.JLabel;

public class Java0522_ForthSwing extends JFrame{
	public Java0522_ForthSwing() {
		setTitle("Mouse 이벤트 예제");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setLayout(null);
		
		JLabel lbl = new JLabel("hello");
		lbl.setBounds(15, 15, 50, 20);
		addMouseMotionListener(new MouseAdapter() {
//			public void mouseClicked(MouseEvent e) {
//				int x = e.getX();
//				int y = e.getY();
//				System.out.println("좌표: "+x+", "+y);
//				lbl.setLocation(x, y);
//			}
			
			public void mouseDragged(MouseEvent e) {
				int x = e.getX() + lbl.getX();
				int y = e.getY() + lbl.getY();
				lbl.setLocation(x, y);
			}
		});
		add(lbl);
		
		setSize(300,300);
		setVisible(true);
	}
	
	public static void main(String[] args) {
		new Java0522_ForthSwing();
	}

}
