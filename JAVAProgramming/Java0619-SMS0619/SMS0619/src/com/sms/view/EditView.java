package com.sms.view;

import java.awt.BorderLayout;
import java.awt.Font;
import java.awt.GridLayout;
import java.awt.event.ActionListener;

import javax.swing.ButtonGroup;
import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JPasswordField;
import javax.swing.JRadioButton;
import javax.swing.JTextField;

import com.sms.model.StudentDTO;

public class EditView extends JDialog {
	private JPasswordField txtPassword;
	private JTextField txtId;
	private JTextField txtPhone;
	private JButton btnSave = new JButton("수정");
	
//	private ButtonGroup roleGroup = new ButtonGroup();
	private JRadioButton rbStudent = new JRadioButton("학생", true);
	private JRadioButton rbAdmin = new JRadioButton("관리자");
	private JButton btnLogin = new JButton("로그인");

	private StudentDTO student;
	

	public EditView(JFrame parent, StudentDTO student) {
		super(parent, "학생 정보 수정", true);
		this.student = student;
		
		setLayout(new BorderLayout());
		setLocationRelativeTo(parent);
		setSize(350, 200);
		
		
		setTitle("학생정보수정");
		setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
		
		JLabel lblTitle = new JLabel("학생 관리 시스템", JLabel.CENTER); // 내용 가운데
		lblTitle.setFont(new Font("맑은 고딕", Font.BOLD, 18));
		
		JPanel contentE = new JPanel(new GridLayout(4, 2, 10, 10));
		contentE.add(new JLabel("학번:" + txtId));
		contentE.add(new JLabel(student.getStudent_id()));
		contentE.add(new JLabel("비밀번호:"));
		txtPassword = new JPasswordField(student.getPassword());
		contentE.add(txtPassword);

		contentE.add(new JLabel("연락처:"));
		txtPhone = new JTextField(student.getPhone());
		contentE.add(txtPhone);
	
		add(contentE, BorderLayout.CENTER);
		add(btnSave, BorderLayout.SOUTH);
		
	}
	
	public void addSaveButtonListener(ActionListener listener) {
		btnSave.addActionListener(listener);
	}
//	
//	public String getId() {
//		return txtId.getText().trim();
//	}
	
	public String getPassword() {
		return new String(txtPassword.getPassword());
	}
	
	public String getPhone() {
		return new String(txtPhone.getPhone().trim());
	}
//	
	public String getSelectRole() {
//		System.out.println("++++++++++++++++" + rbStudent.isSelected());
		return rbStudent.isSelected() ? "학생" : "관리자";
	}
	
	public void addLoginListener(ActionListener listener) {
		btnLogin.addActionListener(listener);
	}
	
	public void showMessage(String message) {
		JOptionPane.showMessageDialog(this, message);
		
	}

	public StudentDTO getUpddateData() {
		System.out.println("update" + student.getStudent_id());
		return new StudentDTO(
				student.getStudent_id(), 
				new String(txtPassword.getPassword()),
				student.getName(),
				student.getDept_code(),
				txtPhone.getText()
				);
	}
	
	
	private void EditInfo(JFrame mainView, StudentDTO currentStudent) {
		
		EditView editView = new EditView(mainView, currentStudent);
		editView.addSaveButtonListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				StudentDTO updateData = editView.getUpddateData();
				StudentDAO studentDAO = new StudentDAO();
				boolean success = studentDAO.updateStudent(updateData);
				if(success) {
					editView.dispose();
				}
			});
		
		mainView.dispose();
//		StudentDAO studentDAO = new StudentDAO();
//		EditView editView = new EditView();
		editView.setVisible(true);
	}

}
