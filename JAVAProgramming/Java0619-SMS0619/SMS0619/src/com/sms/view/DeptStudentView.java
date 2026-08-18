package com.sms.view;

import java.awt.BorderLayout;

import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JDialog;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.table.DefaultTableModel;

public class DeptStudentView extends JDialog{
	private JComboBox<String> comboDept = new JComboBox<String>();
	private JButton btnSearch = new JButton("조회");
	private JTable table;
	private DefaultTableModel model;
	
	
	public DeptStudentView(JFrame parent) {
		super(parent, "학과별 학생 조회", true);
		setLayout(new BorderLayout());
		JPanel northP = new JPanel();
		northP.add(comboDept);
		northP.add(btnSearch);
		add(northP, BorderLayout.NORTH);
		
		model = new DefaultTableModel(new String[] {"학번", "성명", "연락처"}, 0);
		table = new JTable(model);
		add(new JScrollPane(table), BorderLayout.CENTER);
		setSize(400, 300);
		setLocationRelativeTo(parent);
	}
}
