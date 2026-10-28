package com.aitech.library.member;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.dao.DuplicateKeyException;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import jakarta.servlet.http.HttpSession;

@Controller
public class MemberController {

	@Autowired
	private MemberDao memberDao;

	@Autowired
	private BCryptPasswordEncoder passwordEncoder;

	@RequestMapping("/registermember")
	public String registermember() {
		return "user/register_member";
	}

	@RequestMapping("/registermemberconfirm")
	public String registermemberconfirm(MemberVo memberVo) {
		memberVo.setM_pw(passwordEncoder.encode(memberVo.getM_pw()));
		try {
			memberDao.insertMember(memberVo);
		} catch (DuplicateKeyException e) {
			return "redirect:/registermember";
		}
		return "user/register_member";
	}

	@RequestMapping("/checkid")
	@ResponseBody
	public String checkId(@RequestParam("m_id") String m_id) {
		return String.valueOf(memberDao.countById(m_id));
	}

	@RequestMapping("/loginmember")
	public String loginmember() {
		return "user/login_member";
	}

	@RequestMapping("/loginmemberconfirm")
	public String loginmemberconfirm(@RequestParam("m_id") String m_id, @RequestParam("m_pw") String m_pw,
			HttpSession session) {
		MemberVo member = memberDao.getMemberById(m_id);
		// if(member != null && member.getM_pw().equals(m_pw)) {
		if (member != null && passwordEncoder.matches(m_pw, member.getM_pw())) {
			session.setAttribute("loginMember", member);
			return "redirect:/booklist";
		}
		return "redirect:/loginmember";
	}

	@RequestMapping("/logoutmember")
	public String logoutmember(HttpSession session) {
		session.invalidate();
		return "redirect:/booklist";
	}

	@RequestMapping("/modifymember")
	public String modifymember(@RequestParam("m_no") int m_no, Model model) {
		MemberVo member = memberDao.getDetailMember(m_no);
		if (member == null)
			return "redirect:/booklist";
		model.addAttribute("member", member);
		return "user/modify_member";
	}

	@RequestMapping("/modifymemberconfirm")
	public String modifymemberconfirm(MemberVo memberVo) {
		if (memberVo.getM_pw() == null || memberVo.getM_pw().isEmpty()) {
			MemberVo oldmember = memberDao.getDetailMember(memberVo.getM_no());
			memberVo.setM_pw(oldmember.getM_pw());
		} else {
			memberVo.setM_pw(passwordEncoder.encode(memberVo.getM_pw()));
		}
		memberDao.updateMember(memberVo);
		return "redirect:/booklist";
	}

}
