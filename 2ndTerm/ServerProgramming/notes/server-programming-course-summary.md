# Server Programming (서버 프로그래밍) 수업 정리

> 교재: 《쉽게 배우는 JSP 웹 프로그래밍(2판)》(송미영 저, 한빛아카데미, ISBN 979-11-5664-006-6)
> 실습 프로젝트: **BookMarket**(도서 쇼핑몰) — 각 장에서 배운 내용을 누적 적용하며 완성해 가는 방식
> 자료 출처: `REFERENCES/server-programming/ppt_40006`(강의 슬라이드), `answer_40006`(연습문제 해답), `fig_40006`(교재 그림/표), `source`(예제·해답 소스 및 실습 환경 설치 파일)

---

## 1. 강의 개요

- **총 16주 구성**(중간고사 8주차, 기말고사 16주차)
- 교재 18개 장을 강의 순서에 맞춰 2개 장씩 묶어 진행
- 매 장마다 "이론 학습 → 개별 예제 실습 → BookMarket 프로젝트에 적용" 순서로 진행

### 주차별 진행표

| 주차 | 장 | 내용 |
|---|---|---|
| 1 | 1장, 2장 | JSP의 개요: 원리 이해 및 개발 환경 구축 / 스크립트 태그: 시작 페이지 만들기 |
| 2 | 3장, 4장 | 디렉티브 태그: 한글 출력 및 페이지 모듈화 / 액션 태그: 도서 목록 표시 |
| 3 | 5장, 6장 | 내장 객체: 도서 상세 정보 표시 / 폼 태그: 도서 등록 페이지 만들기 |
| 4 | 7장 | 파일 업로드: 도서 이미지 등록 |
| 5 | 8장 | 유효성 검사: 도서 등록 데이터 검증 |
| 6 | 9장 | 다국어 처리: 도서 등록 페이지 다국어 처리 |
| 7 | 10장 | 시큐리티: 도서 등록 페이지 보안 처리 |
| 8 | — | **중간고사** |
| 9 | 11장 | 예외 처리: 예외 처리 페이지 만들기 |
| 10 | 12장 | 필터: 로그 기록하기 |
| 11 | 13장, 14장 | 세션: 장바구니 페이지 / 쿠키: 주문 처리 페이지 |
| 12 | 15장 | 데이터베이스 개발 환경 구축: 도서 관리 테이블 생성·도서 등록 |
| 13 | 16장 | JDBC로 데이터베이스와 JSP 연동: 도서 조회·등록·수정·삭제 |
| 14 | 17장 | JSP 표준 태그 라이브러리(JSTL): 회원 가입·수정·탈퇴 |
| 15 | 18장 | 웹 MVC: 게시판 만들기 |
| 16 | — | **기말고사** |

### 교재 5단계 로드맵

1. **JSP 개요 및 설치**(1장) — 개발 환경 구축
2. **JSP 기본 문법**(2~5장) — 스크립트 태그, 디렉티브 태그, 액션 태그, 내장 객체 → BookMarket 시작 페이지·모듈화·목록·상세정보 구현
3. **페이지 처리 기법**(6~12장) — 폼, 파일 업로드, 유효성 검사, 다국어, 보안, 예외 처리, 필터 → 등록 페이지·이미지 등록·검증·다국어·보안 처리 구현
4. **세션·쿠키·데이터베이스**(13~16장) — 세션, 쿠키, DB 구축, JDBC API → 장바구니·주문 처리·도서 CRUD 구현
5. **JSP 고급 문법**(17~18장) — JSTL, MVC 패턴 → 회원 가입/수정/탈퇴·게시판 구현

### 실습 환경(2판 개정 반영)

- **JDK**: Java 20
- **웹 서버**: Apache Tomcat 10.1.x (Jakarta EE 기반, `javax.*` → `jakarta.*` 패키지 마이그레이션 필요)
- **IDE**: Eclipse IDE for Enterprise Java Developers (2023-06)
- **DBMS**: MySQL 8.0.34 + MySQL Connector/J 8.0.33
- 파일 업로드용 오픈 라이브러리: `cos.jar`(cos-22.05), `commons-fileupload`, `commons-io`
- JSTL 라이브러리: `jstl-1.2.jar`

---

## 2. 장별 핵심 내용

