# 📚 ServerProgramming 수업 및 실습 관리 지침

이 워크스페이스는 서버 프로그래밍 과목의 수업 자료 및 실습 코드를 관리하는 공간입니다.
실습 정리 및 디렉토리 관리 요청 시 아래 원칙을 항상 준수합니다.

---

## 0. 프로젝트 개요

- **교재**: 《쉽게 배우는 JSP 웹 프로그래밍(2판)》(송미영 저, 한빛아카데미)
- **실습 환경**: Eclipse IDE + Apache Tomcat 9.0 + JDK 21 + MySQL 8.0
- **핵심 실습 프로젝트**: `BookMarket` (도서 쇼핑몰) — 각 장 학습 내용을 누적 적용하여 완성
- **워크스페이스 루트**: `JSPLecture/` (Eclipse 워크스페이스)

---

## 1. 날짜별 실습 프로젝트 관리 원칙 (`JSPLecture/`)

- 실습 프로젝트 폴더는 `JSPLecture/JSP{MMDD}/` 형식으로 날짜별로 생성합니다.
  - 예: `JSPLecture/JSP0819/`, `JSPLecture/JSP0828/`, `JSPLecture/JSP0904/`
- 각 날짜별 프로젝트는 `src/main/webapp/` 아래에 실습 `.jsp` 파일 및 Java 소스를 배치합니다.
- `BookMarket/`은 수업 전체에서 누적으로 기능이 추가되는 메인 실습 프로젝트입니다.
  새로운 장의 내용이 추가될 때마다 해당 장에 맞는 파일을 `BookMarket/src/main/webapp/`에 추가합니다.

---

## 2. 실습 정리 마크다운 문서화

각 날짜 실습 후 아래 형식의 마크다운 문서를 작성합니다.

### 문서 위치
- 날짜별 실습 프로젝트 정리: `notes/YYYY-MM-DD.md` (예: `notes/2026-08-19.md`)
- BookMarket 프로젝트 정리: `notes/BookMarket.md` (별도 분리된 전용 문서로 누적 기록)
- 장별 개념 정리 또는 수업 노트: `notes/` 폴더 내에 주제별로 관리

### 날짜별 정리 문서 필수 포함 항목

1. **실습 파일 목록 및 전체 원본 코드**: 해당 날짜에 작성한 `.jsp`, `.java`, `.js` 파일 등의 요약본이 아닌 **전체 원본 코드(생략 없이 완전한 발췌)** 및 동작 원리 설명
2. **실행 환경 및 구조**:
   - 프로젝트명 및 Tomcat 배포 경로 (URL 매핑)
   - `web.xml`의 Servlet/Filter 매핑, `<jsp:include>` 모듈화 구조
3. **핵심 JSP/Java 태그 및 문법**:
   - 스크립트 태그(`<% %>`, `<%! %>`, `<%= %>`), 디렉티브 태그(`page`, `include`, `taglib`)
   - 액션 태그(`jsp:forward`, `jsp:include`, `jsp:useBean` 등)
   - 내장 객체(`request`, `response`, `session`, `out`, `application` 등)
4. **💡 핵심 문법 정리 표 (Key Takeaways)**: 당일 학습한 JSP/Servlet/Java 주요 개념 요약 표

> ⚠️ **원칙 준수 사항**:
> - 날짜별 정리 문서에 코드를 첨부할 때 축약이나 생략 없이 **전체 원본 코드를 발췌하여 첨부**합니다.
> - **BookMarket 프로젝트 관련 항목**은 날짜별 문서가 아닌 **`notes/BookMarket.md` 등 별도의 분리된 문서에 기록 및 관리**합니다.

---

## 3. 디렉토리 구조 및 변경 이력 누적 (`DirectoryStructure.md`)

- `JSPLecture/DirectoryStructure.md`에 변경사항을 날짜순(최신순) 누적 기록합니다.
- 새로운 실습 프로젝트(`JSPMMDD/`), 파일, 설정이 추가될 때마다 **변경 이력 섹션 최상단**에 새 항목을 추가합니다.
- **필수 포함 내용**:
  - 변경사항 요약 표 (`➕ 추가`, `🔧 변경`, `🗑️ 삭제`)
  - 해당 시점의 전체 디렉토리 구조 트리 (설명 주석 포함)
  - `.gitignore` 현황 (루트 기준)
  - 세부 설명 및 실습 내용

