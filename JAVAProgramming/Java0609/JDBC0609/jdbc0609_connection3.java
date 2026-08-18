import java.sql.Statement;

import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextField;

import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;

public class jdbc0609_connection3 extends JFrame{
	JTextField tf_name;
	JComboBox<String> cb_dept;
	JButton btn1;
	JButton btn2;
	
	public jdbc0609_connection3() {
		setTitle("입력");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setSize(300, 200);
		setLayout(new FlowLayout());
	
		JLabel lbl_name = new JLabel("성명");
		tf_name = new JTextField(20);
		JLabel lbl_dept = new JLabel("학과");
		String[] dept_values = {"AI엔지니어링", "소프트웨어공학"};
		
		cb_dept = new JComboBox<String>(dept_values);
		cb_dept.setPreferredSize(new Dimension(220, 25));
		
		btn1 = new JButton("입력");
		btn2 = new JButton("c취소");
		btn1.setPreferredSize(new Dimension(100, 30));
		btn2.setPreferredSize(new Dimension(100, 30));
		
		btn1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				try {
					Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/madang", "root", "#mysql123");
					Statement stmt = conn.createStatement();
					stmt.executeUpdate("insert into sample(username, dept)"
					+ "values('" + tf_name.getText() + "','" 
					+ cb_dept.getSelectedItem() + "')");
					conn.close();
				} catch (SQLException e1) {
					e1.printStackTrace();
				}
			}
		});
		
		btn2.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				
			}
		});
		
		
		add(lbl_name);
		add(tf_name);
		add(lbl_dept);
		add(cb_dept);
		add(btn1);
		add(btn2);
		setVisible(true);
	}
	private <conn> void DBconnection() {
		
	}

	public static void main(String[] args) {
		new jdbc0609_connection3();
	}
}

