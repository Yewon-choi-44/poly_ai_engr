<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>
<%@ include file="../include/header.jsp"%>

	<form method = "get" action="searchmenu" class="d-flex gap-2 mb-4">
		<input type="text" name="searchTxt" class="form-control" placeholder="메뉴명을 입력하세요" value="${searchTxt}">
		<button type="submit" class="btn btn-dark flex-shrink-0">검색</button>
	</form>

	<h3 class="mb-3">메뉴</h3>
	<div class="row">
		<c:forEach var="menu" items="${menus}">
			<div class="col-md-3 mb-4">
				<div class="card h-100">		
					<div class="card-body text-center">
						<c:choose>
							<c:when test="${not empty menu.mn_img}">
								<img src="${menu.mn_img}" class="card-img-top" style="height: 140px; object-fit: cover;" alt="${menu.mn_img}"> 
							</c:when>
							<c:otherwise>
								<div class="bg-light py-4 mb-2" style="font-size: 40px">
									이미지 준비중	
								</div>
							</c:otherwise>
						</c:choose>
						<div class="d-grid">
							<c:if test="${sessionScope.m_role == USER"}>
								<c:choose>
									<c:when test="${menu.mn_sale == 0}">
										<a href="#" class="btn btn-warning fw-bold"
											onclick="return confirm('[${menu.mn_name}] 주문하시겠습니까?');"> 주문하기</a>
									</c:when>
									<c:otherwise>
										<div class="d-grid"><button class="btn btn-outline-secondary" disabled>품절</button></div>
									</c:otherwise>
								</c:choose>
							</c:if>
						</div>

				
					</div>
				</div>
			</div>
		</c:forEach>
	</div>
<%@ include file="../include/footer.jsp"%>
