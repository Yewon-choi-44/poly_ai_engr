<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ include file="../include/header.jsp"%>
	<h2 class="text-center mb-4">내 주문</h2>
	<table class="table table-bordered table-hover align-middle text-center bg-white">
		<thead class="table-dark">
			<tr><th>번호</th><th>메뉴</th><th>수량</th><th>단가</th><th>총액</th><th>요청사항</th><th>주문일시</th><th>상태</th><th>취소</th></tr>
		</thead>
		<tbody>
				<tr>
					<td>1</td>
					<td>메뉴</td>
					<td>수량</td>
					<td>단가</td>
					<td>가격</td>
					<td>요청사항</td>
					<td>주문일시</td>
					<td><span class="badge bg-primary">주문됨 1</span>
						<span class="badge bg-warning text-dark">준비중 2</span>
						<span class="badge bg-success">완료 3</span>
						<span class="badge bg-secondary">취소 4</span>
					</td>
					<td>
							<a href="#" class="btn btn-sm btn-outline-danger"
								onclick="return confirm('주문을 취소하시겠습니까?');">취소</a>
					</td>
				</tr>
		</tbody>
	</table>
	<p class="text-muted" style="font-size: 13px;">※ 취소는 "주문됨" 상태에서만 가능합니다.</p>
<%@ include file="../include/footer.jsp"%>
