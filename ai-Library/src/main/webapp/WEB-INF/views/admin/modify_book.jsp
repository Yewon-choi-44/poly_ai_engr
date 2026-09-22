<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>
<%@ include file="../include/header.jsp"%>

	<div class="card shadow rounded-4">
		<div class="card-body p-5">
			<h3 class="card-title text-center mb-4">도서 수정</h3>
			
			<form method="post" action="modifybookconfirm" enctype="multipart/form-data">
				<input type="hidden" name="b_no" value="${book.b_no}"
				
				<label class="form-label">도서명</label>
				<input type="text" name="b_name" class="form-control mb-3" value="${book.b_name}">
	
				<label class="form-label">저자</label>
				<input type="text" name="b_author" class="form-control mb-3" value="${book.b_author}">
	
				<label class="form-label">출판사</label>
				<input type="text" name="b_publisher" class="form-control mb-3" value="${book.b_publisher}">
	
				<label class="form-label">출판연도</label>
				<input type="text" name="b_publish_year" class="form-control mb-3" value="${book.b_publish_year}">
	
				<label class="form-label">ISBN</label>
				<div class="input-group mb-3">
					<input type="text" name="b_isbn" class="form-control" value="${book.b_isbn}">
					<button class="btn btn-success px-4" type="button">네이버 도서 가져오기</button>
				</div>
	
				<label class="form-label">청구기호</label>
				<input type="text" name="b_call_number" class="form-control mb-3" value="${book.b_call_number}">
	
				<label class="form-label">대출가능유무</label>
				<select class="form-select mb-3" name="b_rental_able">
					<option value="1" ${book.b_rental_able == 1 ? 'selected' : ''}>대출가능</option>
					<option value="0" ${book.b_rental_able == 0 ? 'selected' : ''}>대출불가</option>
				</select>
	
				<%-- <img src="..." class="img-fluid rounded w-25 mb-2"> --%>
				<div class="mb-4 d-flex flex-column align-items-start">
					<label class="form-label">도서 이미지</label>
					<c:choose>
						<c:when test="${not empty book.b_img}">
							<img src="${book.b_img}" class="rounded mx-auto d-block"
							style="width: 180px; height: 240px; object-fit: cover;">
						</c:when>
						<c:otherwise>
							<div class="bg-light rounded py-4 mx-auto" style="width:80px">책이미지</div>
						</c:otherwise>
					</c:choose>					
					<input type="file" name="b_img_file" class="form-control">
				</div>
	
				<div class="d-flex justify-content-center gap-3">
					<button type ="submit" class="btn btn-info px-4">수정</button>
					<a href="managementbook" class="btn btn-secondary px-4">취소</a>
				</div>
			</form>
		</div>
	</div>

<%@ include file="../include/footer.jsp"%>
