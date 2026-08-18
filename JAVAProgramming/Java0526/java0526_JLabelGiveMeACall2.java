import java.awt.BorderLayout;
import java.awt.FlowLayout;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.SwingConstants;

public class java0526_JLabelGiveMeACall2 extends JFrame {
	public java0526_JLabelGiveMeACall2() {
		setTitle("이미지 버튼 예제");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setLayout(new BorderLayout());
		
		ImageIcon icon = new ImageIcon("images/normalIcon.gif");
		ImageIcon rollover = new ImageIcon("images/rolloverIcon.gif");
		ImageIcon pressed = new ImageIcon("images/pressedIcon.gif");
		
		JButton btn = new JButton("저나해~~~~~", icon);
		btn.setHorizontalAlignment(SwingConstants.LEFT);
		btn.setVerticalAlignment(SwingConstants.TOP);
	
		btn.setRolloverIcon(rollover);
		btn.setPressedIcon(pressed);
	
		add(btn);
		setSize(300, 150);
		setVisible(true);
	}
	public static void main(String[] args) {
		new java0526_JLabelGiveMeACall2();
	}

}
