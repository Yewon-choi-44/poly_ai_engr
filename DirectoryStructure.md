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
│   ├── pom.xml                     # Maven 설정 (Spring MVC Starter, Tomcat Jasper 등)
│   └── src/
│       ├── main/
│       │   ├── java/com/example/demo/
│       │   │   ├── Application.java            # Spring Boot 진입점
│       │   │   ├── HelloController.java        # 기본 컨트롤러 (/hello, /about, /greet, /today)
│       │   │   └── ServletInitializer.java     # WAR 배포 초기화
│       │   ├── resources/
│       │   │   ├── application.properties      # 서버 포트(8090) 및 JSP 뷰 리졸버 설정
│       │   │   └── static/index.html           # 기본 정적 페이지
│       │   └── webapp/WEB-INF/views/           # JSP 뷰 파일 (hello, about, greet, today)
│       └── test/
│
├── MiniBookMarket/                 # [프로젝트 2] 미니 도서 마켓 프로젝트
│   ├── pom.xml                     # Maven 설정 (Spring MVC Starter, Tomcat Jasper 등)
│   └── src/
│       ├── main/
│       │   ├── java/com/example/demo/
│       │   │   ├── MiniBookMarketApplication.java # Spring Boot 진입점
│       │   │   ├── BookMarketController.java      # 도서 마켓 컨트롤러 (/intro, /book, /recent, /review)
│       │   │   └── ServletInitializer.java        # WAR 배포 초기화
│       │   ├── resources/
│       │   │   ├── application.properties         # 서버 포트(8017) 및 JSP 뷰 리졸버 설정
│       │   │   └── static/index.html              # 기본 정적 페이지
│       │   └── webapp/WEB-INF/views/              # JSP 뷰 파일 (intro, book, recent, review)
│       └── test/
│
└── daily_practice/                 # 📚 일별 실습 아카이빙 폴더
    └── 260901_tue/                 # [2026-09-01 화] 실습 아카이브
        ├── 2026-09-01.md           # 2026-09-01 실습 상세 정리 문서
        ├── 0901WebTest/            # 0901WebTest 소스 및 pom.xml 아카이브
        └── MiniBookMarket/         # MiniBookMarket 소스 및 pom.xml 아카이브
```

---

## 🕒 변경 이력 (Changelog)

### 📅 2026-09-01 (화)
- **실습 주제**: Spring Boot 4.x 기반 웹 애플리케이션 시작 및 Spring MVC 기초 (Controller, Model, JSP)

| 구분 | 대상 경로 | 세부 내용 |
| :---: | :--- | :--- |
| ➕ 추가 | `.gitignore` | STS/Eclipse/Maven 빌드, IDE 메타데이터, 서버 로그 및 패키지 아카이브 무시 규칙 추가 |
| ➕ 추가 | `GEMINI.md` | Spring Boot 실습 아카이빙 및 에이전트 행동 지침 문서화 |
| ➕ 추가 | `0901WebTest/` | Controller 어노테이션(`@Controller`, `@RequestMapping`, `@RequestParam`), `Model` 객체 및 JSP View 연결 실습 |
| ➕ 추가 | `MiniBookMarket/` | 도서 소개 및 추천 도서, 신간 소개, 리뷰 평점 파라미터 처리 실습 |
| ➕ 추가 | `daily_practice/260901_tue/` | 당일 실습 코드 아카이빙 및 `2026-09-01.md` 학습 정리 문서 생성 |
| ➕ 추가 | `DirectoryStructure.md` | 디렉토리 구조 및 변경 이력 문서 신규 생성 |
| ➕ 추가 | `README.md` | 워크스페이스 개요 및 바로가기 문서 신규 생성 |
