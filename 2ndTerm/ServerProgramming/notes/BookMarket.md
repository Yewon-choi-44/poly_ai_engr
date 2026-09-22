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
| 3장 | 인코딩 설정 및 페이지 모듈화 (헤더/푸터 분리) | welcome.jsp, menu.jsp, footer.jsp | ✅ 완료 |
| 4장 | JavaBeans 기반 도서 목록 조회 페이지 | Book.java, BookRepository.java, books.jsp | ✅ 완료 |
| 5장 | request 내장 객체 활용 도서 상세 정보 조회 | book.jsp | ✅ 완료 |
| 6장 | 폼 태그 기반 도서 신규 등록 페이지 | addBook.jsp | ✅ 완료 |
| 7장 | cos.jar(MultipartRequest) 이용 도서 이미지 업로드 | addBook.jsp, processAddBook.jsp | ✅ 완료 |
| 8장 | 유효성 검사 (자바스크립트) — 도서 등록 폼에 부분 적용 | addBook.jsp, resources/js/validation.js | 🔶 진행 중 (버그 있음, 아래 4·5번 참고) |

> 8장은 교재의 독립 실습(`JSPLecture/JSP0918/`, [`notes/2026-09-18.md`](./2026-09-18.md) 참고)과 별도로, BookMarket의 `addBook.jsp` 도서 등록 폼에도 클라이언트 사이드 검증이 실제로 통합되었습니다. 로그인/회원가입 폼(`login`, `register` 등)에는 아직 적용되지 않아 "진행 중"으로 표기합니다.

---

## 2. 프로젝트 디렉토리 구조

```
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
│       ├── addBook.jsp                 ← [6/7/8장] 도서 등록 폼 (multipart/form-data + 클라이언트 검증)
│       ├── processAddBook.jsp          ← [7장] 도서 등록 처리 (MultipartRequest 파일 업로드)
│       └── resources/
│           ├── css/
│           │   └── bootstrap.min.css   ← 부트스트랩 CSS (기존 ./css/ 에서 이 경로로 이동)
│           ├── js/
│           │   └── validation.js       ← [8장, 신규] 도서 등록 폼 클라이언트 사이드 유효성 검사
│           └── images/
│               ├── ISBN1234.jpg        ← 도서 1(seed) 이미지
│               ├── ISBN1235.jpg        ← 도서 2(seed) 이미지
│               ├── ISBN1236.jpg        ← 도서 3(seed) 이미지
│               ├── ISBN12341234.png    ← 실습 중 업로드 테스트로 생성된 이미지 (신규)
│               └── Thumbs.db           ← Windows 탐색기 캐시 (Git 미추적, .gitignore 처리됨)
```

> 🔧 **경로 변경**: 이전에는 CSS/이미지가 `webapp/css/`, `webapp/images/`에 직접 있었으나, 이번에 전부 `webapp/resources/{css,images,js}/` 하위로 재구성되었습니다. `processAddBook.jsp`의 이미지 저장 경로(`realFolder`)도 `...\webapp\images` → `...\webapp\resources\images`로 함께 수정되었습니다.

---

## 3. Java 소스 코드 (전체 원본 발췌)

### 📄 src/main/java/dto/Book.java — 도서 DTO (JavaBean)

```java
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
```

- **동작 원리**:
  - Serializable 인터페이스를 구현하여 객체 직렬화를 지원하는 표준 JavaBean 클래스입니다.
  - 도서의 모든 속성을 private 필드로 캡슐화하고 기본 생성자와 getter/setter 메서드를 제공합니다.

---

### 📄 src/main/java/dao/BookRepository.java — 도서 데이터 관리 DAO (싱글톤)

```java
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
```

- **동작 원리**:
  - 싱글톤 패턴(`getInstance()`)으로 애플리케이션 내 단 하나의 객체 메모리만 공유 관리합니다.
  - 생성자에서 기본 도서 3권 데이터를 초기화하며, `addBook()`, `getAllBooks()`, `getBookById()` 메서드로 CRUD 기능을 수행합니다.

---

## 4. JSP 실습 코드 (전체 원본 발췌)

### 📄 src/main/webapp/menu.jsp — 공통 헤더 네비게이션 모듈

```jsp
<header class = "pb-3 mb mb-4 border-bottom">
	<a href = "./welcome.jsp" class="d-flex align-items-center text-dark text-decoration-none">
		<svg width="32" height="32" fill="currentColor" class="bi bi-house-fill" viewBox="0 0 16 16">
			<path d = "M8.707 1.5a1 1 0 0 0-1.414 0L.646 8.146a.5.5 0 0 0 .708.708L82.207l6.646 6.647a.5.5 0 0 0 .708-.708L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293L8.707 1.5Z" />
			<path d = "m8 3.293 6 6V13.5a1.5 1.5 0 0 1-1.5 1.5h-9A1.5 1.5 0 0 1 2 13.5V9.293l6-6Z" />
		</svg>
		<span class = "fs-4">Home</span>
	</a>
</header>
```

