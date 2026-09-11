# 📚 BookMarket 쇼핑몰 메인 프로젝트 누적 실습 노트

> **교재**: 《쉽게 배우는 JSP 웹 프로그래밍(2판)》(송미영 저, 한빛아카데미)  
> **핵심 프로젝트**: BookMarket (도서 쇼핑몰 웹 애플리케이션)  
> 각 장의 학습 내용을 누적하여 기능을 지속적으로 확장·진화시키는 메인 전용 정리 문서입니다.

---

## 1. 프로젝트 개요 및 누적 진행 현황

- **프로젝트명**: BookMarket
- **실습 환경**: Eclipse IDE + Apache Tomcat 9.0 + JDK 21
- **배포 URL 매핑**: http://localhost:8080/BookMarket/
- **저장소 패턴**: 싱글톤 패턴 기반의 데이터 접근 객체(BookRepository) 및 JavaBeans DTO(Book)

### 📊 장별 기능 누적 개발 현황

| 장 | 구현 기능 | 주요 파일 | 완료 여부 |
|---|---|---|---|
| 1장 | 동적 웹 프로젝트 생성 및 기본 구조 설계 | BookMarket/ | ✅ 완료 |
| 2장 | 부트스트랩(Bootstrap) 적용 시작 페이지 작성 | Welcome0819.jsp | ✅ 완료 |
| 3장 | 인코딩 설정 및 페이지 모듈화 (헤더/푸터 분리) | welcome.jsp, menu.jsp, ooter.jsp | ✅ 완료 |
| 4장 | JavaBeans 기반 도서 목록 조회 페이지 | Book.java, BookRepository.java, ooks.jsp | ✅ 완료 |
| 5장 | request 내장 객체 활용 도서 상세 정보 조회 | ook.jsp | ✅ 완료 |
| 6장 | 폼 태그 기반 도서 신규 등록 페이지 | ddBook.jsp | ✅ 완료 |
| 7장 | cos.jar(MultipartRequest) 이용 도서 이미지 업로드 | ddBook.jsp, processAddBook.jsp | ✅ 완료 |

---

## 2. 프로젝트 디렉토리 구조

`
BookMarket/
├── .classpath
├── .project
├── .gitignore                          ← 빌드 결과물, .settings, Thumbs.db 제외
├── src/main/
│   ├── java/
│   │   ├── dao/
│   │   │   └── BookRepository.java     ← 도서 목록 싱글톤 DAO (하드코딩 3권 + 동적 추가)
│   │   └── dto/
│   │       └── Book.java               ← 도서 DTO (JavaBean, Serializable)
│   └── webapp/
│       ├── Welcome0819.jsp             ← [2장] Bootstrap 적용 초기 시작 페이지
│       ├── welcome.jsp                 ← [3장] include 모듈화 메인 페이지
│       ├── menu.jsp                    ← [3장] 공통 헤더 네비게이션 모듈
│       ├── footer.jsp                  ← [3장] 공통 바닥글 모듈
│       ├── books.jsp                   ← [4장] 도서 전체 목록 페이지
│       ├── book.jsp                    ← [5장] 도서 상세 정보 페이지 (request 파라미터)
│       ├── addBook.jsp                 ← [6/7장] 도서 등록 폼 (multipart/form-data)
│       ├── processAddBook.jsp          ← [7장] 도서 등록 처리 (MultipartRequest 파일 업로드)
│       └── resources/
│           ├── css/
│           │   └── bootstrap.min.css   ← 부트스트랩 CSS
│           └── images/
│               ├── ISBN1234.jpg        ← 도서 1 이미지
│               ├── ISBN1235.jpg        ← 도서 2 이미지
│               └── ISBN1236.jpg        ← 도서 3 이미지
`

---

## 3. Java 소스 코드 (전체 원본 발췌)

### 📄 src/main/java/dto/Book.java — 도서 DTO (JavaBean)

