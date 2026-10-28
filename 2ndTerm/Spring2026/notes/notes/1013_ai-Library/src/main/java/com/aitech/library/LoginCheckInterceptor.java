package com.aitech.library;

import org.springframework.web.servlet.HandlerInterceptor;

import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;

public class LoginCheckInterceptor implements HandlerInterceptor {
	public boolean preHandle(HttpServletRequest request, HttpServletResponse response,
			Object handler) throws Exception {
		HttpSession session = request.getSession();
		if(session.getAttribute("loginMember") ==  null) {
			response.sendRedirect("/loginmember");
			return false;
		}
		return true;
	}
}
