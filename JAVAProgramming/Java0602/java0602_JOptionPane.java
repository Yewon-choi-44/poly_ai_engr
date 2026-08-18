import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.accessibility.AccessibleIcon;
import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextArea;
import javax.swing.JTextField;

public class java0602_JOptionPane extends JFrame{
	public java0602_JOptionPane(){
		setTitle("옵션팬 예제");
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setSize(500, 200);
		setLayout(new BorderLayout());

		JPanel jp1 = new JPanel();
		JPanel jp2 = new JPanel();
		
		jp1.setBackground(Color.LIGHT_GRAY);
		
		
		String[] btn_txts = {"Input Name", "Confirm", "Message"};
		JButton[] btns = new JButton[btn_txts.length];
		JTextField tf = new JTextField(10);

		for(int i=0 ; i<btns.length;i++) {
			btns[i] = new JButton(btn_txts[i]);
			btns[i].addActionListener(new ActionListener() {
				@Override
				public void actionPerformed(ActionEvent e) {
					if(e.getSource().equals(btns[0])) {
						String result = JOptionPane.showInputDialog("이름을 입력하세요.");
						tf.setText(result);
					} else if (e.getSource().equals(btns[1])) {
						int result = JOptionPane.showConfirmDialog(null, "계속할건가?", "Confirm", JOptionPane.YES_NO_OPTION);
						if(result == JOptionPane.YES_OPTION) {
							tf.setText("ㅖ.");
						} else {
							tf.setText("ㄴ.");							
						}
					} else if (e.getSource().equals(btns[2])) {
						JOptionPane.showConfirmDialog(null, "다시봐","Message", JOptionPane.ERROR_MESSAGE);
					}
				}
			});
			jp1.add(btns[i]);
		}
		
		
		jp1.add(tf);
		add(jp1, BorderLayout.NORTH);
		add(jp2, BorderLayout.CENTER);
		setVisible(true);
	}
	public static void main(String[] args) {
		new java0602_JOptionPane();
	}

}