`java
package dto;

import java.io.Serializable;

public class Book implements Serializable {
	
	private static final long serialVersionUID = -3380744562125414844L;
	
	private String bookId;      // 도서 ID (예: ISBN1234)
	private String name;        // 도서명
	private int unitPrice;      // 가격
	private String author;      // 저자
	private String description; // 설명
	private String publisher;   // 출판사
	private String category;    // 분류
	private long unitInStock;   // 재고 수량
	private String releaseDate; // 출판일(월/년)
	private String condition;   // 상태 (신규/중고/E-Book)
	private String filename;    // 이미지 파일명

	public Book() {
		super();
	}
	
	public Book(String bookId, String name, Integer unitPrice) {
		this.bookId = bookId;
		this.name = name;
		this.unitPrice = unitPrice;
	}

	public String getBookId() {
		return bookId;
	}
	
	public void setBookId(String bookId) {
		this.bookId = bookId;
	}

	public String getName() {
		return name;
	}
	
	public void setName(String name) {
		this.name = name;
	}

	public int getUnitPrice() {
		return unitPrice;
	}
	
	public void setUnitPrice(int unitPrice) {
		this.unitPrice = unitPrice;
	}

	public String getAuthor() {
		return author;
	}
	
	public void setAuthor(String author) {
		this.author = author;
	}

	public String getDescription() {
		return description;
	}
	
	public void setDescription(String description) {
		this.description = description;
	}

	public String getPublisher() {
		return publisher;
	}
	
	public void setPublisher(String publisher) {
		this.publisher = publisher;
	}

	public String getCategory() {
		return category;
	}

	public void setCategory(String category) {
		this.category = category;
	}

	public long getUnitInStock() {
		return unitInStock;
	}

	public void setUnitInStock(long unitInStock) {
		this.unitInStock = unitInStock;
	}

	public String getReleaseDate() {
		return releaseDate;
	}

	public void setReleaseDate(String releaseDate) {
		this.releaseDate = releaseDate;
	}

	public String getCondition() {
		return condition;
	}

	public void setCondition(String condition) {
		this.condition = condition;
	}

	public static long getSerialversionuid() {
		return serialVersionUID;
	}

	public String getFilename() {
		return filename;
	}
	
	public void setFilename(String filename) {
		this.filename = filename;
	}
}
`

- **동작 원리**:
  - Serializable 인터페이스를 구현하여 객체 직렬화를 지원하는 표준 JavaBean 클래스입니다.
  - 도서의 모든 속성을 private 필드로 캡슐화하고 기본 생성자와 getter/setter 메서드를 제공합니다.

---

### 📄 src/main/java/dao/BookRepository.java — 도서 데이터 관리 DAO (싱글톤)

`java
package dao;

import java.util.ArrayList;
import dto.Book;

public class BookRepository {
	
	private ArrayList<Book> listOfBooks = new ArrayList<Book>();
	private static BookRepository instance = new BookRepository();
	
	public static BookRepository getInstance() {
		return instance;
	}
	
	public void addBook(Book book) {
		listOfBooks.add(book);
	}
	
	public BookRepository() {
		Book book1 = new Book("ISBN1234", "C# 프로그래밍", 27000);
		book1.setAuthor("우재남");
		book1.setDescription("C#을 처음 시작하는 독자를 위한 기초서입니다.");
		book1.setPublisher("한빛아카데미");
		book1.setCategory("IT모바일");
		book1.setUnitInStock(1000);
		book1.setReleaseDate("2022/10/06");
		book1.setFilename("ISBN1234.jpg");
		
		Book book2 = new Book("ISBN1235", "자바마스터", 30000);
		book2.setAuthor("송미영");
		book2.setDescription("자바 입문자와 실무자를 위한 필독 기초 및 실습서입니다.");
		book2.setPublisher("한빛아카데미");
		book2.setCategory("IT모바일");
		book2.setUnitInStock(1000);
		book2.setReleaseDate("2023/01/01");
		book2.setFilename("ISBN1235.jpg");
		
		Book book3 = new Book("ISBN1236", "파이썬 프로그래밍", 30000);
		book3.setAuthor("최성철");
		book3.setDescription("파이썬의 기초부터 데이터 처리 실습까지 쉽게 알려주는 책입니다.");
		book3.setPublisher("한빛아카데미");
		book3.setCategory("IT모바일");
		book3.setUnitInStock(1000);
		book3.setReleaseDate("2023/01/01");
		book3.setFilename("ISBN1236.jpg");
		
		listOfBooks.add(book1);
		listOfBooks.add(book2);
		listOfBooks.add(book3);
	}
	
	public ArrayList<Book> getAllBooks() {
		return listOfBooks;
	}
	
	public Book getBookById(String bookId) {
		Book bookById = null;
		
		for (int i = 0; i < listOfBooks.size(); i++) {
			Book book = listOfBooks.get(i);
			if (book != null && book.getBookId() != null && book.getBookId().equals(bookId)) {
				bookById = book;
				break;
			}
		}
		return bookById;
	}
}
`

