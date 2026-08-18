package com.sms.controller;

import java.awt.HeadlessException;
import java.awt.Menu;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.JTextPane;

import com.sms.model.AdminDTO;
import com.sms.model.StudentDAO;
import com.sms.model.StudentDTO;
import com.sms.view.DeptStudentView;
import com.sms.view.EditView;
import com.sms.view.LoginView;
import com.sms.view.MainView;
import com.sms.view.StudentRegisterView;

public class MainController extends JFrame {
	private MainView mainView;
	private StudentDTO currentStudent;
	private StudentDAO admin;
	private EditView editView;
	private String userRole;

	
	
	// 관리자 로그인시 사용
	public MainController(MainView mainView, String userRole) {
		this.mainView = mainView;
		this.userRole = userRole;

		this.mainView.addMenuListener(new MenuActionListener());
	}

	// 학생 로그인시 사용
	public MainController(MainView mainView, StudentDTO currentStudent, EditView editView, String userRole) {
		this.mainView = mainView;
		this.editView = editView;
		this.currentStudent = currentStudent;
		this.userRole = userRole;
		this.mainView.addMenuListener(new MenuActionListener());
	}
	
	

	public class MenuActionListener implements ActionListener {
		@Override
		public void actionPerformed(ActionEvent e) {
			System.out.println("---------" + e.getSource());
			if (e.getSource() == mainView.getButtonLogout()) {
				LogOut();
			} else if (e.getSource() == mainView.getButtonEditInfo()) {
				EditInfo();
			} else if (e.getSource() == mainView.getBtnRegisterStudent()) {
				System.out.println("추가");
				RegisterStudent();
			} else if(e.getSource()==mainView.getbtnSearchDeptStudent()) {
				SearchDept();
			}
		}

		private void SearchDept() {
			DeptStudentView deptview = new DeptStudentView(mainView);
			deptview.setVisible(true);
		}

		private void RegisterStudent() {
			StudentDAO dao = new StudentDAO();
			StudentRegisterView registerview = new StudentRegisterView(mainView, dao.getDeptList());
			registerview.addRegisterListener(new ActionListener() {
				@Override
				public void actionPerformed(ActionEvent e) {
					String[] data = registerview.getData();
					StudentDTO registerStudent = new StudentDTO(data[0],data[1],data[2],data[3],data[4]);
				
				if(dao.insertStudent(registerStudent)) {
					registerview.dispose();
				}
				}
			});
			
			registerview.setVisible(true);

		}

		private void LogOut() {
			if (JOptionPane.showConfirmDialog(mainView, "로그아웃 하시겠습니까?", "로그아웃",
					JOptionPane.YES_NO_OPTION) == JOptionPane.YES_NO_OPTION) {

				mainView.dispose();
				StudentDAO studentDAO = new StudentDAO();
				LoginView loginView = new LoginView();
				new LoginController(studentDAO, loginView);

				loginView.setVisible(true);
			}
		}

		private void EditInfo() {
				EditView editView = new EditView(mainView, currentStudent);
				editView.addSaveButtonListener(new ActionListener() {
					@Override
					public void actionPerformed(ActionEvent e) {
						StudentDTO updateData = editView.getUpddateData();
						System.out.println("contro" + updateData);
						StudentDAO studentDAO = new StudentDAO();
						boolean success = studentDAO.updateStudent(updateData);
						if(success) {
							editView.dispose();
					}
				});
//				mainView.dispose();
//				StudentDAO studentDAO = new StudentDAO();
//				EditView editView = new EditView();
				editView.setVisible(true);
				}
		}
	}
}
