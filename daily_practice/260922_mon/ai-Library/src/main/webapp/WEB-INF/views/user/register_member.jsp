<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ include file="../include/header.jsp" %>

	<div class = "row justify-content-center">
		<div class="col-md-5">
			<div class="card p-4">
				<h4 class="mb-4">회원가입</h4>
				
				<div class="row mb-3">
					<label class="col-sm-3 col-from-label">아이디</label>
					<div class="col-sm-9 d-flex gap-2">
						<input type="text" name="m_id" class="form-control">
						<button class="btn btn-warning btn-sm text-white flex-shrink-0">중복확인</button>
					</div> 
				</div>
				
				<div class="row mb-3">
					<label class="col-sm-3 col-from-label">비밀번호</label>
					<div class="col-sm-9">
						<input type="password" name="m_pw" class="form-control">
					</div>
				</div>

				<div class="row mb-3">
					<label class="col-sm-3 col-from-label">이름</label>
					<div class="col-sm-9">
						<input type="name" name="m_name" class="form-control">
					</div>
				</div>
				
				<div class="row mb-3">
					<label class="col-sm-3 col-from-label">성별</label>
					<div class="col-sm-9">
						<input type="gender" name="m_gender" class="form-control">
					</div>
				</div>
				
				<div class="row mb-3">
					<label class="col-sm-3 col-from-label">이메일 주소</label>
					<div class="col-sm-9">
						<input type="mail" name="m_email" class="form-control">
					</div>
				</div>
				
				<div class="row mb-3">
					<label class="col-sm-3 col-from-label">전화번호</label>
					<div class="col-sm-9">
						<input type="phone" name="m_phone" class="form-control">
					</div>
				</div>
				
				<div class="text-center mt-3">
					<button class="btn btn-info px-4 me-2">가입하기</button>
					<button class="btn btn-light border px-4">취소</button>
				</div>
			</div>
		</div>
	</div>		
		
<%@ include file="../include/footer.jsp" %>