- **동작 원리**:
  - 싱글톤 패턴(getInstance())으로 애플리케이션 내 단 하나의 객체 메모리만 공유 관리합니다.
  - 생성자에서 기본 도서 3권데이터를 초기화하며 ddBook(), getAllBooks(), getBookById() 메서드로 CRUD 기능을 수행합니다.

---

## 4. JSP 실습 코드 (전체 원본 발췌)

### 📄 src/main/webapp/menu.jsp — 공통 헤더 네비게이션 모듈

`jsp
<header class = "pb-3 mb mb-4 border-bottom">
	<a href = "./welcome.jsp" class="d-flex align-items-center text-dark text-decoration-none">
		<svg width="32" height="32" fill="currentColor" class="bi bi-house-fill" viewBox="0 0 16 16">
			<path d = "M8.707 1.5a1 1 0 0 0-1.414 0L.646 8.146a.5.5 0 0 0 .708.708L82.207l6.646 6.647a.5.5 0 0 0 .708-.708L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293L8.707 1.5Z" />
			<path d = "m8 3.293 6 6V13.5a1.5 1.5 0 0 1-1.5 1.5h-9A1.5 1.5 0 0 1 2 13.5V9.293l6-6Z" />
		</svg>
		<span class = "fs-4">Home</span>
	</a>
</header>
`

---

### 📄 src/main/webapp/footer.jsp — 공통 바닥글 모듈

`jsp
<footer class = "pt-3 mt-4 text-body-secondary border-top">
	&copy; BookMarket
</footer> 
`

---

### 📄 src/main/webapp/Welcome0819.jsp — 2장 Bootstrap 초기 시작 페이지

`jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
pageEncoding="UTF-8"%>
<%@ page import ="java.util.Date" %>

<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>Welcome</title>
	<link href = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
	<div class = "container py-4">
		<header class = "pb-3 mb-4 border-bottom">
			<a href = "./Welcome.jsp" class = "d-flex align-items-center text-dark text-decoration-none">
				<svg width="32" height="32" fill="currentColor" class="bi bi-house-fill" viewBox="0 0 16 16">
					<path d = "M8.707 1.5a1 1 0 0 0-1.414 0L.646 8.146a.5.5 0 0 0 .708.708L82.207l6 .646 6.647a.5.5 0 0 0 .708-.708L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293L8.707 1.5Z"/>
				</svg>
					<span class = "fs-4">Home</span>
			</a>
		</header>
	

	<%! 
	String greeting = "Welcome to Book Shopping Mall";
	String tagline = "Welcome to Web Market!"; 
	%>
	
	<div class = "p-5 mb-4 bg-body-tertiary rounded-3">
		<div class="container-fluid py-5">
			<h1 class="display-5 fw-bold">
			<%= greeting %></h1>
			<p class="col-md-8 fs-4">BookMarket</p>
			</div>
	</div>
	<div class = "row align-items-md-stretch text-center">
		<div class = "col-md-12">
			<div class = "h-100 p-5">
				<h3><%= tagline %></h3>
				<%
					Date day = new java.util.Date();
					String am_pm;
					int hour = day.getHours();
					int minute=day.getMinutes();
					int second=day.getSeconds();
					
					if (hour / 12 == 0){
						am_pm = "AM";
					} else {
						am_pm = "PM";
						hour = hour - 12;
					}
					String CT = hour + ":" + minute + ":" + second + " " + am_pm;
					out.println("현재 접속 시각: " + CT + "\n");
					%>
			</div>
		</div>
	</div>
	<footer class = "pt-3 mt-4 text-body-secondary border-top">
		&copy; BookMarket
	</footer>


	</div>
</body>
</html>
`

