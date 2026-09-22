<%@ page contentType = "text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ include file = "include/header.jsp"%>

	<h2 class = "text-center mb-4">도서 목록 관리</h2>
	<div class = "d-flex justify-content-end mb-2">
		<button class="btn btn-success px-4">등록</button>
	</div>
	
	<table class = "table table-bordered table-hover align-middle text-center">
		<thead class="table-success">
			<tr>
				<th>번호</th>
				<th>이미지</th>
				<th>도서명</th>
				<th>저자명</th>
				<th>출판사</th>
				<th>출판년도</th>
				<th>관리</th>
			</tr>
		</thead>
		<tbody>
			<tr>
				<td>1</td>
				<td><div class="bg-light rounded py-4 mx-auto" style="width: 80px;">책</div></td>
				<td>스프링 입문</td>
				<td>홍길동</td>
				<td>한빛미디어</td>
				<td>2024</td>
				<td>
					<div class="d-flex justify-content-center gap-1">
						<button class="btn btn-sm btn-success">수정</button>
						<button class="btn btn-sm btn-danger">삭제</button>
					</div>
				</td>
			</tr>
			<tr>
				<td>2</td>
				<td><div class="bg-light rounded py-4 mx-auto" style="width: 80px;">책</div></td>
				<td>MySQL 첫걸음</td>	
				<td>김철수</td>
				<td>위키북스</td>
				<td>2023</td>
				<td>
					<div class="d-flex justify-content-center gap-1">
						<button class="btn btn-sm btn-success">수정</button>
						<button class="btn btn-sm btn-danger">삭제</button>
					</div>
				</td>
			<tr>
				<td>3</td>
				<td><div class="bg-light rounded py-4 mx-auto" style="width: 80px;">책</div></td>
				<td>어린 왕자</td>	
				<td>생텍쥐페리</td>
				<td>민음사</td>
				<td>2015</td>
				<td>
					<div class="d-flex justify-content-center gap-1">
						<button class="btn btn-sm btn-success">수정</button>
						<button class="btn btn-sm btn-danger">삭제</button>
					</div>
				</td>
			</tr>			
		</tbody>
	</table>
	
<%@ include file="include/footer.jsp"%>