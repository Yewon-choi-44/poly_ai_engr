import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import Java0522_ThirdSwing.MyActionListener;

public class Java0522_ThirdSwing extends JFrame {
	JButton btn;

	public Java0522_ThirdSwing() {
		setTitle("Action 이벤트 리스너");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setLayout(new FlowLayout());
		
//		JButton btn = new JButton("Action");
		btn = new JButton("Action");
		btn.addActionListener(new MyActionListener());
		add(btn);
		
		setSize(350, 150);
		setVisible(true);
	}
	
	
	private class MyActionListener implements ActionListener {
		public void actionPerformed(ActionEvent e) {
			
			if (btn.getText().equals("Action")) {
				btn.setText("액션");
			}
			else {
				btn.setText("Action");
			}
			
//			JButton e_btn = (JButton) e.getSource();
//			if(e_btn.getText().equals("Action")) {
//				e_btn.setText("액션");}
//			else {
//				e_btn.setText("Action");
//			}
	}
	}

	public static void main(String[] args) {
		new Java0522_ThirdSwing();
	}

}

