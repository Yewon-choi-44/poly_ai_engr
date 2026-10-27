<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>
<%@ include file="../include/header.jsp" %>

	<div class="row justify-content-center">
		<div class="col-md-5">
			<div class="card p-4">
				<h2 class="mb-3 fw-bold text-center">로그인</h2>
				
					<form method="post" action="loginmemberconfirm" data-validate>
					<label class="form-label">아이디</label>
					<input type="text" name="m_id" class="form-control mb-2" placeholder="아이디" data-label="아이디">
					
					<label class="form-label">비밀번호</label>
					<input type="password" name="m_pw" class="form-control mb-3" placeholder="비밀번호" data-label="비밀번호">
					
					<div class="d-grid gap-2">
						<button class="btn btn-info">로그인</button>
					</div>
					
					<p class="text-center mt-4 mb-0">
						<a href="/registermember" class="text-decoration-none fw-semibold">회원가입</a>
						<a href="/findpassword" class="text-decoration-none fw-semibold ms-3">비밀번호 찾기</a>
					</p>
				</form>
			</div>
		</div>
	</div>	

	<script src="/js/validation.js"></script>
<%@ include file="../include/footer.jsp" %>