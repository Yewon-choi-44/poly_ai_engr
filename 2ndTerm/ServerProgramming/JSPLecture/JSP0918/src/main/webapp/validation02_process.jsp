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
	
	<p> 아 이 디 : <%=id %>
	<p> 비 밀 번 호 : <%=passwd %>	
</body>
</html>