package com.filter;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.Filter;
import javax.servlet.FilterChain;
import javax.servlet.FilterConfig;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;

public class LoginYewonChoi implements Filter {
	@Override 
	public void init(FilterConfig filterConfig) throws ServletException {
		System.out.println("초기화");
	}
	
	@Override
	public void doFilter(ServletRequest request, ServletResponse response,
			FilterChain filterChain) throws IOException, ServletException {
		
		String name = request.getParameter("name");
		
		if (name==null || name.equals("")) {
			response.setCharacterEncoding("UTF-8");
			response.setContentType("text/html; charset=UTF-8");
			PrintWriter writer = response.getWriter();
			String message = "입력된 name 값은 null입니다.";
			writer.println(message);
			return;
		}
		filterChain.doFilter(request, response);
	}
	
	@Override
	public void destroy() {
		System.out.println("필터 해제");
	}
}
