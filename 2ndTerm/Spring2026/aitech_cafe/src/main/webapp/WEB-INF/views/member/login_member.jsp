<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ include file="../include/header.jsp"%>
	<div class="row justify-content-center">
		<div class="col-md-5">
			<div class="card p-4">
				<h4 class="mb-3">로그인</h4>
				<form method="post" action="loginmemberconfirm">
					<label class="form-label">아이디</label>
					<input type="text" name="m_id" class="form-control mb-2" placeholder="아이디" required>

					<label class="form-label">비밀번호</label>
					<input type="password" name="m_pw" class="form-control mb-3" placeholder="비밀번호" required>

					<div class="d-grid">
						<button class="btn btn-dark">로그인</button>
					</div>
				</form>
			</div>
		</div>
	</div>
<%@ include file="../include/footer.jsp"%>
