<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ include file="include/header.jsp" %>

	<div class="d-flex gap-2 mb-4">
		<input type="text" class="form-control" placeholder="도서명을 입력하세요">
		<button class="btn btn-success flex-shrink-0">검색</button>
	</div>
	<h3 class="mb-3">도서 목록</h3>
	<div class="row">
		<div class="col-md-4 mb-3">
			<div class="card">
				<div class="card-body text-center">
					<div class="bg-light py-4 mb-2" style="font-size:40px">책이미지</div>
					<h5>스프링 부트 입문</h5>
					<p class="text-muted">홍길동 저자</p>
					<div class="d-grid">
						<button class="btn btn-warning text-white">대출</button>
					</div>
				</div>
			</div>
		</div>
		<div class="col-md-4 mb-3">
			<div class="card">
				<div class="card-body text-center">
					<div class="bg-light py-4 mb-2" style="font-size:40px">책이미지</div>
					<h5>스프링 부트 입문</h5>
					<p class="text-muted">홍길동 저자</p>
					<div class="d-grid">
						<button class="btn btn-warning text-white">대출</button>
					</div>
				</div>
			</div>
		</div>
		<div class="col-md-4 mb-3">
			<div class="card">
				<div class="card-body text-center">
					<div class="bg-light py-4 mb-2" style="font-size:40px">책이미지</div>
					<h5>스프링 부트 입문</h5>
					<p class="text-muted">홍길동 저자</p>
					<div class="d-grid">
						<button class="btn btn-warning text-white">대출</button>
					</div>
				</div>
			</div>
		</div>
	</div>
<%@ include file="include/footer.jsp" %>