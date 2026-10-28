package com.aitech.library;

import org.springframework.web.servlet.HandlerInterceptor;

import com.aitech.library.member.MemberVo;

import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;

public class AdminCheckInterceptor implements HandlerInterceptor{
	public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
		HttpSession session = request.getSession();
		MemberVo loginMember = (MemberVo) session.getAttribute("loginMember");
		
		if (loginMember == null) {
			response.sendRedirect("/loginmember");
			return false;
		}
		
		if(!"ADMIN".equals(loginMember.getM_role())) {
			response.sendRedirect("/booklist");
			return false;
		}
		return true;
	}
}
