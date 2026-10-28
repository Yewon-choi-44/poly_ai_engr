<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>
<!DOCTYPE html>
<html>

<head>
	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet"
		integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
	<title>AITECH 도서관</title>
</head>

<body class="bg-light">
	<nav class="navbar navbar-expand bg-success" data-bs-theme="dark">
		<div class="container">
			<a class="navbar-brand fw-bold" href="/">AITECH 도서관</a>
			<div class="navbar-nav">
				<c:if test="${not empty sessionScope.loginMember}">
					<span class="nav-link fw-bold">${sessionScope.loginMember.m_name}님</span>
				</c:if>
				<a href="booklist" class="nav-link" href="/booklist">도서목록</a>
				<c:choose>
					<c:when test="${empty sessionScope.loginMember}">
						<a href="loginmember" class="nav-link">로그인</a>
						<a href="registermember" class="nav-link">회원가입</a>
					</c:when>
					<c:otherwise>
						<c:if test="${sessionScope.loginMember.m_role != 'ADMIN'}">
							<a href="rentalbooklist" class="nav-link">대출목록</a>
						</c:if>
						<c:if test="${sessionScope.loginMember.m_role == 'ADMIN'}">
							<a href="managementbook" class="nav-link">도서관리</a>
						</c:if>
						<a href="modifymember?m_no=${sessionScope.loginMember.m_no}" class="nav-link">정보수정</a>
						<a href="logoutmember" class="nav-link">로그아웃</a>
					</c:otherwise>
				</c:choose>
			</div>
		</div>
	</nav>
	<div class="container mt-4">