<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">

	<title>Action Tag</title>
</head>
<body>
	<h3>이 파일은 firstInclude.jsp입니다.</h3>
	<jsp:include page="secondInclude.jsp" flush="false" />
	<p>Jakarta Server Page</p>
</body>
</html>