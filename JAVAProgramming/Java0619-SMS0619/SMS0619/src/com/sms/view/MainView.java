package com.sms.view;

import java.awt.BorderLayout;
import java.awt.Font;
import java.awt.Image;
import java.awt.event.ActionListener;

import javax.swing.BorderFactory;
import javax.swing.Icon;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JToolBar;

import com.sms.controller.MainController;

public class MainView extends JFrame{
	private JToolBar toolBar = new JToolBar();
	private JPanel contentP = new JPanel();
	private JLabel lbl = new JLabel("", JLabel.CENTER);
	
	private JButton btnEditInfo = new JButton("학생정보수정"); // 학생용
	private JButton btnStudentDept = new JButton("학과학생조회"); // 관리자용
	private JButton btnRegisterStudent = new JButton("학생정보추가"); // 관리자용
	private JButton btnLogout = new JButton("로그아웃"); //누구나
	
	public MainView(String name, String role) {
		setTitle("학생 관리 시스템 - 메인(" + role + ")");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setSize(700, 450);
		setLocationRelativeTo(null);
		setLayout(new BorderLayout());
		
		loadAndSetIcon();
		
		toolBar.setFloatable(false);
		toolBar.setBorder(BorderFactory.createEmptyBorder(5, 5, 5, 5));
		
		if(role.equals("학생")) {
			toolBar.add(btnEditInfo);
//			toolBar.add(btnStudentDept);
//			toolBar.add(btnRegisterStudent);
			
		} else {
//			toolBar.add(btnEditInfo);
			toolBar.add(btnStudentDept);
			toolBar.add(btnRegisterStudent);
		}

		toolBar.add(btnLogout);
		
		add(toolBar, BorderLayout.NORTH);
		lbl.setText("님, 환영합니다.");
		lbl.setFont(new Font("맑은 고딕", Font.BOLD, 20));
		contentP.add(lbl, BorderLayout.CENTER);
		add(contentP, BorderLayout.CENTER);
	}

	private void loadAndSetIcon() {
		int width = 30;
		int height = 30;
		btnEditInfo.setIcon(createIcon("images/edit.png", width, height));
		btnStudentDept.setIcon(createIcon("images/dept.png", width, height));
		btnRegisterStudent.setIcon(createIcon("images/add.png", width, height));
		btnLogout.setIcon(createIcon("images/logout.png", width, height));
	}
	
	private Icon createIcon(String path, int width, int height) {
		ImageIcon icon = new ImageIcon(path);
		Image img = icon.getImage().getScaledInstance(width, height, Image.SCALE_SMOOTH);
		return new ImageIcon(img);
	}
	
	public void addMenuListener(ActionListener listener) {
		btnLogout.addActionListener(listener);
		btnEditInfo.addActionListener(listener);
		btnRegisterStudent.addActionListener(listener);
		btnStudentDept.addActionListener(listener);
	}
	
	public JButton getButtonLogout() {
		return btnLogout;
	}
	
	public JButton getButtonEditInfo() {
		return btnEditInfo;
	}

	public JButton getBtnRegisterStudent() {
		return btnRegisterStudent;
	}

	public JButton getbtnSearchDeptStudent() {
		return btnStudentDept;
	}
	

}
