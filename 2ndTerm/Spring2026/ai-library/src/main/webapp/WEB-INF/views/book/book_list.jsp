<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>
<%@ include file="../include/header.jsp" %>

	<form method="get" action="searchbook" class="d-flex gap-2 mb-4">
		<input type="text" name="searchTxt" class="form-control" placeholder="도서명을 입력하세요" value="${searchTxt}">
		<button type="submit" class="btn btn-info flex-shrink-0">검색</button>
	</form>

	<h3 class="mb-3">도서 목록</h3>
	<div class="row">
		<c:forEach var="book" items="${books}">
			<div class="col-md-4 mb-3">
				<div class="card">
					<div class="card-body text-center">
						<c:choose>
							<c:when test="${not empty book.b_img}">
								<img src="${book.b_img}" class="w-100" style="height: 260px; object-fit: cover;">							
							</c:when>
							<c:otherwise>
								<div class="bg-light py-4 mb-2" style="font-size:40px">
									책이미지
								</div>	
							</c:otherwise>
						</c:choose>
						<h5><a href="detailbook?b_no=${book.b_no}" class="text-decoration-none text-dark"> ${book.b_name}</a></h5>
						<p class="text-muted">${book.b_author} 저자</p>
						
						<div class="d-grid">
							<c:if test="${sessionScope.loginMember.m_role != 'ADMIN'}">
								<c:choose>
									<c:when test="${book.b_rental_able == 1}">
										<a href="rentalbook?b_no=${book.b_no}" class="btn btn-warning text-white"
										onclick="return confirm('[${book.b_name}] 대출하시겠습니까?');">대출</a>
									</c:when>
									<c:otherwise>
										<button class="btn btn-secondary" disabled>대출중</button>
									</c:otherwise>
								</c:choose>
						
							</c:if>
						</div>
						
					</div>
				</div>
			</div>
		</c:forEach>
	</div>
<%@ include file="../include/footer.jsp" %>