---

### 📄 src/main/webapp/footer.jsp — 공통 바닥글 모듈

```jsp
<footer class = "pt-3 mt-4 text-body-secondary border-top">
	&copy; BookMarket
</footer> 
```

---

### 📄 src/main/webapp/Welcome0819.jsp — 2장 Bootstrap 초기 시작 페이지

```jsp
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
```

---

### 📄 src/main/webapp/welcome.jsp — 3장 include 디렉티브 모듈화 메인 페이지

```jsp
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
```

---

### 📄 src/main/webapp/books.jsp — 4장 도서 전체 목록 표시 페이지

```jsp
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
```

---

### 📄 src/main/webapp/book.jsp — 5장 request 내장 객체 이용 상세 페이지

```jsp
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
```

---

### 📄 src/main/webapp/addBook.jsp — 6/7/8장 도서 등록 폼 (파일 업로드 + 클라이언트 검증, 최신)

```jsp
<%@ page contentType="text/html; charset=utf-8"%>
<html>
<head>
<link rel ="stylesheet" href ="./resources/css/bootstrap.min.css" />
<script type="text/javascript" src="./resources/js/validation.js"></script>


<title>도서 등록</title>
</head>
<body>
<div class="container py-4">
   <%@ include file="menu.jsp"%>	

   <div class="p-5 mb-4 bg-body-tertiary rounded-3">
      <div class="container-fluid py-5">
        <h1 class="display-5 fw-bold">도서 등록</h1>
        <p class="col-md-8 fs-4">Book Addition</p>      
      </div>
    </div>
  
	 <div class="row align-items-md-stretch">	 	
		<form name="newBook" action="./processAddBook.jsp" method="post" enctype ="multipart/form-data">
		
			
			<div class="mb-3 row">
				<label class="col-sm-2">도서코드</label>
				<div class="col-sm-3">
					<input type="text" name="bookId" id="bookId" class="form-control" >
				</div>
			</div>
			<div class="mb-3 row">
				<label class="col-sm-2">도서명</label>
				<div class="col-sm-3">
					<input type="text" name="name" id="name" class="form-control" >
				</div>
			</div>
				<div class="mb-3 row">
				<label class="col-sm-2">가격</label>
				<div class="col-sm-3">
					<input type="text" name="unitPrice"  id="unitPrice"class="form-control" >
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
				<label class="col-sm-2">상세정보</label>
				<div class="col-sm-5">
					<textarea  name="description" id="description" cols="50" rows="2"
						class="form-control" placeholder="100자 이상 적어주세요"></textarea>
				</div>
			</div>			
			<div class="mb-3 row">
				<label class="col-sm-2">분류</label>
				<div class="col-sm-3">
					<input type="text" name="category" class="form-control" >
				</div>
			</div>
				<div class="mb-3 row">
				<label class="col-sm-2">재고수</label>
				<div class="col-sm-3">
					<input type="text" name="unitInStock" id="unitInStock"class="form-control" >
				</div>
			</div>
			<div class="mb-3 row">
				<label class="col-sm-2">상태</label>
				<div class="col-sm-5">
					<input type="radio" name="condition" value="New " > 신규도서 
					<input type="radio" name="condition" value="Old" > 중고도서 
					<input type="radio" name="condition" value="EBook" > E-Book
				</div>				
			</div>		
			
			<div class="mb-3 row">
				<label class="col-sm-2">이미지</label>
				<div class="col-sm-5">
					<input type="file" name="bookImage" class="form-control">
				</div>
			</div>
			
			<div class="mb-3 row">
				<div class="col-sm-offset-2 col-sm-10 ">
					<input type="button" class="btn btn-primary" value="등록" onclick="CheckAddBook()">
				</div>
			</div>
		</form>
	</div>
	<jsp:include page="footer.jsp" />
</div>	
</body>
</html>
```

- **동작 원리 (6/7장 대비 달라진 점)**:
  - CSS 경로가 `./css/bootstrap.min.css` → `./resources/css/bootstrap.min.css`로, 파일 업로드 저장 위치가 `webapp/images` → `webapp/resources/images`로 함께 이동했습니다(경로 재구성).
  - `<script src="./resources/js/validation.js">`로 검증 스크립트를 로드하고, 제출 버튼이 `type="submit"` → `type="button" onclick="CheckAddBook()"`로 바뀌어, **검증 함수가 `true`를 반환(=`document.newBook.submit()` 호출)할 때만 실제 제출**되는 구조로 전환되었습니다.
  - `bookId`, `name`, `unitPrice`, `description`, `unitInStock` 필드에 `id` 속성이 새로 추가되었습니다. `validation.js`가 `getElementById()`로 값을 읽기 위한 것입니다.
  - 필드명이 `unitsInStock`(복수형, 6/7장 당시) → `unitInStock`(단수형, `Book.java`의 실제 프로퍼티명과 일치)으로 수정되었고, 이미지 필드명도 `BookImage` → `bookImage`(소문자 시작)로 정리되었습니다.

