import java.sql.Statement;

import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextField;

import java.awt.Dimension;
import java.awt.FlowLayout;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;

public class jdbc0609_connection2 extends JFrame{
	public jdbc0609_connection2() {
		setTitle("입력");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setSize(300, 200);
		setLayout(new FlowLayout());
		JLabel lbl_name = new JLabel("성명");
		JTextField tf_name = new JTextField(20);
		JLabel lbl_dept = new JLabel("학과");
		
		String[] dept_values = {"AI엔지니어링", "소프트웨어공학"};
		JComboBox<String> cb_dept = new JComboBox<String>(dept_values);
		cb_dept.setPreferredSize(new Dimension(220, 25));
		JButton btn = new JButton("입력");
		btn.setPreferredSize(new Dimension(150, 30));
		add(lbl_name);
		add(tf_name);
		add(lbl_dept);
		add(cb_dept);
		add(btn);
		setVisible(true);
	}
	public static void main(String[] args) {
		new jdbc0609_connection2();
	}
}

