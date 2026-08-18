package com.sms.model;

public class AdminDTO {
	String admin_id;
	String password;
	String admin_name;
	
	public AdminDTO(String admin_id, String password, String admin_name) {
//		super();
		this.admin_id = admin_id;
		this.password = password;
		this.admin_name = admin_name;
	}

	/**
	 * @return the admin_id
	 */
	public String getAdmin_id() {
		return admin_id;
	}

	/**
	 * @param admin_id the admin_id to set
	 */
	public void setAdmin_id(String admin_id) {
		this.admin_id = admin_id;
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
	 * @return the admin_name
	 */
	public String getAdmin_name() {
		return admin_name;
	}

	/**
	 * @param admin_name the admin_name to set
	 */
	public void setAdmin_name(String admin_name) {
		this.admin_name = admin_name;
	}

}
