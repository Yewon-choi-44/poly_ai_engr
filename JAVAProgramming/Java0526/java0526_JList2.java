import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Vector;

import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JList;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;

public class java0526_JList2 extends JFrame{
	JTextField tf = new JTextField(10);
	Vector<String> v = new Vector<String>();
	JList<String> list = new JList<String>(v);
	
	public java0526_JList2() {
		setTitle("리스트 만들기");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setLayout(new FlowLayout());
		
		JLabel lbl = new JLabel("이름 입력 후 <Enter> 키");
//		list.setVisibleRowCount(5);
//		list.setFixedCellWidth(100); //엔터 치고 리스트 칸 어쩌구 뭐해주는거... 있이 돌려보고 없이 돌려보셈
		
		JScrollPane jsp = new JScrollPane(list);
	
		
		tf.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				v.add(tf.getText());
				list.setListData(v);
				tf.setText("");
			}
		});
		
		add(lbl);
		add(tf);		
		add(jsp);
		
		setSize(300, 300);
		setVisible(true);
	}
	public static void main(String[] args) {
		new java0526_JList2();
	}

}
