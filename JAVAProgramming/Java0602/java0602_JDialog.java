import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JFrame;
import javax.swing.JTextArea;
import javax.swing.JTextField;

class MyDialog extends JDialog{
	public MyDialog(String title) {
		setTitle(title);
		setLayout(new FlowLayout());
		JTextField tf = new JTextField(10);
		JButton okbtn = new JButton("OK");
		okbtn.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				setVisible(false);
			}
		});
		
		add(tf);
		add(okbtn);
		setSize(250, 100);
		setVisible(true);
	}
}

public class java0602_JDialog extends JFrame{
	MyDialog dialog;
	public java0602_JDialog(){
		setTitle("dialog 예제");
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setSize(300, 150);
		setLayout(new FlowLayout());
		
		dialog = new MyDialog("Test Dialog");
		JButton btn = new JButton("show Dialog");
		btn.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				dialog.setVisible(true);
				
			}
		});
		add(btn);
		setVisible(true);
	}
	public static void main(String[] args) {
		new java0602_JDialog();
	}

}
