# 📚 Spring_2026 수업 및 실습 관리 지침

이 워크스페이스는 Spring Boot 4.x 기반 Java 웹 개발 수업의 실습 코드 및 프로젝트를 관리하는 공간입니다.
실습 정리 및 디렉토리 관리 요청 시 아래 원칙을 항상 준수합니다.

---

## 1. 프로젝트 구조 원칙

이 워크스페이스에는 현재 다음 프로젝트가 존재합니다.

| 폴더명 | 설명 | 포트 | 패키지 |
| :--- | :--- | :---: | :--- |
| `0901WebTest/` | Spring MVC 기초 실습 (Controller, Model, JSP) | 8090 | `com.example.demo` |
| `MiniBookMarket/` | 도서 마켓 웹 실습 (JSP 뷰, 파라미터 처리) | 8017 | `com.example.demo` |
| `ai-Library/` | AI 도서관 실습 (MySQL 연동, JDBC, DAO 패턴) | 8090 | `com.aitech.library` |

새 프로젝트가 추가될 때는 위 표에 반드시 항목을 추가합니다.

---

## 2. 일별 실습 아카이빙 원칙 (`daily_practice/`)

- 실습 코드는 `daily_practice/YYMMDD_요일/` (예: `daily_practice/260901_tue/`, `daily_practice/260915_tue/`) 폴더 아래에 날짜별로 보관합니다.
- 각 날짜 폴더에는 실습에 사용된 프로젝트 소스 코드(Java, JSP, properties 등)를 보관합니다.
- 날짜 폴더 안에 `2026-MM-DD.md` 형식의 학습 정리 문서를 작성합니다.

---

## 3. 실습 정리 마크다운 문서화 (`2026-MM-DD.md`)

각 날짜 폴더 내에 `2026-MM-DD.md` 문서를 작성하여 당일 실습 내용을 체계적으로 정리합니다.

**필수 포함 항목**:
1. **Controller 코드 및 URL 매핑**: `@Controller`, `@RequestMapping`, `@RequestParam` 사용 예시 및 동작 설명
2. **Model 및 View 연결 구조**: `Model` 인터페이스를 통한 데이터 바인딩, JSP View Resolver 경로 매핑
3. **DB 연동 코드** (해당하는 경우): DAO 패턴, `DataSource`, `JdbcTemplate`, `PreparedStatement` 사용법
4. **VO/도메인 클래스**: 필드 정의, getter/setter 구조
5. **설정 파일**: `application.properties`, `db.properties`, `DBconfig.java` 설정 내용
6. **JSP 뷰 파일**: 주요 JSP 페이지의 구조 및 EL/JSTL 사용 예시
7. **💡 핵심 문법 정리 표 (Key Takeaways)**: 당일 학습한 Spring MVC, JDBC, Java 주요 개념 요약

---

## 4. DB 연동 관련 주의사항

`ai-Library` 프로젝트는 MySQL과 연동합니다.

- DB 연결 정보(`db.url`, `db.username`, `db.password`)는 `db.properties` 파일에 관리합니다.
- `db.properties`는 민감 정보를 포함하므로 **절대 Git에 커밋하지 않습니다**.
- `DBconfig.java`는 `@PropertySource("classpath:db.properties")`를 사용하여 DB 설정을 주입합니다.
- `BookDao`는 `DataSource`를 직접 사용하는 순수 JDBC 방식으로 구현되어 있습니다.

---

## 5. 레이어드 아키텍처 원칙 (`ai-Library`)

`ai-Library` 프로젝트는 다음 레이어 구조를 따릅니다.

```
Controller  →  DAO  →  DB
     ↑              ↑
   Model(JSP)    DataSource
```

| 클래스 | 역할 | 어노테이션 |
| :--- | :--- | :--- |
| `HomeController` | 라우팅 및 화면 전환 | `@Controller` |
| `BookController` | 도서 목록 조회 및 Model 바인딩 | `@Controller` |
| `DBTestController` | DB 연결 테스트 (개발/디버그용) | `@Controller` |
| `BookDao` | DB 접근 및 SQL 실행 | `@Repository` |
| `BookVo` | 도서 데이터 전달 객체 (VO) | - |
| `DBconfig` | DataSource 및 JdbcTemplate 빈 설정 | `@Configuration` |

