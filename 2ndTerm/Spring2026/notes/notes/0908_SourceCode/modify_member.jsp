<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ include file="include/header.jsp" %>

	<div class="row justify-content-center">
		<div class="col-md-6">
			<div class="card p-4">
				<h4 class="mb-4 fw-bold text-center">회원 정보 수정</h4>
				
				<div class="row mb-3">
					<label class="col-sm-3 col-form-label">아이디</label>
					<div class="col-sm-9">
						<label class="col-sm-3 col-form-label">hong123</label>
					</div>
				</div>
				
				<div class="row mb-3">
					<label class="col-sm-3 col-form-label">비밀번호</label>
					<div class="col-sm-9">
						<input type="text" name="m_pw" class="form-control" placeholder="변경하시려면 새로운 비밀번호를 입력하세요">
					</div>
				</div>
				
				<div class="row mb-3">
					<label class="col-sm-3 col-form-label">비밀번호 확인</label>
					<div class="col-sm-9">
						<input type="text" name="m_pw" class="form-control" placeholder="새로운 비밀번호를 다시 입력하세요">
					</div>
				</div>
				
				<div class="row mb-3">
					<label class="col-sm-3 col-form-label">이름</label>
					<div class="col-sm-9">
						<input type="text" name="m_name" class="form-control" value="홍길동">
					</div>
				</div>
				
				<div class="row mb-3">
					<label class="col-sm-3 col-form-label">성별</label>
					<div class="col-sm-9">
						<select class="form-select" name="m_gender">
							<option value="M" selected>남성</option>
							<option value="F">여성</option>
						</select>
					</div>
				</div>
				
				<div class="row mb-3">
					<label class="col-sm-3 col-form-label">이메일</label>
					<div class="col-sm-9">
						<input type="text" name="m_email" class="form-control" value="hong@aitech.co.kr">
					</div>
				</div>
				
				<div class="row mb-3">
					<label class="col-sm-3 col-form-label">전화</label>
					<div class="col-sm-9">
						<input type="text" name="m_phone" class="form-control" value="010-1234-5678">
					</div>
				</div>
				
				<div class="text-center mt-3">
					<button class="btn btn-success px-4 me-2">수정</button>
					<button class="btn btn-light border px-4">취소</button>
				</div>
			</div>
		</div>
	</div>	

<%@ include file="include/footer.jsp" %>