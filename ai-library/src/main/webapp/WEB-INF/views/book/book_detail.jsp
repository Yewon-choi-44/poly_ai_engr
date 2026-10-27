<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>
<%@ include file="../include/header.jsp"%>

	<div class="row justify-content-center">
		<div class="col-lg-8">
			<div class="card shadow-lg rounded-4 border-0">
				<div class="card-header bg-info bg-opacity-25 text-center py-3 rounded-top-4">
					<h3 class="mb-0">${book.b_name}</h3>
				</div>
				<div class="card-body p-4">
					<div class="row">
						<div class="col-md-4 text-center mb-3 mb-md-0">
							<c:choose>
								<c:when test="${not empty book.b_img}">
									<img src="${book.b_img}" class="w-100 rounded"
									style="max-height: 420px; object-fit: contain;">
								</c:when>
								<c:otherwise>
									<div class="bg-light py-5 rounded" style="font-size:60px">책이미지</div>									
								</c:otherwise>
							</c:choose>
						</div>

						<div class="col-md-8 d-flex flex-column">
							<table class="table table-borderless flex-grow-1">
								<tbody>
									<tr class="border-bottom">
										<th scope="row">저자</th>
										<td>${book.b_author}</td>
									</tr>
									<tr class="border-bottom">
										<th scope="row">출판사</th>
										<td>${book.b_publisher}</td>
									</tr>
									<tr class="border-bottom">
										<th scope="row">출판연도</th>
										<td>${book.b_publisher_year}</td>
									</tr>
									<tr class="border-bottom">
										<th scope="row">ISBN</th>
										<td>${book.b_isbn}</td>
									</tr>
									<tr class="border-bottom">
										<th scope="row">청구기호</th>
										<td>${book.b_call_number}</td>
									</tr>
									<tr>
										<th scope="row">대출 가능 여부</th>
										<td>
											<c:choose>
												<c:when test="${book.b_rental_able == 1}">대출가능</c:when>
												<c:otherwise>대출불가</c:otherwise>
											</c:choose>
										</td>
									</tr>
								</tbody>
							</table>
							<div class="text-center mt-4">
								<a href="booklist" class="btn btn-outline-secondary px-4 me-2">목록으로</a>
								<c:choose>
									<c:when test="${book.b_rental_able == 1}">
										<a href="rentalbook?b_no=${book.b_no}" class="btn btn-info px-4" 
										onclick="return confirm('[${book.b_name}] 대출하시겠습니까?');">대출하기</a>
									</c:when>
									<c:otherwise>
										<button type="button" class="btn btn-secondary px-4" disabled>대출중</button>
									</c:otherwise>
								</c:choose>
								<!-- <a href="#" class="btn btn-info px-4">대출하기</a> -->
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>

<%@ include file="../include/footer.jsp"%>
