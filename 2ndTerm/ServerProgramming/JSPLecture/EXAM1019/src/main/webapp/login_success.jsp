<%@ page contentType="text/html; charset=utf-8"%>
<html>
<head>
<title>Security</title>
</head>


<body>
	<%
		String id = request.getParameter("id");
	%>
	<p><%=id %>님 로그인을 성공하였습니다.

	<p> <a href="loginForm.jsp" class="btn btn-secondary" type="button">로그아웃</a>
</body>
</html>