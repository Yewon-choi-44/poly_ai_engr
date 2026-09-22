<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ include file="../include/header.jsp" %>

	<div class = "row justify-content-center">
		<div class="col-md-5">
			<div class="card p-5">
				<h4 class="mb-4">회원 정보 수정</h4>
				
				<div class="row mb-3">
					<label class="col-sm-3 col-form-label">아이디</label>
					<div class="col-sm-9 d-flex gap-2">
						<input type="text" name="m_id" class="form-control">
					</div> 
				</div>
				
				<div class="row mb-3">
					<label class="col-sm-3 col-form-label">비밀번호</label>
					<div class="col-sm-9">
						<input type="password" name="m_pw" class="form-control" placeholder="변경하시려면 새로운 비밀번호를 입력하세요.">
					</div>
				</div>

				<div class="row mb-3">
					<label class="col-sm-3 col-form-label">비밀번호 확인</label>
					<div class="col-sm-9">
						<input type="password" name="m_pw" class="form-control" placeholder="새로운 비밀번호를 다시 입력하세요.">
					</div>
				</div>

				<div class="row mb-3">
					<label class="col-sm-3 col-form-label">성명</label>
					<div class="col-sm-9">
						<input type="name" name="m_name" class="form-control">
					</div>
				</div>
				
				<div class="row mb-3">
					<label class="col-sm-3 col-form-label">성별</label>
					<div class="col-sm-9">
						<select class = "form-select">
							<option value = "남">남자</option>
							<option value = "여">여자</option>
						</select>
					</div>
				</div>
				
				<div class="row mb-3">
					<label class="col-sm-3 col-form-label">이메일 주소</label>
					<div class="col-sm-9">
						<input type="mail" name="m_email" class="form-control">
					</div>
				</div>
				
				<div class="row mb-3">
					<label class="col-sm-3 col-form-label">전화번호</label>
					<div class="col-sm-9">
						<input type="phone" name="m_phone" class="form-control">
					</div>
				</div>
				
				<div class="text-center mt-3 gap-3">
					<button class="btn btn-info px-4 me-2">수정</button>
					<button class="btn btn-light border px-4">취소</button>
				</div>
			</div>
		</div>
	</div>		
		
<%@ include file="../include/footer.jsp" %>