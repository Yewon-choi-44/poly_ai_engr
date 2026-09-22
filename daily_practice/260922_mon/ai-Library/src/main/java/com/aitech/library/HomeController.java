package com.aitech.library;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class HomeController {
	
	@RequestMapping("/")
	public String home() {
		return "redirect:booklist";
	}
	
	@RequestMapping("/loginmember")
	public String loginmember() {
		return "login_member";
	}

	
	@RequestMapping("/registermember")
	public String registermember() {
		return "register_member";
	}

	@RequestMapping("/findpassword")
	public String findpassword() {
		return "find_password";
	}
	
	@RequestMapping("/modifymember")
	public String modifymember() {
		return "modify_member";
	}

}