---

### 📄 src/main/webapp/processAddBook.jsp — 7장 파일 업로드 및 도서 동적 저장 처리 (최신)

```jsp
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
<title>신규도서등록</title>
</head>
<body>
	<% 
	request.setCharacterEncoding("UTF-8");

	String filename = "";
	String realFolder = "C:\\Users\\AI-00\\Desktop\\하이테크_\\2ndTerm\\ServerProgramming\\JSPLecture\\BookMarket\\src\\main\\webapp\\resources\\images";
	
	int maxSize = 5 * 1024 * 1024;
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
	String unitInStock = multi.getParameter("unitInStock"); 
	String condition = multi.getParameter("condition"); 

	Enumeration files = multi.getFileNames();
	String fname = (String) files.nextElement();
	String fileName = multi.getFilesystemName(fname);
	
	Integer price;
	
	if (unitPrice.isEmpty())
		price=0;
	else
		price=Integer.valueOf(unitPrice);
	
	long stock;
	
	if (unitInStock.isEmpty())
		stock=0;
	else
		stock=Long.valueOf(unitInStock);
	
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
```

- **동작 원리 (7장 대비 달라진 점)**:
  - `realFolder` 저장 경로가 `webapp\images` → `webapp\resources\images`로 변경되어, `addBook.jsp`의 CSS/이미지 경로 재구성과 일관성을 맞췄습니다.
  - `multi.getParameter("unitsInStock")` → `multi.getParameter("unitInStock")`로 파라미터명이 수정되어, `addBook.jsp`의 `<input name="unitInStock">`과 이제 정확히 일치합니다(6/7장 당시에는 폼 필드명이 `unitsInStock`이었는데 DAO/DTO는 `unitInStock`이라 불일치가 있었던 것으로 보입니다).
  - `price`, `stock` 계산 시 `if (unitPrice == null || unitPrice.isEmpty())`처럼 있던 **`null` 체크가 사라지고** `if (unitPrice.isEmpty())`만 남았습니다 — 아래 "발견된 이슈" 참고.

---

### 📄 src/main/webapp/resources/js/validation.js — [8장, 신규] 도서 등록 폼 클라이언트 검증

```javascript
function CheckAddBook() {

	var bookId = document.getElementById("bookId");
	var name = document.getElementById("name");
	var unitPrice = document.getElementById("unitPrice");
	var unitsInStock = document.getElementById("unitsInStock");
	var description = document.getElementById("description");

	
	
	// 상품아아디 체크
	if (!check(/^ISBN[0-9]{4,11}$/, bookId,
			"[상품 코드]\nISBN과 숫자를 조합하여 5~12자까지 입력하세요\n첫 글자는 반드시 ISBN로 시작하세요"))
		return false;
	// 상품명 체크
	
	if (name.value.length < 4 || name.value.length > 12) {
		alert("[상품명]\n최소 4자에서 최대 50자까지 입력하세요");
		name.select();
		name.focus();
		return false;
	}
	// 상품 가격 체크
	if (unitPrice.value.length == 0 || isNaN(unitPrice.value)) {
		alert("[가격]\n숫자만 입력하세요");
		unitPrice.select();
		unitPrice.focus();
		return false;
	}

	if (unitPrice.value < 0) {
		alert("[가격]\n음수를 입력할 수 없습니다");
		unitPrice.select();
		unitPrice.focus();
		return false;
	} else if (!check(/^\d+(?:[.]?[\d]?[\d])?$/, unitPrice,
			"[가격]\n소수점 둘째 자리까지만 입력하세요"))
		//return false;

	// 재고 수 체크
	if (isNaN(unitsInStock.value)) {
		alert("[재고 수]\n숫자만 입력하세요");
		unitsInStock.select();
		unitsInStock.focus();
		return false;
	}
	
	if (description.value.length < 80) {
		alert("[상세설명]\n최소 100자이상 입력하세요");
		description.select();
		description.focus();
		return false;
	}
	
	function check(regExp, e, msg) {

		if (regExp.test(e.value)) {
			return true;
		}
		alert(msg);
		e.select();
		e.focus();
		return false;
	}

	 document.newBook.submit()
}
```

