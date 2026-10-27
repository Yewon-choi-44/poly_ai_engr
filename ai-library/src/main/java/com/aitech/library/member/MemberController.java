package com.aitech.library.member;

import com.aitech.library.book.BookController;
import java.util.UUID;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.dao.DuplicateKeyException;
import org.springframework.mail.MailException;
import org.springframework.mail.SimpleMailMessage;
import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;


import jakarta.servlet.http.HttpSession;

@Controller
public class MemberController {
	
	private final BookController bookController;

	@Autowired
	private MemberDao memberDao;
	
	@Autowired
	private BCryptPasswordEncoder passwordEncoder;
	
	@Autowired
	private JavaMailSender mailSender;

	MemberController(BookController bookController) {
		this.bookController = bookController;
	}
	
	@RequestMapping("/registermember")
	public String registerMember() {
		return "user/register_member";
	}
	@RequestMapping("/registermemberconfirm")
	public String registerMemberConfirm(MemberVo memberVo) {
		memberVo.setM_pw(passwordEncoder.encode(memberVo.getM_pw()));
		try {
			memberDao.insertMember(memberVo);
		} catch (DuplicateKeyException e) {
			return "redirect:/registermember";
		}
		return "redirect:/loginmember";
	}
	
	@RequestMapping("/modifymember")
	public String modifyMember(@RequestParam("m_no") int m_no, Model model) {
		MemberVo member = memberDao.getDetailMember(m_no);
		if(member == null)
			return "redirect/booklist";
		model.addAttribute("member", member);
		return "user/modify_member";
	}

	@RequestMapping("/modifymemberconfirm")
	public String modifyMemberConfirm(MemberVo memberVo) {
		if (memberVo.getM_pw() == null || memberVo.getM_pw().isEmpty()) {
			MemberVo oldMember = memberDao.getDetailMember(memberVo.getM_no());
			memberVo.setM_pw(oldMember.getM_pw());
		} else {
			memberVo.setM_pw(passwordEncoder.encode(memberVo.getM_pw()));
		}
		memberDao.updateMember(memberVo);
		return "redirect:/booklist";
	}
	
	@RequestMapping("/checkid")
	@ResponseBody
	public String checkId(@RequestParam("m_id") String m_id) {
		return String.valueOf(memberDao.countById(m_id));
	}
	
	@RequestMapping("/loginmember")
	public String loginMember() {
		return "user/login_member";
	}
	
	@RequestMapping("/loginmemberconfirm")
	public String loginMemberConfirm(@RequestParam("m_id") String m_id, @RequestParam("m_pw") String m_pw, HttpSession session) {
		MemberVo member = memberDao.getMemberById(m_id);
//		if (member != null && member.getM_pw().equals(m_pw)) {
		if (member != null && passwordEncoder.matches(m_pw, member.getM_pw())) {
			session.setAttribute("loginMember", member);
			return "redirect:/booklist";
		}
		return "user/login_member";
	}
	
	@RequestMapping("/logoutmember")
	public String logoutMember(HttpSession session) {
		session.invalidate();
		return "redirect:/booklist";
	}
	
	@RequestMapping("/findpassword")
	public String findpassword() {
		return "user/find_password";
	}
	
	@RequestMapping("/findpasswordconfirm")
	public String findpasswordconfirm(
			@RequestParam("m_id") String m_id, @RequestParam("m_mail") String m_mail) {
		MemberVo member = memberDao.getMemberByIdMail(m_id, m_mail);
		if (member == null) {
			System.out.println("ssssssssssssssssssssssssssssssssssssssssss"); 
			
			return "redirect:/findpassword";
	}
	
	String tempPw = UUID.randomUUID().toString().substring(0, 8);
		
	SimpleMailMessage message = new SimpleMailMessage();
	message.setTo(member.getM_mail());
	message.setSubject("[AITECH 도서관] 임시 비밀번호 안내");
	message.setText("[AITECH 도서관]의 비밀번호가 다음과 같이 초기화 되었습니다.\n임시 비밀번호: " + tempPw 
			+ "\n이 비밀번호로 로그인한 뒤, 정보 수정에서 새 비밀번호로 변경해주세요.");
	try {
		mailSender.send(message);
	} catch (MailException e) {
		e.printStackTrace();
		return "redirect:/findpassword";		
	}		
	memberDao.updatePassword(member.getM_no(), passwordEncoder.encode(tempPw));
	return "redirect:/loginmember";

}
}