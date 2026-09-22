# 📁 Spring_2026 디렉토리 구조 및 변경 이력

본 문서는 `Spring_2026` 워크스페이스의 프로젝트 구조 및 일별 변경 내역을 관리하는 문서입니다.

---

## 📌 전체 디렉토리 구조

```text
Spring_2026/
├── .gitignore                      # Git 추적 제외 규칙 (.metadata, target, logs, .settings 등)
├── GEMINI.md                       # AI 어시스턴트 행동 지침 및 수업 실습 관리 원칙
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
│       │   │   └── application.properties      # 서버 포트(8090), JSP 뷰 리졸버 설정
│       │   └── webapp/WEB-INF/views/
│       │       ├── home.jsp                    # 홈 화면 (도서 목록으로 리다이렉트)
│       │       ├── register_book.jsp           # 도서 등록 폼
│       │       ├── include/
│       │       │   ├── header.jsp              # 공통 헤더 (Bootstrap 5.3.8, 네비게이션 바)
│       │       │   └── footer.jsp              # 공통 푸터 (Bootstrap JS 번들)
│       │       ├── book/
│       │       │   └── book_list.jsp           # 도서 목록 (JSTL c:forEach, Bootstrap 카드 UI)
│       │       ├── user/
│       │       │   ├── login_member.jsp        # 회원 로그인 폼
│       │       │   ├── register_member.jsp     # 회원 가입 폼
│       │       │   ├── modify_member.jsp       # 회원 정보 수정 폼
│       │       │   └── find_password.jsp       # 비밀번호 찾기 폼
│       │       └── admin/
│       │           └── management_book.jsp     # 관리자 도서 관리 페이지
│       └── test/
│           └── java/com/aitech/library/
│               └── AiLibraryApplicationTests.java
│
└── daily_practice/                 # 📚 일별 실습 아카이빙 폴더
    └── 260901_tue/                 # [2026-09-01 화] 실습 아카이브
        ├── 2026-09-01.md           # 2026-09-01 실습 상세 정리 문서
        ├── 0901WebTest/            # 0901WebTest JSP 뷰 아카이브 (hello, about, greet, today)
        └── MiniBookMarket/         # MiniBookMarket 소스 아카이브
```

---

## 🕒 변경 이력 (Changelog)

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
| 🔧 변경 | `DirectoryStructure.md` | ai-Library 프로젝트 구조 반영, 전체 트리 갱신 |
| 🔧 변경 | `README.md` | ai-Library 및 2026-09-01 실습 문서 바로가기 링크 추가 |

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
