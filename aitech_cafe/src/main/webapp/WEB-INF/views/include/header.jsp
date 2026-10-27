<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="jakarta.tags.core"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>캠퍼스 카페</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
	<nav class="navbar navbar-expand bg-dark" data-bs-theme="dark">
		<div class="container">
			<a class="navbar-brand fw-bold" href="#">☕ 캠퍼스 카페</a>
			<div class="navbar-nav">
				<c:if test="${not empty sessionScope.loginMember}">
					<span class="nav-link fw-bold">${sessionScope.loginMember.m_name}님</span>
				</c:if>
				
				<a class="nav-link" href="#">메뉴</a>
				<c:choose>
					<c:when test="${empty sessionScope.loginMember}">
						<a class="nav-link" href="loginmember">로그인</a>
					</c:when>
				
					<c:otherwise>
						<a class="nav-link" href="myorders">내주문</a>
						<a class="nav-link" href="logoutmember">로그아웃</a>
				</c:otherwise>
				</c:choose>
			</div>
		</div>
	</nav>
	<div class="container mt-4">