### 1장. JSP의 개요
- 인터넷/웹의 동작 원리(클라이언트-서버 방식), 정적 vs 동적 웹 페이지
- 서블릿과 JSP의 개념·특징·차이, 동작 과정과 생명주기(웹 서버 / 웹 컨테이너 / WAS 개념 포함)
- JDK·Tomcat·Eclipse 설치 및 연동, 동적 웹 프로젝트 생성
- 실습: `JSPBook` 예제 프로젝트, `BookMarket` 프로젝트 생성 및 첫 실행

### 2장. 스크립트 태그 — [BookMarket] 시작 페이지 만들기
- 스크립트 태그(`<% %>`)의 JSP→서블릿 변환 원리
- **선언문 태그**(`<%! %>`): 전역 변수·메소드 선언
- **스크립틀릿 태그**(`<% %>`): 지역 변수, 로직(반복문 등)
- **표현문 태그**(`<%= %>`): 출력 전용, `out.print()`와 동일 효과
- JSP 주석(`<%-- --%>`) vs HTML 주석의 차이
- 실습: 부트스트랩 CSS를 적용한 BookMarket 시작 페이지 제작

### 3장. 디렉티브 태그 — [BookMarket] 한글 출력 및 페이지 모듈화
- **page 디렉티브**: `contentType`, `pageEncoding`, `import`, `session`, `buffer`, `autoFlush`, `isThreadSafe`, `info`, `errorPage`, `isErrorPage`, `isELIgnored`, `isScriptingEnabled` 등 속성 전반
- **include 디렉티브**: 외부 파일 정적 포함(변환 시점에 병합)
- **taglib 디렉티브**: JSTL 등 태그 라이브러리 설정
- 실습: 한글 인코딩 처리, 머리글/본문/바닥글로 페이지 모듈화

### 4장. 액션 태그 — [BookMarket] 도서 목록 표시하기
- **forward**: 다른 페이지로 제어 이동(버퍼 초기화)
- **include**: 외부 파일 실행 결과 포함(런타임 시점, `include` 디렉티브와 차이)
- **param**: forward/include와 함께 파라미터 전달
- **자바빈즈(JavaBeans)**: 작성 규칙(Serializable, 기본 생성자, private 프로퍼티, Getter/Setter)
- `useBean`(빈 생성/검색), `setProperty`(값 저장), `getProperty`(값 조회)
- 실습: 도서(Book) 클래스와 도서 데이터 접근 클래스 작성, 도서 목록 페이지 구현

### 5장. 내장 객체 — [BookMarket] 도서 상세 정보 표시하기
- 내장 객체 개념(JSP 컨테이너가 `_jspService()`에 자동 포함)
- **request**: 요청 파라미터 조회, HTTP 헤더 조회, 웹 브라우저/서버 정보, 속성 유효 범위(scope)
- **response**: 페이지 이동(리다이렉션), 응답 헤더 설정, 응답 콘텐츠(MIME·인코딩·오류 코드) 설정
- **out**: 출력 스트림 객체, 표현문 태그와 동일한 역할
- 실습: 도서 상세 정보 페이지, 접속 시각 자동 갱신

### 6장. 폼 태그 — [BookMarket] 도서 등록 페이지 만들기
- **form** 태그(GET/POST 방식 차이), **input**, **select/option**, **textarea** 태그
- 폼 데이터 처리: `getParameter()`(개별), 일괄 처리 메소드(`getParameterNames()`, `getParameterValues()` 등)
- 실습: 도서 등록 페이지(form)와 등록 처리 페이지 작성, 도서 목록/상세 페이지 갱신

### 7장. 파일 업로드 — [BookMarket] 도서 이미지 등록하기
- 파일 업로드 폼 규칙(`method=POST`, `enctype=multipart/form-data`, `input type=file`)
- **MultipartRequest**(cos.jar): 파일과 일반 데이터 동시 처리, 한글 인코딩 용이
- **Commons-FileUpload**(commons-fileupload.jar, commons-io.jar): `DiskFileUpload`, `FileItem` 클래스
- Java EE → Jakarta EE 마이그레이션(패키지명 `javax.*` → `jakarta.*`) 방법 별도 설명
- 실습: 도서 이미지 정적 리소스 관리, 이미지 업로드 기능 구현

### 8장. 유효성 검사 — [BookMarket] 도서 등록 데이터의 유효성 검사하기
- 자바스크립트 기반 클라이언트 측 유효성 검사(핸들러 함수, `onsubmit`/`onclick`)
- 기본 검사: 데이터 유무(null/빈 문자열), 데이터 길이, 숫자 여부(`isNaN()`)
- 데이터 형식 검사: 정규 표현식(메타 문자, 문자 클래스), 이메일/전화번호/주민번호 패턴
- 실습: `validation.js` 작성, 도서 등록 페이지에 유효성 검사 적용

