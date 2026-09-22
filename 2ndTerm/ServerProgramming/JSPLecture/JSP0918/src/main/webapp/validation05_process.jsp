<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Validation</title>
</head>
<body>
	<h3> 입력에 성공했습니다. </h3>
	<%
		request.setCharacterEncoding("utf-8");
		String id = request.getParameter("id");
		String passwd = request.getParameter("passwd");
	%>
	
	<p> 아 이 디 : <%=request.getParameter("id") %>
	<p> 비 밀 번 호 : <%=request.getParameter("passwd") %>	
	<p> 이 름 : <%=request.getParameter("name") %>	
	<p> 연 락 처 : <%=request.getParameter("phone1") %> - <%=request.getParameter("phone2") %> - <%= request.getParameter("phone3") %>
	<p> 이 메 일 : <%=request.getParameter("email") %>
</body>
</html>