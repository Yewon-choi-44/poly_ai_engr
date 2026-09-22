<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>
<%@ include file="../include/header.jsp" %>

<div class="d-flex gap-2 mb-4">
	<input type="text" class="form-control" placeholder="도서명을 입력하세요">
	<button class="btn btn-info flex-shrink-0">검색</button>
</div>

<h3 class="mb-3">도서 목록</h3>
<div class="row">
	<c:forEach var="book" items="${books}">
		<div class="col-md-4 mb-3">
			<div class="card">
				<div class="card-body text-center">
					
					<c:choose>
						<c:when test="${not empty book.b_img}">
							<img src = "${book.b_img}" class="w-100 rounded mb-2" style="height: 260px; object-fit: cover;">
						</c:when>
						<c:otherwise>
							<div class="bg-light py-4 mb-2" style="font-size: 40px"></div>
						</c:otherwise>
					</c:choose>
					
					<h5><a href="bookdetail?b_no=${book.b_no}" class="text-decoration-none text-dark">${book.b_name}</a></h5>
					<p class="text-muted">${book.b_author} 저자</p>
					<div class="d-grid">
						<button class="btn btn-warning text-white">대출</button>
					</div>
				</div>
			</div>
		</div>
	</c:forEach>
</div>
		
<%@ include file="../include/footer.jsp" %>