---

### 📄 src/main/webapp/welcome.jsp — 3장 include 디렉티브 모듈화 메인 페이지

`jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
pageEncoding="UTF-8"%>
<%@ page import ="java.util.Date" %>

<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>Welcome</title>
	<link href = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
	<div class = "container py-4">
		<%@ include file = "menu.jsp" %>
		<%! 
		String greeting = "도서 쇼핑몰에 오신 것을 환영합니다";
		String tagline = "Welcome to Web Market!"; 
		%>
	
	<div class = "p-5 mb-4 bg-body-tertiary rounded-3">
		<div class="container-fluid py-5">
			<h1 class="display-5 fw-bold">
			<%= greeting %></h1>
			<p class="col-md-8 fs-4">BookMarket</p>
		</div>
	</div>
	<div class = "row align-items-md-stretch text-center">
		<div class = "col-md-12">
			<div class = "h-100 p-5">
				<h3><%= tagline %></h3>
				<%
					response.setIntHeader("Refresh", 5);
					Date day = new java.util.Date();
					String am_pm;
					int hour = day.getHours();
					int minute=day.getMinutes();
					int second=day.getSeconds();
					
					if (hour / 12 == 0){
						am_pm = "AM";
					} else {
						am_pm = "PM";
						hour = hour - 12;
					}
					String CT = hour + ":" + minute + ":" + second + " " + am_pm;
					out.println("현재 접속 시각: " + CT + "\n");
				%><hr>
				<p><a href="./books.jsp" class ="btn btn-secondary" role="button">도서 목록 &raquo;</a>
				<p><a href="./addBook.jsp" class ="btn btn-secondary" role="button">[관리자]도서 등록 &raquo;</a>
			</div>
		</div>
		<%@include file = "footer.jsp" %>
	</div>
	</div>
</body>
</html>
`

---

### 📄 src/main/webapp/books.jsp — 4장 도서 전체 목록 표시 페이지

`jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import = "java.util.ArrayList" %>
<%@ page import = "dto.Book" %>
<%@ page import = "dao.BookRepository" %>

<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>도서 목록</title>
	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
	<div class = "container py-4">
		<%@ include file = "menu.jsp" %>
		
		<div class = "p-5 mb-4 bg-body-tertiary rounded-3">
			<div class = "container-fluid py-5">
				<h1 class = "display-5 fw-bold">도서 목록</h1>
				<p class = "col-md-8 fs-4">BookList</p>
			</div>
		</div>
		
		<%
			BookRepository dao = BookRepository.getInstance();
			ArrayList<Book> listOfBooks = dao.getAllBooks();
		%>
		
		<div class = "row align-items-md-stretch  text-center">
			<%
				for (int i=0 ; i < listOfBooks.size() ; i++) {
					Book book=listOfBooks.get(i);
			%>
			<div class = "col-md-4">
				<div class = "h-100 p-2">
					<img src = "./resources/images/<%= book.getFilename() %>" style = "width: 250px; height: 350px;" />
					<h5><b><%=book.getName() %></b></h5>
					<p> <%=book.getAuthor() %>
					<br><%=book.getPublisher() %> | <%= book.getReleaseDate() %>
					<p> <%=book.getDescription().substring(0,60) %>...
					<p> <%=book.getUnitPrice() %>원
					<p> <a href="./book.jsp?id=<%=book.getBookId() %>"
					class="btn btn-secondary" role="button"> 상세 정보 &raquo;</a>
				</div>
			</div>
			<%
				}
			%>
		</div>
		<%@ include file="footer.jsp" %>
	</div>
</body>
</html>
`

---

### 📄 src/main/webapp/book.jsp — 5장 request 내장 객체 이용 상세 페이지

