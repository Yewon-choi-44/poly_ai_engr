<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>
<!DOCTYPE html>
<html>

<head>
	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet"
		integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
	<title>AITECH 도서관</title>
</head>


<body class = "bg-body-secondary">
	<nav class="navbar navbar-expand bg-info" data-bs-theme="dark">
		<div class="container">
			<a class="navbar-brand fw-bold" href="/">AITECH 도서관</a>
			<div class="navbar-nav">
				<c:if test="${not empty sessionScope.loginMember}">
					<span class="nav-link fw-bold">${sessionScope.loginMember.m_name}님</span>
				</c:if>
				
				<a class="nav-link" href="booklist">도서목록</a>
				
				<c:choose>
					<c:when test="${empty sessionScope.loginMember}">
						<a class="nav-link" href="/loginmember">로그인</a>
						<a class="nav-link" href="/registermember">회원가입</a>
					</c:when>
					<c:otherwise>
						<c:if test="${sessionScope.loginMember.m_role != 'ADMIN'}">
							<a class="nav-link" href="rentalbooklist">대출목록</a>
						</c:if>
						<c:if test="${sessionScope.loginMember.m_role == 'ADMIN'}">
							<a class="nav-link" href="managementbook">관리자메뉴</a>
						</c:if>

						<a class="nav-link" href="modifymember?m_no=${sessionScope.loginMember.m_no}">정보수정</a>		
						<a class="nav-link" href="logoutmember">로그아웃</a>
					</c:otherwise>	
				</c:choose>
			</div>
		</div>
	</nav>
	<br>