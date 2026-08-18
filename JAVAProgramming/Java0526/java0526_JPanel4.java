import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;

import javax.swing.ButtonGroup;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JRadioButton;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;

public class java0526_JPanel4 extends JFrame {
	JTextField tf = new JTextField(20);
	JTextArea ta = new JTextArea(7, 20);
	
	public java0526_JPanel4() {
		setTitle("텍스트 필드 만들기");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setLayout(new FlowLayout());
		
		JLabel lbl = new JLabel("입력 후 <Enter>키를 입력하세요.");
		JScrollPane jsp = new JScrollPane(ta);
		
		tf.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				ta.append(tf.getText() + "\n");
				tf.setText("");
			}
		});
		
		add(lbl);
		add(tf);
		add(jsp);
		
		setSize(300, 250);
		setVisible(true);
	}
	
	public static void main(String[] args) {
		new java0526_JPanel4();
	}
}
