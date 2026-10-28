<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>
<%@ include file="../include/header.jsp" %>

	<div class="row justify-content-center">
		<div class="col-md-6">
			<div class="card p-4">
				<h4 class="mb-4 fw-bold text-center">회원가입</h4>
				<form method="post" action="registermemberconfirm" data-validate>
					<div class="row mb-3">
						<label class="col-sm-3 col-form-label">아이디</label>
						<div class="col-sm-9 d-flex gap-2">
							<input type="text" name="m_id" id="m_id" class="form-control"
							data-label="아이디">
							<button type="button" id="checkIdBtn" 
							class="btn btn-warning text-white flex-shrink-0">중복확인</button>
						</div>
					</div>
					
					<div class="row mb-3">
						<label class="col-sm-3 col-form-label">비밀번호</label>
						<div class="col-sm-9">
							<input type="text" name="m_pw" class="form-control" 
							data-label="비밀번호">
						</div>
					</div>
					
					<div class="row mb-3">
						<label class="col-sm-3 col-form-label">이름</label>
						<div class="col-sm-9">
							<input type="text" name="m_name" class="form-control" 
							data-label="이름">
						</div>
					</div>
					
					<div class="row mb-3">
						<label class="col-sm-3 col-form-label">성별</label>
						<div class="col-sm-9 d-flex align-items-cneter">
							<div class="from-check form-check-inline">
								<input type="radio" name="m_gender" value="M" id="genderM"
								class="from-check-input" checked>
								<label for="gemderM" class="form-check-label">남</label>
							</div>
							<div class="from-check form-check-inline">
								<input type="radio" name="m_gender" value="F" id="genderF"
								class="from-check-input">
								<label for="gemderF" class="form-check-label">여</label>
							</div>
						</div>
					</div>
					
					<div class="row mb-3">
						<label class="col-sm-3 col-form-label">이메일</label>
						<div class="col-sm-9">
							<input type="text" name="m_mail" class="form-control" 
							data-label="아이디">
						</div>
					</div>
					
					<div class="row mb-3">
						<label class="col-sm-3 col-form-label">전화</label>
						<div class="col-sm-9">
							<input type="text" name="m_phone" class="form-control" 
							data-label="전화">
						</div>
					</div>
					
					<div class="text-center mt-3">
						<button type="submit" class="btn btn-success px-4 me-2">가입하기</button>
						<a href="booklist" class="btn btn-light border px-4">취소</a>
					</div>
				</form>
			</div>
		</div>
	</div>	
	
	<script src="/js/validation.js"></script>
	<script src="/js/register_member.js"></script>
	
<%@ include file="../include/footer.jsp" %>