<%@ page contentType="text/html; charset=utf-8"%>
<html>
<head>
<title>Security</title>
</head>
<body>
	<form name="loginForm" action="loginForm_process.jsp" method="post">
		<p>사용자명: <input type="text" name="id">
		<p>비밀번호 : <input type="password" name="passwd">
		<p><input type="submit" value="전송">
	</form>
</body>
</html>