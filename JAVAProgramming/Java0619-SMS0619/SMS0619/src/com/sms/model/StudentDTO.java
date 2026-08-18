package com.sms.model;

public class StudentDTO {
	String student_id;
	String password;
	String name;
	String dept_code;
	String phone;
	
	public StudentDTO(String student_id, String password, String name, String dept_code, String phone) {
		this.student_id = student_id;
		this.password = password;
		this.name = name;
		this.dept_code = dept_code;
		this.phone = phone;
	}
	/**
	 * @return the student_id
	 */
	public String getStudent_id() {
		return student_id;
	}
	/**
	 * @param student_id the student_id to set
	 */
	public void setStudent_id(String student_id) {
		this.student_id = student_id;
	}
	/**
	 * @return the password
	 */
	public String getPassword() {
		return password;
	}
	/**
	 * @param password the password to set
	 */
	public void setPassword(String password) {
		this.password = password;
	}
	/**
	 * @return the name
	 */
	public String getName() {
		return name;
	}
	/**
	 * @param name the name to set
	 */
	public void setName(String name) {
		this.name = name;
	}
	/**
	 * @return the dept_code
	 */
	public String getDept_code() {
		return dept_code;
	}
	/**
	 * @param dept_code the dept_code to set
	 */
	public void setDept_code(String dept_code) {
		this.dept_code = dept_code;
	}
	/**
	 * @return the phone
	 */
	public String getPhone() {
		return phone;
	}
	/**
	 * @param phone the phone to set
	 */
	public void setPhone(String phone) {
		this.phone = phone;
	}
	
}