`jsp
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ page import="dto.Book" %>
<%@ page import="dao.BookRepository" %>

<html>
<head>
	<meta charset="UTF-8">
	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
	<link rel = "stylesheet" href="./resources/css/bootstrap.min.css" />
	<title>도서 상세 정보</title>
</head>

<body>
	<div class="container py-4">
		<%@ include file="menu.jsp" %>
		
		<div class="p-5 mb-4 bg-body-tertiary rounded-3">
			<div class="container-fluid py-5">
				<h1 class="display-5 fw-bold">도서 정보</h1>
				<p class="col-md-8 fs-4">BookInfo</p>
			</div>
		</div>
		
		<% 
			String id = request.getParameter("id");
			BookRepository dao = BookRepository.getInstance();
			Book book = dao.getBookById(id);
		%>
		
		<div class = "row align-items-md-stretch">
			<div class="col-md-5">
				<img src = "./resources/images/<%= book.getFilename() %>" style="width : 70% ">
			</div>	
				<div class = "col-md-6">
					<h3><b><%=book.getName() %></b></h3>
					<p> <%=book.getDescription() %>
					<p> <b>도서코드 : </b><span class="badge text-bg-danger"><%=book.getBookId() %></span>
					<p> <b>저자</b> : <%=book.getAuthor() %>
					<p> <b>출판사</b> : <%=book.getPublisher() %>
					<p> <b>출판일</b> : <%=book.getReleaseDate() %>
					<p> <b>분류</b> : <%=book.getCategory() %>
					<p> <b>재고 수</b> : <%=book.getUnitInStock() %>
					<h4> <%=book.getUnitPrice() %>원</h4>
					<p> <a href="#" class="btn btn-info">도서 주문 &raquo;</a>
					<a href="./books.jsp" class="btn btn-secondary"> 도서 목록 &raquo;</a>
				
			</div>
		</div>
		<jsp:include page="footer.jsp" />
	</div>
</body>
</html>
`

---

### 📄 src/main/webapp/addBook.jsp — 6장/7장 도서 등록 폼 (파일 업로드 포함)

`jsp
<%@ page contentType="text/html; charset=utf-8" %>
<html>
	<head>
		<link rel = "stylesheet" href="./css/bootstrap.min.css" />
		<title>도서 등록</title>
	</head>

	<body>
		<div class="container py-4">
			<%@ include file = "menu.jsp" %>
			
			<div class="p-5 mb-4 bg-body-tertiary rounded-3">
				<div class="container-fluid py-5">
					<h1 class = "display-5 fw-bold">도서 등록</h1>
					<p class="col-md-8 fs-4">Book Addition</p>
				</div>			
			</div>
			
			<div class="row align-items-md-stretch">
				<form name="newBook" action="./processAddBook.jsp" class="form-horizontal" method="post" enctype="multipart/form-data">
					
					<div class="mb-3 row">
						<label class="col-sm-2">도서코드</label>
						<div class="col-sm-3">
							<input type="text" name="bookId" class="form-control">
						</div>
					</div>
					
					<div class="mb-3 row">
						<label class="col-sm-2">도서명</label>
						<div class="col-sm-3">
							<input type="text" name="name" class="form-control">
						</div>
					</div>
					
					<div class="mb-3 row">
						<label class="col-sm-2">가격</label>
						<div class="col-sm-3">
							<input type="text" name="unitPrice" class="form-control">
						</div>
					</div>
					
					<div class="mb-3 row">
						<label class="col-sm-2">저자</label>
						<div class="col-sm-3">
							<input type="text" name="author" class="form-control">
						</div>
					</div>
					
					<div class="mb-3 row">
						<label class="col-sm-2">출판사</label>
						<div class="col-sm-3">
							<input type="text" name="publisher" class="form-control">
						</div>
					</div>
					
					<div class="mb-3 row">
						<label class="col-sm-2">출판일</label>
						<div class="col-sm-3">
							<input type="text" name="releaseDate" class="form-control">
						</div>
					</div>
					
					<div class="mb-3 row">
						<label class="col-sm-2">상세설명</label>
						<div class="col-sm-5">
							<textarea name="description" cols="50" rows="2"></textarea>
						</div>
					</div>
					
					<div class="mb-3 row">
						<label class="col-sm-2">분류</label>
						<div class="col-sm-3">
							<input type="text" name="category" class="form-control">
						</div>
					</div>
					
					<div class="mb-3 row">
						<label class="col-sm-2">재고수</label>
						<div class="col-sm-3">
							<input type="text" name="unitsInStock" class="form-control">
						</div>
					</div>
					
					<div class="mb-3 row">
						<label class="col-sm-2">상태</label>
						<div class="col-sm-5">
							<input type="radio" name="condition" value="New"> 신규도서
							<input type="radio" name="condition" value="Old"> 중고도서
							<input type="radio" name="condition" value="EBook"> E-Book
						</div>
					</div>
					
					<div class="mb-3 row">
						<label class = "col-sm-2">이미지</label>
						<div class = "col-sm-5">
							<input type = "file" name = "BookImage" class="form-control">
						</div>
					</div>
					
					<div class="mb-3 row">
						<div class="col-sm-offset-2 col-sm-10">
							<input type="submit" class="btn btn-primary" value="등록">
						</div>
					</div>
				</form>
			</div>	
			<jsp:include page="footer.jsp" />			
		
		</div>
	</body>
</html>
`

