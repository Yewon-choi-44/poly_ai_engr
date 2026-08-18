import java.awt.FlowLayout;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;

public class java0526_JLabelGiveMeACall extends JFrame {
	public java0526_JLabelGiveMeACall() {
		setTitle("이미지 버튼 예제");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setLayout(new FlowLayout());
		
		ImageIcon icon = new ImageIcon("images/normalIcon.gif");
		ImageIcon rollover = new ImageIcon("images/rolloverIcon.gif");
		ImageIcon pressed = new ImageIcon("images/pressedIcon.gif");
		
		JButton btn = new JButton("저나해~~~~~", icon);
		btn.setRolloverIcon(rollover);
		btn.setPressedIcon(pressed);
		add(btn);
		setSize(300, 150);
		setVisible(true);
	}
	public static void main(String[] args) {
		new java0526_JLabelGiveMeACall();
	}

}
