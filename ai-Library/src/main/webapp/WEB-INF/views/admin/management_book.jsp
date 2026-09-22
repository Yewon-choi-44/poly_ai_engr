<%@ page contentType = "text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>
<%@ include file = "../include/header.jsp" %>

	<h2 class = "text-center mb-4">도서 목록 관리</h2>
	<div class = "d-flex justify-content-end mb-2">
		<!-- <button class="btn btn-info px-4">등록</button>-->
		<a href="registerbook" class="btn btn-info px-4">등록</a>
	</div>
	
	<table class = "table table-bordered table-hover align-middle text-center">
		<thead class="table-info">
			<tr>
				<th>번호</th>
				<th>이미지</th>
				<th>도서명</th>
				<th>저자명</th>
				<th>출판사</th>
				<th>출판년도</th>
				<th>관리</th>
			</tr>
		</thead>
		<tbody>
			<c:forEach var="book" items="${books}" varStatus="status">
				<tr>
					<td>${status.count}</td>
					
					<td>
						
						<c:choose>
							<c:when test="${not empty book.b_img}">
								<img src="${book.b_img}" class="rounded mx-auto d-block"
								style="width: 80px; height: 110px; object-fit: cover;">
							</c:when>
							<c:otherwise>
								<div class="bg-light rounded py-4 mx-auto" style="width: 80px;">책이미지</div>
							</c:otherwise>
						</c:choose>
					</td>
					
					<td>${book.b_name}</td>
					<td>${book.b_author}</td>
					<td>${book.b_publisher}</td>
					<td>${book.b_publish_year}</td>
					<td>
						<div class="d-flex justify-content-center gap-1">
							<a href="modifybook?b_no=${book.b_no}" class="btn btn-sm btn-info">수정</a>
							<a href="deletebook?b_no=${book.b_no}" class = "btn btn-sm btn-danger"
							onclick="return confirm('[${book.b_name}] 삭제하시겠습니까?");>삭제</a>
						</div>
					</td>
				</tr>	
			</c:forEach>	
		</tbody>
	</table>
	
<%@ include file="../include/footer.jsp"%>