---

## 6. JSP 뷰 구조 원칙 (`ai-Library`)

JSP 뷰는 기능별로 분리된 디렉토리에 배치합니다.

```
WEB-INF/views/
├── home.jsp                    # 홈 화면
├── register_book.jsp           # 도서 등록
├── include/
│   ├── header.jsp              # 공통 헤더 (include 전용)
│   └── footer.jsp              # 공통 푸터 (include 전용)
├── book/
│   └── book_list.jsp           # 도서 목록 조회
├── user/
│   ├── login_member.jsp        # 회원 로그인
│   ├── register_member.jsp     # 회원 가입
│   ├── modify_member.jsp       # 회원 정보 수정
│   └── find_password.jsp       # 비밀번호 찾기
└── admin/
    └── management_book.jsp     # 관리자 도서 관리
```

- 공통 UI 요소(헤더/푸터)는 `include/` 아래에 두고 JSP `<%@ include %>` 또는 `<jsp:include>`로 재사용합니다.
- 기능이 늘어날수록 `user/`, `book/`, `admin/` 디렉토리를 기능 단위로 분리하는 원칙을 유지합니다.

---

## 7. 디렉토리 구조 및 변경 이력 관리 (`DirectoryStructure.md`)

- 새로운 실습, 폴더, 설정 파일이 추가될 때마다 `DirectoryStructure.md`의 `## 변경 이력 (Changelog)` 섹션 최상단에 새 날짜를 추가합니다.
- **필수 포함 내용**:
  - 변경사항 요약 표 (`➕ 추가`, `🔧 변경`, `🗑️ 삭제`)
  - 해당 시점의 전체 디렉토리 구조 트리 (설명 주석 포함)
  - 세부 설명 및 실습 내용

---

## 8. Git 및 저장소 관리

- `target/`, `.settings/`, `.classpath`, `.project`, `.metadata/` 등 IDE 및 빌드 아티팩트는 Git에 추적되지 않도록 루트 `.gitignore`를 준수합니다.
- **절대 커밋하지 않을 파일**: `db.properties` (DB 접속 정보), `*.log`, `*.war`, `*.jar`
- 루트 `README.md`의 바로가기 링크와 일별 실습 아카이브 표를 항상 최신 상태로 유지합니다.
- 권장 커밋 메시지:
  ```
  feat: add ai-Library BookController and BookDao
  docs: add 2026-09-01 practice summary
  chore: update DirectoryStructure.md and index
  fix: resolve DB connection issue in DBconfig
  ```

---

## 9. 개발 환경 기준

| 항목 | 내용 |
| :--- | :--- |
| Language / SDK | Java 17 |
| Framework | Spring Boot 4.1.1 (`spring-boot-starter-webmvc`) |
| Build Tool | Maven (WAR packaging) |
| View Engine | JSP (`tomcat-embed-jasper`) + JSTL (`jakarta.servlet.jsp.jstl`) |
| DB | MySQL (`mysql-connector-j`, `spring-boot-starter-jdbc`) |
| IDE | STS (Spring Tool Suite) / Eclipse |

---

## 10. AI 어시스턴트 행동 원칙

- **코드 수정 요청 시**: 기존 패키지 구조(`com.aitech.library` 등)와 레이어 아키텍처를 따른다.
- **새 기능 추가 시**: Controller → DAO → DB 흐름을 유지하며, 각 클래스의 책임을 분리한다.
- **실습 정리 요청 시**: `daily_practice/YYMMDD_요일/2026-MM-DD.md` 형식으로 정리하고, `DirectoryStructure.md`와 `README.md`를 함께 갱신한다.
- **DB 관련 코드 작성 시**: `db.properties`에 접속 정보를 외부화하는 원칙을 유지하며, 접속 정보를 직접 코드에 하드코딩하지 않는다.
- **JSP 뷰 생성 시**: 기능 단위 서브 디렉토리(`book/`, `user/`, `admin/`) 아래에 배치하고 공통 요소는 `include/`를 사용한다.
- **보안**: API 키, 비밀번호, DB 접속 정보를 포함한 민감 정보는 절대 Git에 커밋하지 않는다.
