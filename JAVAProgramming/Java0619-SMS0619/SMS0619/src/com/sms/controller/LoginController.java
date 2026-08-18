package com.sms.controller;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import com.sms.model.AdminDTO;
import com.sms.model.StudentDAO;
import com.sms.model.StudentDTO;
import com.sms.view.LoginView;
import com.sms.view.MainView;

public class LoginController {
	private StudentDAO studentDao;
	private LoginView loginView;

	public LoginController(StudentDAO studentDao, LoginView loginView) {
		this.studentDao = studentDao;
		this.loginView = loginView;
		this.loginView.addLoginListener(new LoginActionListener());
	}

	private class LoginActionListener implements ActionListener {
		@Override
		public void actionPerformed(ActionEvent e) {
//			System.out.println("++++++++++++++++");
			String id = loginView.getId();
			String password = loginView.getPassword();
			String role = loginView.getSelectRole();
//			System.out.println("++++++++++++++++" + role);
			
			

			if (id.isEmpty() || password.isEmpty()) {
				loginView.showMessage("아이디와 빔리번호르 모두 입력하시오.");
				return;
			}

			if (role.equals("학생")) {
				StudentDTO student = studentDao.loginStudent(id, password);

				if (student != null) {
					loginView.showMessage(student.getName() + " 학생 환영합니다.");
					loginView.dispose();
					
					MainView mainView = new MainView(student.getName(), role);
					new MainController(mainView, student, null, "학생");
					mainView.setVisible(true);
					
				} else {
					loginView.showMessage("학번 또는 비밀번호를 확인하세요.");
				}

			} else if (role.equals("관리자")) {
//				System.out.println("didd");
				AdminDTO admin = studentDao.loginAdmin(id, password);
				if (admin != null)
					loginView.showMessage(admin.getAdmin_name() + " 관리자분 환영합니다.");
					loginView.dispose();
					
					MainView mainView = new MainView(admin.getAdmin_name(), role);
					new MainController(mainView, "관리자");
					mainView.setVisible(true);
					
				}else {
				loginView.showMessage("아이디 또는 비밀번호를 확인하세요.");
			} 
		}
	}

}
