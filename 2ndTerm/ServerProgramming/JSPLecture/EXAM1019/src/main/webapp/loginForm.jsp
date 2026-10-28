<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>loginForm</title>
</head>

<script>
	
	function checkLogin( ){
		var form = document.loginForm;
		if (form.passwd.value.length > 12 || form.passwd.value.length < 8) {		
			alert("비밀번호는 영문자, 숫자 혼합 8자~12자까지 입력해야 합니다!");
			form.passwd.select();
			return;
		}	
	
		form.submit();
 } 
</script>

<body>
	<form method="post" action="loginForm_process.jsp" name="Member">
		<p> 아이디 : <input type "text" name="id">
		<p> 비밀번호 : <input type = "text" name="passwd">
		<p> <input type="submit" value="전송" onclick="checkLogin()">	
	</form>
</body>
</html>