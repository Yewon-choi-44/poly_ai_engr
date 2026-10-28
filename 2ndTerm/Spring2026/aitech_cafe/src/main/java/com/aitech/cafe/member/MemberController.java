package com.aitech.cafe.member;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import jakarta.servlet.http.HttpSession;

@Controller
public class MemberController {
	@Autowired
	private MemberDao memberDao;
	
	@RequestMapping("/loginmember")
	public String loginmember() {
		return "member/login_member";
	}
	
	@RequestMapping("/menulist")
	public String menulist() {
		return "menu/menu_list";
	}

	@RequestMapping("/loginmemberconfirm")
	public String testlogin(@RequestParam("m_id") String m_id, @RequestParam("m_pw") String m_pw, HttpSession session) {
		MemberVo member = memberDao.getMemberById(m_id);
		if (member != null && member.getM_pw().equals(m_pw)) {
			session.setAttribute("loginMember", member);
			return "redirect:/menulist";
		}
		return "member/login_member";
	}
	
	@RequestMapping("logoutmember")
	public String logoutmember(HttpSession session) {
		session.invalidate();
		return "redirect:/menulist";
	}
}
