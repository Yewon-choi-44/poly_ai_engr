<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>
<%@ include file="../include/header.jsp" %>

	<div class="row justify-content-center">
		<div class="col-md-5">
			<div class="card p-4">
				<h2 class="mb-3 fw-bold text-center">비밀번호 찾기</h2>
				
				<form method="post" action="findpasswordconfirm" data-validate>
					<label class="form-label">아이디</label>
					<input type="text" name="m_id" class="form-control mb-2" placeholder="아이디"
					data-label="아이디">
					
					<label class="form-label">이메일</label>
					<input type="text" name="m_mail" class="form-control mb-3" placeholder="이메일"
					data-label="이메일">
					
					<div class="d-grid gap-2">
						<button type="submit" class="btn btn-info">비밀번호 찾기</button>
					</div>
				</form>
				<p class="text-center mt-4 mb-0">
					<a href="/loginmember" class="text-decoration-none fw-semibold">로그인</a>
					<a href="/registermember" class="text-decoration-none fw-semibold ms-3">회원가입</a>
				</p>
			</div>
		</div>
	</div>	
	<script src="js/validation.js"></script>
	
<%@ include file="../include/footer.jsp" %>