---

### 📄 src/main/webapp/processAddBook.jsp — 7장 파일 업로드 및 도서 동적 저장 처리

`jsp
<%@page import="java.util.Enumeration"%>
<%@page import="com.oreilly.servlet.multipart.*"%>
<%@page import="com.oreilly.servlet.*"%>
<%@page import="dto.Book"%>
<%@page import="dao.BookRepository"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>도서 등록 처리</title>
</head>
<body>
	<% 
	request.setCharacterEncoding("UTF-8");

	String realFolder = "C:\\Users\\AI-00\\Desktop\\하이테크_\\2ndTerm\\ServerProgramming\\JSPLecture\\BookMarket\\src\\main\\webapp\\resources\\images";
	
	int maxSize = 5 * 1024 * 1024; // 5MB
	String encType = "utf-8";
	
	MultipartRequest multi = new MultipartRequest(request, realFolder, maxSize, encType, new DefaultFileRenamePolicy());
	
	String bookId = multi.getParameter("bookId"); 
	String name = multi.getParameter("name"); 
	String unitPrice = multi.getParameter("unitPrice"); 
	String author = multi.getParameter("author"); 
	String publisher = multi.getParameter("publisher"); 
	String releaseDate = multi.getParameter("releaseDate"); 
	String description = multi.getParameter("description"); 
	String category = multi.getParameter("category"); 
	String unitInStock = multi.getParameter("unitsInStock"); 
	String condition = multi.getParameter("condition"); 

	Enumeration files = multi.getFileNames();
	String fname = (String) files.nextElement();
	String fileName = multi.getFilesystemName(fname);
	
	Integer price;
	if (unitPrice == null || unitPrice.isEmpty())
		price = 0;
	else
		price = Integer.valueOf(unitPrice);
	
	long stock;
	if (unitInStock == null || unitInStock.isEmpty())
		stock = 0;
	else
		stock = Long.valueOf(unitInStock);
	
	BookRepository dao = BookRepository.getInstance();

	Book newBook = new Book();
	newBook.setBookId(bookId);
	newBook.setName(name);
	newBook.setUnitPrice(price);
	newBook.setAuthor(author);
	newBook.setPublisher(publisher);
	newBook.setReleaseDate(releaseDate);
	newBook.setDescription(description);
	newBook.setCategory(category);
	newBook.setUnitInStock(stock);
	newBook.setCondition(condition);
	newBook.setFilename(fileName);

	dao.addBook(newBook);
	
	response.sendRedirect("books.jsp");
%>
</body>
</html>
`

---

## 5. 💡 Key Takeaways (핵심 아키텍처 정리표)

| 개념/기술 | 내용 및 역할 | 적용 파일 |
|---|---|---|
| **JavaBean (DTO)** | 도서 정보 속성을 캡슐화한 직렬화 객체 | Book.java |
| **Singleton DAO** | 메모리 상 단 하나의 객체로 도서 리스트 CRUD 담당 | BookRepository.java |
| **Include 모듈화** | 네비게이션 헤더와 바닥글 레이아웃을 재사용 모듈로 분리 | menu.jsp, ooter.jsp, welcome.jsp |
| **Request Parameter** | URL 쿼리 스트링(?id=ISBN1234)으로 선택한 도서 ID 전달 후 조회 | ooks.jsp -> ook.jsp |
| **Multipart Request** | cos.jar 라이브러리를 통해 이미지 파일과 폼 데이터를 함께 저장 | ddBook.jsp, processAddBook.jsp |