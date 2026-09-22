# 📁 Spring_2026 디렉토리 구조 및 변경 이력

본 문서는 `Spring_2026` 워크스페이스의 프로젝트 구조 및 일별 변경 내역을 관리하는 문서입니다.

---

## 📌 전체 디렉토리 구조

```text
Spring_2026/
├── .gitignore                      # Git 추적 제외 규칙 (.metadata, target, logs, .settings 등)
├── AGENTS.md                       # AI 어시스턴트 행동 지침 및 수업 실습 관리 원칙 (구 GEMINI.md)
├── DirectoryStructure.md           # 디렉토리 구조 및 일별 변경 이력 관리 문서
├── README.md                       # 워크스페이스 메인 소개 및 실습 바로가기 문서
│
├── 0901WebTest/                    # [프로젝트 1] Spring Boot + JSP 기본 웹 테스트 프로젝트
│   └── src/
│       └── main/
│           ├── resources/
│           │   └── application.properties      # 서버 포트(8090) 및 JSP 뷰 리졸버 설정
│           └── webapp/WEB-INF/views/           # JSP 뷰 파일 (hello, about, greet, today)
│               ├── hello.jsp                   # JSP 스크립트릿으로 현재 시각 출력
│               ├── about.jsp                   # 정적 자기소개 페이지
│               ├── greet.jsp                   # @RequestParam → EL ${name} 출력
│               └── today.jsp                   # Model로 title·author·comment 전달
│
├── MiniBookMarket/                 # [프로젝트 2] 미니 도서 마켓 프로젝트
│   └── src/
│       └── main/
│           ├── resources/
│           │   └── application.properties      # 서버 포트(8017) 및 JSP 뷰 리졸버 설정
│           └── webapp/WEB-INF/views/           # JSP 뷰 파일 (intro, book, recent, review)
│
├── ai-Library/                     # [프로젝트 3] AITECH 도서관 — MySQL 연동, DAO 패턴, Bootstrap UI
│   ├── pom.xml                     # Maven 설정 (Spring MVC, JDBC, MySQL, JSTL, Jasper)
│   └── src/
│       ├── main/
│       │   ├── java/com/aitech/library/
│       │   │   ├── AiLibraryApplication.java   # Spring Boot 진입점 (@SpringBootApplication)
│       │   │   ├── HomeController.java          # 화면 라우팅 (/, /loginmember, /registermember, /findpassword, /modifymember)
│       │   │   ├── DBTestController.java        # DB 연결 테스트 (/dbTest, /dbInsert)
│       │   │   ├── ServletInitializer.java      # WAR 배포 초기화
│       │   │   ├── book/
│       │   │   │   ├── BookController.java      # 도서 목록 조회 (/booklist)
│       │   │   │   ├── BookDao.java             # JDBC 직접 사용 DAO (insertBook, getAllBook)
│       │   │   │   ├── BookRowMapper.java       # RowMapper 구현체 (ResultSet → BookVo)
│       │   │   │   └── BookVo.java              # 도서 데이터 VO (b_no, b_name, b_author 등 11개 필드)
│       │   │   └── config/
│       │   │       └── DBconfig.java            # @Configuration, DataSource/JdbcTemplate 빈 설정
│       │   ├── resources/
│       │   │   ├── application.properties      # 서버 포트(8090), JSP 뷰 리졸버, Multipart 업로드 설정
│       │   │   └── db.properties                # DB 접속 정보 (⚠️ Git 미추적, .gitignore 등록됨)
│       │   └── webapp/WEB-INF/views/
│       │       ├── home.jsp                    # 홈 화면 (도서 목록으로 리다이렉트)
│       │       ├── include/
│       │       │   ├── header.jsp              # 공통 헤더 (Bootstrap 5.3.8, 네비게이션 바 + 관리자메뉴 링크)
│       │       │   └── footer.jsp              # 공통 푸터 (Bootstrap JS 번들)
│       │       ├── book/
│       │       │   ├── book_list.jsp           # 도서 목록 (JSTL c:forEach, Bootstrap 카드 UI)
│       │       │   └── book_detail.jsp         # 도서 상세 조회 (이미지 + 정보 테이블)
│       │       ├── user/
│       │       │   ├── login_member.jsp        # 회원 로그인 폼 (현재 Controller 매핑 비활성화)
│       │       │   ├── register_member.jsp     # 회원 가입 폼 (현재 Controller 매핑 비활성화)
│       │       │   ├── modify_member.jsp       # 회원 정보 수정 폼 (현재 Controller 매핑 비활성화)
│       │       │   └── find_password.jsp       # 비밀번호 찾기 폼 (현재 Controller 매핑 비활성화)
│       │       └── admin/
│       │           ├── management_book.jsp     # 관리자 도서 관리 페이지 (실제 CRUD 연동)
│       │           ├── register_book.jsp       # 도서 등록 폼 (이미지 업로드 포함, views/ → admin/ 이동)
│       │           └── modify_book.jsp         # 도서 수정 폼 (기존 값 프리필 + 이미지 교체)
│       └── test/
│           └── java/com/aitech/library/
│               └── AiLibraryApplicationTests.java
│
├── upload/book_images/             # 업로드된 도서 표지 이미지 저장 폴더 (런타임 생성, ai-Library 하위)
│
└── daily_practice/                 # 📚 일별 실습 아카이빙 폴더
    ├── 260901_tue/                 # [2026-09-01 화] 실습 아카이브
    │   ├── 2026-09-01.md           # 2026-09-01 실습 상세 정리 문서
    │   ├── 0901WebTest/            # 0901WebTest JSP 뷰 아카이브 (hello, about, greet, today)
    │   └── MiniBookMarket/         # MiniBookMarket 소스 아카이브
    ├── until_260922_mon/           # [2026-09-22 월, 이전 스냅샷] 도서 등록+목록 조회까지 구현된 시점 아카이브
    │   ├── 2026-09-22.md           # 순수 JDBC(DataSource 직접 사용) 방식 시점의 정리 문서
    │   └── ai-Library/             # 당시 소스 스냅샷
    └── 260922_mon/                 # [2026-09-22 월, 최신] 도서 CRUD 완성 + 이미지 업로드 아카이브
        ├── 2026-09-22.md           # 최신 실습 정리 문서 (JdbcTemplate 전환, Multipart 업로드, CRUD 완성)
        └── ai-Library/             # 최신 소스 스냅샷
```

