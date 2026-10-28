<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>
<%@ include file="../include/header.jsp" %>

	<div class="row justify-content-center">
		<div class="col-md-6">
			<div class="card p-4">
				<h4 class="mb-4 fw-bold text-center">회원 정보 수정</h4>
				<form method="post" action="modifymemberconfirm" data-validate>
					<input type="hidden" name="m_no" value="${member.m_no}">
				<div class="row mb-3">
					<label class="col-sm-3 col-form-label">아이디</label>
					<div class="col-sm-9">
						<label class="col-sm-3 col-form-label" value="${member.m_id}"></label>
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
						<input type="text" name="m_pw_check" class="form-control" placeholder="새로운 비밀번호를 다시 입력하세요">
					</div>
				</div>
				
				<div class="row mb-3">
					<label class="col-sm-3 col-form-label">이름</label>
					<div class="col-sm-9">
						<input type="text" name="m_name" class="form-control"data-label="이름" value="${member.m_name}" >
					</div>
				</div>
				
				<div class="row mb-3">
					<label class="col-sm-3 col-form-label">성별</label>
					<div class="col-sm-9 d-flex align-items-center">
						<div class="form-check form-check-inline">
							<input type="radio" name="m_gender" value="M" id="genderM"
							class="form-check-input" ${member.m_gender == 'M' ? 'checked' : ''}>
							<label for = "genderM" class="form-check-label">남</label>							 
						</div>
						<div class="form-check form-check-inline">
							<input type="radio" name="m_gender" value="F" id="genderF"
							class="form-check-input" ${member.m_gender == 'F' ? 'checked' : ''}>
							<label for = "genderF" class="form-check-label">여</label>							 
						</div>
					</div>
				</div>
				
				<div class="row mb-3">
					<label class="col-sm-3 col-form-label">이메일</label>
					<div class="col-sm-9">
						<input type="text" name="m_mail" class="form-control" data-label="이메일" value="${member.m_mail}" >
					</div>
				</div>
				
				<div class="row mb-3">
					<label class="col-sm-3 col-form-label">전화</label>
					<div class="col-sm-9">
						<input type="text" name="m_phone" class="form-control" data-label="전번" value="${member.m_phone}">
					</div>
				</div>
				
				<div class="text-center mt-3">
					<button type="submit" class="btn btn-info px-4 me-2">수정</button>
					<a class="btn btn-light border px-4">취소</a>
				</div>
				</form>
				<script src="/js/validation.js"></script>
			</div>
		</div>
	</div>	

<%@ include file="../include/footer.jsp" %>