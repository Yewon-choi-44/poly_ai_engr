# 📚 Spring_2026 수업 및 실습 저장소

Spring Boot 4.x 및 Java 웹 개발 수업의 실습 코드와 일별 학습 정리를 관리하는 저장소입니다.

---

## 🚀 빠른 바로가기

- 📋 [AI 행동 지침 (GEMINI.md)](./GEMINI.md)
- 📁 [디렉토리 구조 및 변경 이력 (DirectoryStructure.md)](./DirectoryStructure.md)
- 🚫 [Git 추적 제외 설정 (.gitignore)](./.gitignore)

---

## 🏗️ 프로젝트 목록

| 프로젝트 | 설명 | 포트 |
| :--- | :--- | :---: |
| [0901WebTest](./0901WebTest/) | Spring MVC 기초 — Controller, Model, JSP View Resolver | 8090 |
| [MiniBookMarket](./MiniBookMarket/) | 미니 도서 마켓 — 파라미터 처리, JSP 뷰 | 8017 |
| [ai-Library](./ai-Library/) | AITECH 도서관 — MySQL JDBC 연동, DAO 패턴, Bootstrap UI | 8090 |

---

## 📅 일별 실습 아카이브 (`daily_practice/`)

| 일자 | 요일 | 주요 프로젝트 | 핵심 학습 내용 | 상세 문서 |
| :---: | :---: | :--- | :--- | :---: |
| **2026-09-22** | 월 | `ai-Library` | - Spring Boot + MySQL JDBC 연동 (`DataSource`, `Connection`, `PreparedStatement`)<br>- DAO 패턴 및 VO 객체 매핑 (`BookDao`, `BookVo`, `BookRowMapper`)<br>- JSTL (`c:forEach`) 도서 목록 렌더링 및 Bootstrap 5 카드 UI<br>- 공통 레이아웃 분리 (`header.jsp`, `footer.jsp`) 및 회원 관리 폼 | [2026-09-22.md](./daily_practice/260922_mon/2026-09-22.md) |
| **2026-09-01** | 화 | `0901WebTest`<br>`MiniBookMarket` | - Spring Boot 웹 프로젝트 생성 및 Starter 의존성<br>- `@Controller`, `@RequestMapping`, `@RequestParam`<br>- `Model` 인터페이스를 통한 JSP 뷰 데이터 바인딩<br>- JSP View Resolver 및 `tomcat-embed-jasper` 연동 | [2026-09-01.md](./daily_practice/260901_tue/2026-09-01.md) |

---

## 🛠️ 개발 및 실행 환경

| 항목 | 내용 |
| :--- | :--- |
| Language / SDK | Java 17 |
| Framework | Spring Boot 4.1.1 (`spring-boot-starter-webmvc`) |
| Build Tool | Maven (WAR packaging) |
| View Engine | JSP (`tomcat-embed-jasper`) + JSTL (`jakarta.servlet.jsp.jstl`) |
| DB | MySQL (`mysql-connector-j`, `spring-boot-starter-jdbc`) |
| IDE | STS (Spring Tool Suite) / Eclipse |