### 9장. 다국어 처리 — [BookMarket] 도서 등록 페이지의 다국어 처리하기
- 국제화(i18n)와 지역화(L10n) 개념
- **Locale 클래스**: 로케일 감지(`request.getLocale()`), 언어/날짜·시간/통화·숫자 표현
- **JSTL fmt 태그**: `setLocale`, `requestEncoding`, `bundle`/`message`/`setBundle`(리소스번들), `formatNumber`/`parseNumber`, `formatDate`/`parseDate`, `timeZone`/`setTimeZone`
- 실습: 한글/영문 `*.properties` 리소스번들 작성, 도서 등록 페이지 다국어 지원

### 10장. 시큐리티 — [BookMarket] 도서 등록 페이지의 보안 처리하기
- 인증(authentication)과 권한 부여(authorization) 개념
- 웹 서버(Tomcat) `tomcat-users.xml`에 역할·사용자 구성
- **선언적 시큐리티**: `web.xml`의 `<security-role>`, `<security-constraint>`(`<web-resource-collection>`, `<auth-constraint>`, `<user-data-constraint>`), `<login-config>`(`<auth-method>`: BASIC/DIGEST/FORM/CLIENT-CERT, `<form-login-config>`)
- **프로그래밍적 시큐리티**: `request.isUserInRole()` 등 코드 기반 권한 처리
- 실습: 로그인 인증을 통한 도서 등록 페이지 접근 제한, 로그아웃 구현

### 11장. 예외 처리 — [BookMarket] 예외 처리 페이지 만들기
- 예외 처리 개요(웹 서버 기본 오류 페이지의 보안 취약점)
- **page 디렉티브 방식**: `errorPage`/`isErrorPage` 속성 조합, `exception` 내장 객체
- **web.xml 방식**: `<error-page>`의 `<error-code>`(404, 500 등) / `<exception-type>` 매핑
- **try-catch-finally**: 스크립틀릿 내 자바 표준 예외 처리 구문
- 실습: 도서 상세 페이지 오류 대응, `web.xml` 오류 코드 매핑

### 12장. 필터 — [BookMarket] 로그 기록하기
- 필터(filter) 개념: 클라이언트-서버 사이 요청/응답 전처리·후처리
- **Filter 인터페이스**: `init()`, `doFilter()`(request/response/FilterChain), `destroy()`
- `web.xml`의 `<filter>`, `<filter-mapping>`(URL 패턴 유형: 경로/확장자/정확matching)
- 실습: 로그인 인증 처리 필터, 로그 기록 파일 생성 필터

### 13장. 세션 — [BookMarket] 장바구니 페이지 만들기
- 세션(session) 개념: 서버 측 상태 유지, 웹 브라우저당 하나씩 존재
- 생성: `setAttribute()` / 조회: `getAttribute()`, `getAttributeNames()`
- 삭제: `removeAttribute()`(단일), `invalidate()`(전체)
- 유효 시간: `setMaxInactiveInterval()`(기본값 1,800초)
- 실습: 세션 기반 장바구니 담기/삭제(개별·전체) 기능 구현

### 14장. 쿠키 — [BookMarket] 주문 처리 페이지 만들기
- 쿠키(cookie) 개념: 클라이언트 측 상태 저장, 세션과의 차이(저장 위치, 보안성)
- 생성: `Cookie()` + `response.addCookie()`
- 조회: `request.getCookies()`, `getName()`/`getValue()`
- 삭제: `setMaxAge(0)`
- 실습: 배송 정보/주문 정보/주문 완료/주문 취소 페이지 구현

### 15장. 데이터베이스 개발 환경 구축 — [BookMarket] 도서 관리 테이블 생성 및 도서 등록하기
- 데이터베이스·DBMS 개념, MySQL 특징
- MySQL 8.0 설치, MySQL Connector/J 드라이버 설치 및 Eclipse 연동(Data Source Explorer)
- SQL 기본 명령어: 테이블 생성/조회/변경(`CREATE`, `ALTER`, `RENAME`), 데이터 조작(`INSERT`, `SELECT`, `UPDATE`, `DELETE`)
- 실습: `BookMarketDB` 데이터베이스 및 도서 관리 테이블 생성, 도서 데이터 등록(`book.sql`, `insert.sql`)

