<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>
<%@ include file="../include/header.jsp"%>
	<div class="row justify-content-center">
		<div class="col-md-6">
			<div class="card shadow rounded-4">
				<div class="card-body p-5">
					<h4 class="card-title text-center fw-bold mb-4">주문하기</h4>

					<div class="d-flex gap-3 align-items-center mb-4">
						<div class="d-flex align-items-center justify-content-center bg-secondary-subtle text-secondary rounded flex-shrink-0" style="width: 90px; height: 90px; font-size: 13px;">사진 없음</div>
						<div>
							<h5 class="mb-1">메뉴</h5>
							<span class="fw-bold">가격</span>
						</div>
					</div>

						<div class="row mb-3">
							<label class="col-sm-3 col-form-label">수량</label>
							<div class="col-sm-9"><input type="number" name="o_qty" class="form-control" value="1" min="1" max="9" required></div>
						</div>
						<div class="row mb-4">
							<label class="col-sm-3 col-form-label">요청사항</label>
							<div class="col-sm-9"><input type="text" name="o_req" class="form-control" placeholder="선택 입력 (예: 샷 추가)"></div>
						</div>

						<p class="text-center text-muted mb-3" style="font-size: 14px;">결제는 수령 시 카운터에서 진행됩니다.</p>

						<div class="d-flex justify-content-center gap-3">
							<button class="btn btn-warning fw-bold px-4"
								onclick="return confirm('[메뉴] 주문하시겠습니까?');">주문하기</button>
							<a href="#" class="btn btn-light border px-4">취소</a>
						</div>
				</div>
			</div>
		</div>
	</div>
<%@ include file="../include/footer.jsp"%>
