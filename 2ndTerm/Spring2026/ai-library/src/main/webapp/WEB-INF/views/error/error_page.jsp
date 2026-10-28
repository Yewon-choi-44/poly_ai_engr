<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>
<%@ include file="../include/header.jsp" %>

	<div class="text-center py-5">
		<h1 class="displat-4 fw-bold text-secondary">
			<c:out value="${statusCode}" default="오류" />
		</h1>
		<p class="fs-5 mt-3">
			<c:choose>
				<c:when test="${statusCode == 404}">페이지를 찾을 수 없습니다.</c:when>
				<c:when test="${statusCode == 400}">잘못된 요청입니다.</c:when>
				<c:otherwise>처리 중 문제가 발생했습니다. 잠시 후 다시 시도해주세요.</c:otherwise>
			</c:choose>
		</p>
		<a href="booklist" class="btn btn-info px-4 mt-3">도서목록으로</a>
	</div>


<%@ include file="../include/footer.jsp" %>