---

## 🕒 변경 이력 (Changelog)

### 📅 2026-09-22 (월) — `GEMINI.md` → `AGENTS.md` 이름 변경

| 구분 | 대상 경로 | 세부 내용 |
| :---: | :--- | :--- |
| 🔧 변경 | `GEMINI.md` → `AGENTS.md` | 여러 AI 코딩 도구가 공통으로 인식하는 `AGENTS.md` 관례를 따르기 위해 파일명 변경 (`git mv`로 이력 보존, 내용 변경 없음) |
| 🔧 변경 | `README.md` | AI 행동 지침 바로가기 링크를 `AGENTS.md`로 갱신 |
| 🔧 변경 | `DirectoryStructure.md` | 전체 트리의 파일명을 `AGENTS.md`로 갱신 (과거 변경 이력 항목들은 당시 파일명 `GEMINI.md` 그대로 유지) |

---

### 📅 2026-09-22 (월) — 도서 CRUD 완성 및 이미지 업로드 기능 추가

- **실습 주제**: `MultipartFile` 이미지 업로드, 도서 상세조회/수정/삭제, `BookDao`의 `JdbcTemplate` 전환

| 구분 | 대상 경로 | 세부 내용 |
| :---: | :--- | :--- |
| 🔧 변경 | `ai-Library/.../book/BookController.java` | `/registerbookconfirm`(이미지 업로드 저장), `/bookdetail`, `/modifybook`, `/modifybookconfirm`, `/deletebook` 매핑 추가 |
| 🔧 변경 | `ai-Library/.../book/BookDao.java` | `DataSource` 직접 사용 방식 → `JdbcTemplate` + `BookRowMapper` 방식으로 리팩터링, `getDetailBook`/`updateBook`/`deleteBook` 추가 |
| ➕ 추가 | `ai-Library/.../views/book/book_detail.jsp` | 도서 상세 조회 페이지 신규 생성 |
| ➕ 추가 | `ai-Library/.../views/admin/modify_book.jsp` | 도서 수정 폼 신규 생성 |
| 🔧 변경 | `ai-Library/.../views/admin/register_book.jsp` | `views/register_book.jsp` → `views/admin/register_book.jsp`로 이동, 이미지 업로드 `<input type="file">` 추가 |
| 🔧 변경 | `ai-Library/.../views/admin/management_book.jsp` | 정적 더미 데이터 → 실제 CRUD 연동 (등록/수정/삭제 버튼, 이미지 썸네일) |
| 🔧 변경 | `ai-Library/.../views/include/header.jsp` | "관리자메뉴" 네비게이션 링크 추가 |
| ➕ 추가 | `ai-Library/upload/book_images/` | 업로드된 도서 표지 이미지 저장 폴더 (런타임 생성, Git 미추적 대상) |
| 🔧 변경 | `ai-Library/src/main/resources/application.properties` | Multipart 업로드 크기 제한(10MB), 업로드 폴더 정적 리소스 매핑 추가 |
| 🔧 변경 | `ai-Library/.../HomeController.java`, `DBTestController.java` | 회원 관련 4개 매핑, DB 테스트 2개 매핑 임시 주석 처리 |
| ➕ 추가 | `daily_practice/260922_mon/` | 오늘자 최신 소스 및 `2026-09-22.md` 정리 문서 신규 아카이빙 |
| 🔧 변경 | `daily_practice/260922_mon/` (기존) → `daily_practice/until_260922_mon/` | 이전 시점(도서 등록+목록만 구현) 아카이브를 이름 변경하여 별도 보존 |
| 🔧 변경 | `DirectoryStructure.md`, `README.md` | 전체 트리 및 일별 아카이브 표를 최신 상태로 갱신 |
| 🔧 변경 | `GEMINI.md` | 0번 섹션(작업 시작 전 최우선 점검 — `.gitignore`) 및 "코드 수록 및 설명 원칙" 신설 |
| 🔧 변경 | `ai-Library/.gitignore` | `upload/`(런타임 업로드 이미지 폴더) 무시 규칙 추가 — 기존에 무시 목록에 없어 커밋 대상에 잡힐 뻔한 상태였음 |