### 16장. JDBC로 데이터베이스와 JSP 연동 — [BookMarket] 도서 조회·등록·수정·삭제하기
- JDBC 개요와 처리 흐름(드라이버 로딩 → Connection 생성 → 쿼리 실행 → 결과 처리 → 자원 반납)
- 드라이버 로딩(`Class.forName()`), `DriverManager.getConnection()`, `close()`
- **Statement**(정적 쿼리) vs **PreparedStatement**(동적 쿼리, `?` 파라미터 바인딩)
- `executeQuery()`(조회), `executeUpdate()`(삽입/수정/삭제), **ResultSet** 객체로 결과 접근
- 실습: DB 연동으로 도서 목록 조회, 신규 등록, 수정, 삭제(CRUD 전체) 구현

### 17장. JSP 표준 태그 라이브러리(JSTL) — [BookMarket] 회원 가입·수정·탈퇴하기
- JSTL 개념과 사용자 정의 태그의 이점(재사용성, 가독성, 역할 분담)
- **Core 태그**: 표현 지원(`c:out`, `c:set`, `c:remove`, `c:catch`), 흐름 제어(`c:if`, `c:choose/when/otherwise`, `c:forEach`, `c:forTokens`), URL 관리(`c:import`, `c:param`, `c:redirect`, `c:url`)
- **SQL 태그**: `sql:query`(SELECT), `sql:update`(INSERT/UPDATE/DELETE)
- **Functions 태그**: `fn:contains`, `fn:containsIgnoreCase`, `fn:split`, `fn:join` 등 문자열 처리
- 실습: 회원 관리 테이블 생성, 회원 가입/수정/탈퇴, 로그인/로그아웃 페이지 구현

### 18장. 웹 MVC — [BookMarket] 게시판 만들기
- MVC 패턴: Model(데이터·비즈니스 로직) / View(출력) / Controller(흐름 제어)
- **모델 1**(JSP 중심, 로직과 출력이 혼재) vs **모델 2**(서블릿 컨트롤러 + JSP 뷰 + 자바빈즈 모델로 분리)
- 컨트롤러 서블릿 구성: `web.xml`의 `<servlet>`/`<servlet-mapping>`(URL 패턴, `.do` 확장자 매핑 관례), `doGet()`/`doPost()`, 포워딩 처리
- 실습: MVC 패턴을 적용한 로그인 인증 예제, BookMarket 게시판 구현(과정의 최종 단계)

---

## 3. 실습 프로젝트(BookMarket) 진화 흐름

```
1장  프로젝트 생성 및 초기 실행
2장  시작 페이지(부트스트랩 CSS 적용)
3장  한글 출력 + 페이지 모듈화(머리글/바닥글)
4장  도서 목록 표시(자바빈즈 기반 Book 클래스)
5장  도서 상세 정보 표시(request/response/out 내장 객체)
6장  도서 등록 페이지(폼 태그)
7장  도서 이미지 등록(파일 업로드)
8장  도서 등록 데이터 유효성 검사(자바스크립트)
9장  도서 등록 페이지 다국어 처리(JSTL fmt)
10장 도서 등록 페이지 보안 처리(로그인 인증)
──────────── 중간고사 ────────────
11장 예외 처리 페이지
12장 로그 기록(필터)
13장 장바구니 페이지(세션)
14장 주문 처리 페이지(쿠키)
15장 도서 관리 테이블 생성 및 도서 등록(MySQL 연동)
16장 도서 조회/등록/수정/삭제(JDBC 연동, DB 기반으로 전환)
17장 회원 가입/수정/탈퇴(JSTL 활용)
18장 게시판 만들기(MVC 패턴 적용)
──────────── 기말고사 ────────────
```

---

## 4. 참고 자료 위치

| 구분 | 경로 |
|---|---|
| 강의 슬라이드(Ch00~Ch18) | `REFERENCES/server-programming/ppt_40006/` |
| 교재 그림·표 자료(장별) | `REFERENCES/server-programming/fig_40006/` |
| 연습문제 해답(PDF/HWP) | `REFERENCES/server-programming/answer_40006/` |
| 연습문제 해답 소스코드 | `REFERENCES/server-programming/answer_40006/실습연습문제_해답소스/` |
| 장별 예제 소스(JSPBook) | `REFERENCES/server-programming/source/JSPBook/` |
| BookMarket 단계별 소스(01~18) | `REFERENCES/server-programming/source/BookMarket/` |
| 실습 환경 설치 파일(JDK/Tomcat/Eclipse/cos/MySQL) | `REFERENCES/server-programming/source/실습환경/` |
