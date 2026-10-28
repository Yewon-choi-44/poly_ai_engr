package com.aitech.library;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class HomeController {
	
	@RequestMapping("/")
	public String home() {
		return "home";
	}
	
	@RequestMapping("/loginmember")
	public String loginmember() {
		return "login_member";
	}
	
	@RequestMapping("/booklist")
	public String booklist() {
		return "book_list";
	}
	
	@RequestMapping("/registermember")
	public String registermember() {
		return "register_member";
	}
	
	@RequestMapping("/modifymember")
	public String modifymember() {
		return "modify_member";
	}
	
	@RequestMapping("/findpassword")
	public String findpassword() {
		return "find_password";
	}
}