> ⚠️ 오늘 소스에서 발견된 이슈(이미지 삭제 조건 오류, JSP 태그 닫힘 누락, 헤더-컨트롤러 링크 불일치 등)는 [`daily_practice/260922_mon/2026-09-22.md`](./daily_practice/260922_mon/2026-09-22.md)의 "발견된 이슈" 표에 정리되어 있음. 코드 수정은 진행하지 않았으며, 다음 실습 시 확인 필요.

---

### 📅 2026-09-22 (월) — ai-Library 추가 및 문서 정비

- **실습 주제**: MySQL 연동, DAO 패턴, JSTL, Bootstrap UI 적용

| 구분 | 대상 경로 | 세부 내용 |
| :---: | :--- | :--- |
| ➕ 추가 | `ai-Library/` | Spring Boot + MySQL JDBC 연동 도서관 프로젝트 신규 생성 |
| ➕ 추가 | `ai-Library/src/main/java/com/aitech/library/` | `AiLibraryApplication`, `HomeController`, `DBTestController`, `ServletInitializer` |
| ➕ 추가 | `ai-Library/.../book/` | `BookController`, `BookDao`, `BookRowMapper`, `BookVo` (DAO + VO 패턴) |
| ➕ 추가 | `ai-Library/.../config/DBconfig.java` | `@PropertySource("classpath:db.properties")` 기반 DataSource·JdbcTemplate 빈 설정 |
| ➕ 추가 | `ai-Library/.../views/` | `home.jsp`, `register_book.jsp`, `include/header·footer.jsp`, `book/book_list.jsp`, `user/login·register·modify·find.jsp`, `admin/management_book.jsp` |
| 🔧 변경 | `GEMINI.md` | Spring_2026 실습 환경 맞춤형 AI 행동 지침으로 전면 재작성 |
| ➕ 추가 | `daily_practice/260901_tue/2026-09-01.md` | 2026-09-01 Spring MVC 기초 실습 정리 문서 생성 |
| ➕ 추가 | `daily_practice/260922_mon/` | 당일 실습 코드 아카이빙(ai-Library) 및 `2026-09-22.md` 학습 정리 문서 생성 |
| 🔧 변경 | `DirectoryStructure.md` | ai-Library 및 daily_practice 아카이브 구조 반영, 전체 트리 갱신 |
| 🔧 변경 | `README.md` | ai-Library 및 2026-09-01/2026-09-22 실습 문서 바로가기 링크 추가 |

---

### 📅 2026-09-01 (화) — 초기 구성

- **실습 주제**: Spring Boot 4.x 기반 웹 애플리케이션 시작 및 Spring MVC 기초 (Controller, Model, JSP)

| 구분 | 대상 경로 | 세부 내용 |
| :---: | :--- | :--- |
| ➕ 추가 | `.gitignore` | STS/Eclipse/Maven 빌드, IDE 메타데이터, 서버 로그 및 패키지 아카이브 무시 규칙 추가 |
| ➕ 추가 | `GEMINI.md` | Spring Boot 실습 아카이빙 및 에이전트 행동 지침 문서화 |
| ➕ 추가 | `0901WebTest/` | Controller 어노테이션(`@Controller`, `@RequestMapping`, `@RequestParam`), `Model` 객체 및 JSP View 연결 실습 |
| ➕ 추가 | `MiniBookMarket/` | 도서 소개 및 추천 도서, 신간 소개, 리뷰 평점 파라미터 처리 실습 |
| ➕ 추가 | `daily_practice/260901_tue/` | 당일 실습 코드 아카이빙 (JSP 뷰 파일 보관) |
| ➕ 추가 | `DirectoryStructure.md` | 디렉토리 구조 및 변경 이력 문서 신규 생성 |
| ➕ 추가 | `README.md` | 워크스페이스 개요 및 바로가기 문서 신규 생성 |