- **동작 원리**:
  - `addBook.jsp`의 제출 버튼(`onclick="CheckAddBook()"`)에서 호출되는 함수로, `getElementById()`로 각 필드를 가져와 순서대로 검증하고 마지막에 `document.newBook.submit()`으로 실제 제출합니다.
  - 도서코드는 정규식(`/^ISBN[0-9]{4,11}$/`)으로 "ISBN + 숫자 4~11자리"인지, 가격은 `isNaN()`과 소수점 자릿수 정규식으로, 상세설명은 길이(`length < 80`)로 검증합니다.
  - 내부에 `check(regExp, e, msg)` 헬퍼 함수를 선언해두고 여러 곳(도서코드, 가격)에서 재사용합니다. 함수 선언이 함수 본문 **중간**에 있지만, 자바스크립트의 함수 선언 호이스팅(hoisting) 덕분에 `check()`가 선언 이전 위치(도서코드 체크 부분)에서 호출되어도 정상 동작합니다.

> ⚠️ **버그 다수 발견** — 아래 5번 "발견된 이슈"에 상세 정리.

---

## 5. ⚠️ 발견된 이슈 (다음 실습 시 확인/수정 필요)

| 위치 | 증상 | 원인 |
|---|---|---|
| `validation.js` `CheckAddBook()` | 재고수 입력값이 항상 "숫자가 아님" 취급되어 재고 검증 단계에서 계속 걸리거나, 반대로 검증이 아예 실행되지 않음 | `document.getElementById("unitsInStock")`로 조회하는데, `addBook.jsp`의 실제 `id`는 `unitInStock`(복수형 `s` 없음). 존재하지 않는 id를 조회하면 `getElementById`가 `null`을 반환하므로, 이후 `unitsInStock.value`에서 `TypeError: Cannot read properties of null`이 발생해 **재고 수 체크 이후 로직 전체가 멈추고 폼이 제출되지 않을 가능성**이 있음 |
| `validation.js` `CheckAddBook()` | 재고 수 체크가 "가격이 소수점 둘째 자리를 초과했을 때"만 실행됨 | 가격 검증부의 `else if (!check(...)) \n //return false;` 에서 `if`에 딸린 실행문이 없고(주석 처리됨), 그 아래 빈 줄을 건너뛰어 **바로 다음의 `if (isNaN(unitsInStock.value)) {...}` 블록 전체가 이 `else if`에 종속**됩니다. 즉 가격이 정상(else if 조건이 거짓)이면 재고 수 검증 자체가 통째로 스킵되고, 가격 정규식이 실패했을 때만 재고 수 검증이 실행되는 의도치 않은 흐름입니다 |
| `processAddBook.jsp` | `unitPrice`나 `unitInStock` 파라미터가 폼에서 전달되지 않는 경우(`null`) 500 에러(NullPointerException) | 기존에 있던 `unitPrice == null` / `unitInStock == null` 널 체크가 이번 수정에서 빠지고 `unitPrice.isEmpty()` / `unitInStock.isEmpty()`만 남음. `MultipartRequest.getParameter()`가 `null`을 반환하는 상황이면 `.isEmpty()` 호출 자체에서 예외 발생 |
| `resources/images/` | 실습 중 생성된 테스트 업로드 파일(`ISBN12341234.png`)이 seed 이미지(`ISBN1234.jpg` 등)와 섞여 있음 | 기능 테스트 산출물로 보이며, 필요 없다면 정리 대상 |

---

## 6. 💡 Key Takeaways (핵심 아키텍처 정리표)

| 개념/기술 | 내용 및 역할 | 적용 파일 |
|---|---|---|
| **JavaBean (DTO)** | 도서 정보 속성을 캡슐화한 직렬화 객체 | Book.java |
| **Singleton DAO** | 메모리 상 단 하나의 객체로 도서 리스트 CRUD 담당 | BookRepository.java |
| **Include 모듈화** | 네비게이션 헤더와 바닥글 레이아웃을 재사용 모듈로 분리 | menu.jsp, footer.jsp, welcome.jsp |
| **Request Parameter** | URL 쿼리 스트링(`?id=ISBN1234`)으로 선택한 도서 ID 전달 후 조회 | books.jsp → book.jsp |
| **Multipart Request** | cos.jar 라이브러리를 통해 이미지 파일과 폼 데이터를 함께 저장 | addBook.jsp, processAddBook.jsp |
| **정적 리소스 경로 재구성** | `webapp/css`, `webapp/images` → `webapp/resources/{css,images,js}`로 통합 | addBook.jsp, book.jsp, books.jsp, processAddBook.jsp |
| **버튼 클릭 검증 → 명시적 submit** | `type="button" onclick="검증함수()"` 후 통과 시에만 `form.submit()` 호출 | addBook.jsp, resources/js/validation.js |
| **함수 선언 호이스팅** | 함수 본문 중간의 내부 함수 선언도 호이스팅되어 그보다 앞선 코드에서 호출 가능 | validation.js의 `check()` |
