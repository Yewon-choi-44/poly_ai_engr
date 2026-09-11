<%@ page contentType="text/html; charset=utf-8" %>
<html>
	<head><title>Implicit Objects</title></head>
</html>

<body>
	<%
		request.setCharacterEncoding("utf-8");
		String userid=request.getParameter("id");
		String password = request.getParameter("passwd");
	%>
	
	<p> 아이디 : <%=userid %>
	<p> 비밀번호 : <%=password %>
</body>