---

## 4. Eclipse 프로젝트 구조 이해

Eclipse 동적 웹 프로젝트의 표준 구조는 아래와 같습니다. 파일 생성·분류 시 이 구조를 기준으로 합니다.

```
JSP{MMDD}/                          ← Eclipse 동적 웹 프로젝트
├── .classpath                      ← 클래스패스 설정 (JRE 21, Tomcat 9.0)
├── .project                        ← Eclipse 프로젝트 설정
├── .gitignore                      ← 프로젝트별 gitignore
├── .settings/                      ← Eclipse IDE 설정 (gitignore 권장)
├── build/classes/                  ← 컴파일 결과물 (gitignore됨)
└── src/main/
    ├── java/                       ← Java 소스 (Servlet, JavaBeans 등)
    └── webapp/
        ├── *.jsp                   ← JSP 실습 파일
        ├── WEB-INF/
        │   ├── web.xml             ← 배포 서술자 (Servlet/Filter/Error 매핑)
        │   └── lib/                ← JAR 라이브러리 (gitignore 권장)
        └── META-INF/
            └── MANIFEST.MF
```

---

## 5. BookMarket 프로젝트 장별 진화 흐름

`BookMarket/`은 아래 순서로 기능이 누적됩니다. 코드 작성·검토 시 현재 진행된 장 수준의 구현 범위를 유지합니다.

| 장 | 추가 기능 |
|---|---|
| 1장 | 프로젝트 생성 및 초기 실행 |
| 2장 | 시작 페이지 (부트스트랩 CSS 적용) |
| 3장 | 한글 출력 + 페이지 모듈화 (머리글/바닥글) |
| 4장 | 도서 목록 표시 (JavaBeans 기반 Book 클래스) |
| 5장 | 도서 상세 정보 표시 (내장 객체 활용) |
| 6장 | 도서 등록 페이지 (폼 태그) |
| 7장 | 도서 이미지 등록 (파일 업로드) |
| 8장 | 유효성 검사 (자바스크립트) |
| 9장 | 다국어 처리 (JSTL fmt) |
| 10장 | 보안 처리 (로그인 인증) |
| 11장 | 예외 처리 페이지 |
| 12장 | 로그 기록 (필터) |
| 13장 | 장바구니 페이지 (세션) |
| 14장 | 주문 처리 페이지 (쿠키) |
| 15장 | 도서 관리 테이블 + MySQL 연동 |
| 16장 | 도서 CRUD (JDBC 연동, DB 기반 전환) |
| 17장 | 회원 가입·수정·탈퇴 (JSTL 활용) |
| 18장 | 게시판 (MVC 패턴 적용) |

---

## 6. Git 및 저장소 관리

- `build/`, `.metadata/`, `.settings/`, `Servers/`, `WEB-INF/lib/*.jar`, `*.class`, `*.log` 등 빌드 결과물 및 IDE 임시 파일이 Git에 추적되지 않도록 `.gitignore`를 항상 준수합니다.
- `tomcat-users.xml`에는 계정 정보가 포함될 수 있으므로 **절대 커밋하지 않습니다** (`Servers/` 전체를 gitignore).
- `JSPLecture/DirectoryStructure.md`의 구조 트리와 `.gitignore` 현황을 최신 상태로 유지합니다.
- MySQL 접속 정보(URL, 계정, 비밀번호)가 포함된 `.java` 또는 `.jsp` 파일은 커밋 전에 확인합니다.

---

## 7. 수업 노트 및 참고 자료 (`notes/`)

- `notes/server-programming-course-summary.md`: 전체 강의 내용의 장별 요약 (기준 문서, 수정 시 장별 구조 유지)
- `notes/BookMarket.md`: BookMarket 쇼핑몰 메인 프로젝트 누적 정리 문서 (날짜별 노트와 별도 관리)
- `notes/ppt_40006/`: 강의 슬라이드 (Ch00~Ch18)
- `notes/old_ppt/`: 이전 버전 슬라이드

> 새로운 장을 배울 때마다 `server-programming-course-summary.md`의 해당 장 내용을 보강하거나,
> 별도 날짜별 노트(`notes/YYYY-MM-DD.md`)에 실습 상세 내용을 기록합니다.
> BookMarket 관련 기능 및 코드는 `notes/BookMarket.md`에 별도로 분리하여 기록합니다.
