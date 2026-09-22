<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ include file="../include/header.jsp"%>

	<div class="card shadow rounded-4">
		<div class="card-body p-5">
			<h3 class="card-title text-center mb-4">도서 등록</h3>

				<label class="form-label">도서명</label>
				<input type="text" name="b_name" class="form-control mb-3" placeholder="도서명을 입력하세요">
	
				<label class="form-label">저자</label>
				<input type="text" name="b_author" class="form-control mb-3" placeholder="저자를 입력하세요">
	
				<label class="form-label">출판사</label>
				<input type="text" name="b_publisher" class="form-control mb-3" placeholder="출판사를 입력하세요">
	
				<label class="form-label">출판연도</label>
				<input type="text" name="b_publish_year" class="form-control mb-3" placeholder="출판년도 입력하세요">
	
				<label class="form-label">ISBN</label>
				<div class="input-group mb-3">
					<input type="text" name="b_isbn" class="form-control" placeholder="ISBN 입력하세요">
					<button class="btn btn-success px-4" type="button">네이버 도서 가져오기</button>
				</div>
	
				<label class="form-label">청구기호</label>
				<input type="text" name="b_call_number" class="form-control mb-3" placeholder="청구기호 입력하세요">
	
				<label class="form-label">대출가능유무</label>
				<select class="form-select mb-3" name="b_rental_able">
					<option value="1">대출가능</option>
					<option value="0">대출불가</option>
				</select>
	
				<label class="form-label">도서 이미지</label>
				<input type="file" name="b_img_file" class="form-control mb-4">
	
				<div class="d-flex justify-content-center gap-3">
					<button class="btn btn-success px-4">등록</button>
					<button class="btn btn-secondary px-4">취소</button>
				</div>
		</div>
	</div>

<%@ include file="../include/footer.jsp"%>
