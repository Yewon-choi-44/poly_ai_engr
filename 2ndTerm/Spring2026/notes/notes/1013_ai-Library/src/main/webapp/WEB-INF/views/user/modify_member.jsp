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
						<label class="col-sm-3 col-form-label">${member.m_id}</label>
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
						<input type="text" class="form-control" placeholder="새로운 비밀번호를 다시 입력하세요">
					</div>
				</div>
				
				<div class="row mb-3">
					<label class="col-sm-3 col-form-label">이름</label>
					<div class="col-sm-9">
						<input type="text" name="m_name" class="form-control" value="${member.m_name}" 
						data-label="이름">
					</div>
				</div>
				
				<div class="row mb-3">
					<label class="col-sm-3 col-form-label">성별</label>
					<div class="col-sm-9 d-flex align-items-cneter">
						<div class="from-check form-check-inline">
							<input type="radio" name="m_gender" value="M" id="genderM"
							class="from-check-input" ${member.m_gender == 'M' ? 'checked' : ''}>
							<label for="gemderM" class="form-check-label">남</label>
						</div>
						<div class="from-check form-check-inline">
							<input type="radio" name="m_gender" value="F" id="genderF"
							class="from-check-input" ${member.m_gender == 'F' ? 'checked' : ''}>
							<label for="gemderF" class="form-check-label">여</label>
						</div>
					</div>
				</div>
				
				<div class="row mb-3">
					<label class="col-sm-3 col-form-label">이메일</label>
					<div class="col-sm-9">
						<input type="text" name="m_mail" class="form-control" value="${member.m_mail}" 
						data-label="이메일">
					</div>
				</div>
				
				<div class="row mb-3">
					<label class="col-sm-3 col-form-label">전화</label>
					<div class="col-sm-9">
						<input type="text" name="m_phone" class="form-control" value="${member.m_phone}" 
						data-label="전화">
					</div>
				</div>
				
				<div class="text-center mt-3">
					<button type="submit" class="btn btn-success px-4 me-2">수정</button>
					<a href="booklist" class="btn btn-light border px-4">취소</a>
				</div>
				</form>
			</div>
		</div>
	</div>
	
	<script src="/js/validation.js"></script>

<%@ include file="../include/footer.jsp" %>