<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>
<%@ include file="../include/header.jsp" %>
		<h2 class="text-center mb-4">대출 이력</h2>	
		<table class="table table-bordered table-hover align-middle text-center">
			<thead class="table-success">
				<tr>
					<th>번호</th>
					<th>이미지</th>
					<th>도서명</th>
					<th>청구기호</th>
					<th>대출일</th>
					<th>반납일</th>
					<th>상태</th>
					<th>반납</th>
				</tr>
			</thead>
			<tbody>
				<c:forEach var="book" items="${rentalbooks}" varStatus="status">
				<tr>
					<td>${status.count}</td>
					<td>
						<c:choose>
							<c:when test="${not empty book.b_img}">
								<img src="${book.b_img}" class="rounded mx-auto d-block"
								style="width: 80px; height: 110px; object-fit: cover;">
							</c:when>
							<c:otherwise>
								<div class="bg-light rounded py-4 mx-auto" style="width: 80px">책</div>									
							</c:otherwise>
						</c:choose>
					</td>
					<td>${book.b_name}</td>
					<td>${book.b_call_number}</td>
					<td>${book.rb_start_date}</td>
					<td>${book.rb_end_date}</td>
					<td>
						<c:choose>
							<c:when test="${empty book.rb_end_date}">
								대출중
							</c:when>
							<c:otherwise>
								반납완료
							</c:otherwise>
						</c:choose>
						
					</td>
					<td>
						<div class="d-flex justify-content-center gap-1">
							<c:if test="${empty book.rb_end_date}">
								<a href="modifybook?b_no=${book.b_no}" class="btn bnt-sm btn-success"
								 onclick="return confirm('[${book.b_name}]을(를) 반납하시겠습니까?');">반납하기</a>	
							</c:if>
						</div>
					</td>
				</tr>
				</c:forEach>
			</tbody>
		</table>
<%@ include file="../include/footer.jsp" %>