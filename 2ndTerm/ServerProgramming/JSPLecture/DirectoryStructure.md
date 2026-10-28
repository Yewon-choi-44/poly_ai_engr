# 📁 JSPLecture 디렉토리 구조 기록

> Eclipse IDE 기반 JSP/Servlet 웹 프로젝트 워크스페이스
> 변경사항이 생길 때마다 날짜별로 기록합니다.

---

## 변경 이력 (Changelog)

<!-- 새 항목은 맨 위에 추가하세요 (최신순) -->

---

## 🗓️ 2026-10-27

> 2026-09-22 이후 진행된 실습 4회차(10-08, 10-12, 10-19 + BookMarket 10장)가 구조 문서에 반영되지 않은 채 쌓여 있어 한꺼번에 정리했습니다. 코드는 수정하지 않았습니다.

### 변경사항 요약
| 구분 | 내용 |
|------|------|
| ➕ 추가 | `JSP1008/` 프로젝트 — [10-08] 시큐리티(10장) 실습: `web.xml` 선언적 보안 + FORM 인증 (`login.jsp`, `login_failed.jsp`, `security01.jsp`, `security02.jsp`) |
| ➕ 추가 | `JSP1012/` 프로젝트 — [10-12] 예외 처리(11장) 실습: errorPage / isErrorPage / exception 객체 / 오류 코드 / 예외 유형 / try-catch (JSP 16개) |
| ➕ 추가 | `JSPSource/` 프로젝트 — [10-12] 교재 2~18장 전체 예제 소스 (JSP 167개, Java 8개, properties 2개, SQL 8개, `web.xml` 변형 3개) |
| ➕ 추가 | `EXAM1019/` 프로젝트 — [10-19] 8·10·12장 종합 평가 프로젝트 (로그인 폼 검증 + 보안 설정 + `com.filter.LoginYewonChoi` 필터) |
| ➕ 추가 | `BookMarket/src/main/webapp/WEB-INF/web.xml` — [10-08] 10장: `admin` 역할로 `/addBook.jsp` 보호, FORM 인증 |
| ➕ 추가 | `BookMarket/src/main/webapp/login.jsp` / `login_failed.jsp` / `logout.jsp` — [10-08] 10장 관리자 로그인·실패 리다이렉트·로그아웃 |
| 🔧 변경 | `BookMarket/src/main/webapp/addBook.jsp` — [10-08] Korean/English 언어 링크(9장 일부) + 로그아웃 버튼(10장) 추가 |
| ➕ 추가 | `JSP1008/.gitignore`, `JSP1012/.gitignore`, `JSPSource/.gitignore`, `EXAM1019/.gitignore` — 다른 프로젝트와 동일한 표준 패턴으로 신규 생성 (이전까지 누락) |
| 🔧 변경 | 루트 `.gitignore` 주석 — 추적 대상 프로젝트 목록에 `JSP1008`, `JSP1012`, `JSPSource`, `EXAM1019` 추가 |
| ➕ 추가 | `../notes/2026-10-08.md`, `../notes/2026-10-12.md`, `../notes/2026-10-19.md` — 날짜별 실습 정리 노트 (전체 원본 코드 + 동작 원리 + 이슈) |
| 🔧 변경 | `../notes/BookMarket.md` — 9장(진행 중)·10장(완료) 현황, 디렉토리 구조, `addBook.jsp` 최신 코드, 신규 4개 파일 전체 코드, 발견된 이슈 갱신 |
| ➕ 추가 | `../README.md` — ServerProgramming 루트 개요 문서 신규 작성 (기존에 없었음) |

> ⚠️ 주요 확인 필요 사항(코드는 수정하지 않음):
> - `JSP1012/WEB-INF/web.xml`에 `<error-page>` 매핑이 없어 오류 코드/예외 유형 실습의 오류 페이지가 동작하지 않음 → [`notes/2026-10-12.md`](../notes/2026-10-12.md) 4번
> - `EXAM1019/WEB-INF/web.xml`의 `/2/…`, `/4/…` 경로와 실제 파일 위치(webapp 루트)가 일치하지 않음, `loginForm.jsp` 폼 이름 불일치 → [`notes/2026-10-19.md`](../notes/2026-10-19.md) 4번
> - `JSPSource/ch16`, `ch17`에 교재 기본 MySQL 접속 정보(`root` 계정)가 하드코딩되어 있음 — 실제 비밀번호로 바꿔 쓰게 되면 커밋 전 확인
> - `Servers/.../tomcat-users.xml`에 `admin` 사용자명이 중복 정의됨 → [`notes/2026-10-08.md`](../notes/2026-10-08.md) 4번

### 현재 디렉토리 구조

```
JSPLecture/                                  ← Eclipse 워크스페이스 루트
│
├── .gitignore                               ← ✅ 추적 대상 주석에 신규 4개 프로젝트 추가
├── .project                                 ← 워크스페이스 메타 파일
├── DirectoryStructure.md                    ← 📄 이 파일
│
├── .metadata/                               ← Eclipse 런타임 데이터 (gitignore됨)
│
├── JSP0819/                                 ← 1~2장 실습 프로젝트
├── JSP0828/                                 ← 3~4장 실습 프로젝트 (액션 태그 & JavaBeans)
├── JSP0904/                                 ← 5장 실습 프로젝트 (JSP 내장 객체)
├── JSP0911/                                 ← 7장 실습 프로젝트 (파일 업로드)
├── JSP0918/                                 ← 8장 실습 프로젝트 (유효성 검사)
│   (위 5개 프로젝트는 이전 항목에서 구조 변경 없음 — 하단 과거 이력 참고)
│
├── JSP1008/                                 ← 🆕 10장 실습 프로젝트 (시큐리티)
│   ├── .classpath / .project / .gitignore   ← ✅ 오늘 .gitignore 신규 생성 (표준 패턴)
│   ├── .settings/ · build/                  ← gitignore됨
│   └── src/main/
│       ├── java/                            ← (비어 있음)
│       └── webapp/
│           ├── login.jsp                    ← FORM 인증 폼 (j_security_check)
│           ├── login_failed.jsp             ← 인증 실패 페이지
│           ├── security01.jsp               ← 인증 성공 안내 (보호 대상 아님)
│           ├── security02.jsp               ← 🔒 role1 전용 — getRemoteUser/getAuthType/isUserInRole 출력
│           ├── META-INF/MANIFEST.MF
│           └── WEB-INF/web.xml              ← security-role(role1) + security-constraint + login-config(FORM)
│
├── JSP1012/                                 ← 🆕 11장 실습 프로젝트 (예외 처리)
│   ├── .classpath / .project / .gitignore   ← ✅ 오늘 .gitignore 신규 생성
│   ├── .settings/ · build/                  ← gitignore됨
│   └── src/main/
│       ├── java/                            ← (비어 있음)
│       └── webapp/
│           ├── errorPage.jsp / errorPage_error.jsp                          ← ① errorPage 속성
│           ├── isErrorPage.jsp / isErrorPage_error.jsp                      ← ② isErrorPage + exception 객체
│           ├── exception.jsp / exception_process.jsp / exception_error.jsp  ← ③ exception 메서드 4종
│           ├── errorCode.jsp / errorCode_process.jsp / errorCode_error.jsp  ← ④ web.xml 오류 코드용
│           ├── exceptionType.jsp / exceptionType_process.jsp / exceptionType_error.jsp ← ⑤ web.xml 예외 유형용
│           ├── tryCatch.jsp / tryCatch_process.jsp / tryCatch_error.jsp     ← ⑥ try-catch + forward
│           ├── META-INF/MANIFEST.MF
│           └── WEB-INF/web.xml              ← ⚠️ 10장 보안 설정 복사본 (error-page 매핑 없음)
│
├── JSPSource/                               ← 🆕 교재 2~18장 예제 소스 (참고용)
│   ├── .classpath / .project / .gitignore   ← ✅ 오늘 .gitignore 신규 생성
│   ├── .settings/ · build/                  ← gitignore됨
│   └── src/main/
│       ├── java/
│       │   ├── ch04/com/dao/                ← Calculator.java, Person.java
│       │   ├── ch09/com/bundle/             ← myBundle.properties, myBundle_en.properties
│       │   ├── ch12/com/filter/             ← AuthenFilter, InitParamFilter, LogFileFilter
│       │   └── ch18/com/{controller,model}/ ← ControllerServlet, LoginController, LoginBean
│       └── webapp/
│           ├── hello.jsp
│           ├── ch02/ ~ ch18/                ← 장별 예제 JSP/SQL (ch02:9, ch03:17, ch04:17, ch05:16, ch06:12, ch07:10,
│           │                                   ch08:10, ch09:5, ch10:4, ch11:16, ch12:4, ch13:9, ch14:4, ch15:6,
│           │                                   ch16:17, ch17:15, ch18:3)
│           ├── META-INF/MANIFEST.MF
│           └── WEB-INF/
│               ├── web.xml                  ← /ch10/security02.jsp FORM 인증
│               ├── ch10_web_BASIC.xml / ch10_web_FORM.xml / ch10)web_FORME_02.xml ← 10장 설정 예시
│               └── lib/*.jar                ← cos, commons-fileupload/io, jstl, mysql-connector (gitignore됨)
│
├── EXAM1019/                                ← 🆕 8·10·12장 종합 평가 프로젝트
│   ├── .classpath / .project / .gitignore   ← ✅ 오늘 .gitignore 신규 생성
│   ├── .settings/ · build/                  ← gitignore됨
│   └── src/main/
│       ├── java/com/filter/
│       │   └── LoginYewonChoi.java          ← name 파라미터 검사 Filter (init/doFilter/destroy)
│       └── webapp/
│           ├── 1/ 2/ 3/ 4/                  ← 문항별 폴더 (비어 있음)
│           ├── loginForm.jsp                ← 비밀번호 8~12자 길이 검사 폼
│           ├── loginForm_process.jsp        ← id/pw 출력
│           ├── login.jsp                    ← 로그인 폼
│           ├── login_success.jsp            ← 로그인 성공 + 로그아웃 링크
│           ├── login_failed.jsp             ← 로그인 실패
│           ├── success.jsp                  ← 필터 적용 대상 페이지
│           ├── META-INF/MANIFEST.MF
│           └── WEB-INF/web.xml              ← admin 보안 + FORM 인증(/4/…) + logFilter 매핑(/4/success.jsp)
│
├── BookMarket/                              ← 📚 누적 메인 프로젝트 (현재: 10장 반영, 9장 일부)
│   ├── .classpath / .project / .gitignore
│   ├── .settings/ · build/                  ← gitignore됨
│   └── src/main/
│       ├── java/
│       │   ├── dto/Book.java                ← ✅ [4장] 도서 DTO
│       │   └── dao/BookRepository.java      ← ✅ [4장] 도서 목록 저장소
│       └── webapp/
│           ├── Welcome0819.jsp              ← ✅ [2장] Bootstrap 시작 페이지
│           ├── welcome.jsp                  ← ✅ [3장] 모듈화
│           ├── menu.jsp / footer.jsp        ← ✅ [3장] 헤더/푸터 부품
│           ├── books.jsp                    ← ✅ [4장] 도서 목록 페이지
│           ├── book.jsp                     ← ✅ [5장] 도서 상세 정보 페이지
│           ├── addBook.jsp                  ← 🔧 [6~10장] 도서 등록 폼 — 언어 링크 + 로그아웃 버튼 추가, 🔒 admin 전용
│           ├── processAddBook.jsp           ← ✅ [7장] 등록 처리
│           ├── login.jsp                    ← 🆕 [10장] 관리자 FORM 로그인 (Bootstrap floating label)
│           ├── login_failed.jsp             ← 🆕 [10장] login.jsp?error=1 리다이렉트
│           ├── logout.jsp                   ← 🆕 [10장] session.invalidate() → addBook.jsp
│           ├── META-INF/
│           ├── WEB-INF/
│           │   ├── web.xml                  ← 🆕 [10장] admin 역할 + /addBook.jsp 보호 + FORM 인증
│           │   └── lib/                     ← cos.jar 등 (gitignore됨)
│           └── resources/
│               ├── css/bootstrap.min.css
│               ├── js/validation.js         ← [8장] 도서 등록 폼 클라이언트 검증
│               └── images/                  ← seed 이미지 3장 + 업로드 테스트 이미지 + Thumbs.db(gitignore됨)
│
└── Servers/                                 ← Tomcat 로컬 설정 (gitignore됨)
    └── Tomcat v9.0 Server at localhost-config/
        └── tomcat-users.xml                 ← ⚠️ 계정 정보 포함 (role1, tomcat, admin 역할 정의)
```

### .gitignore 현황 (루트)
```gitignore
# Eclipse 워크스페이스 메타데이터
.metadata/

# 컴파일 결과물 (모든 하위 프로젝트 포함)
build/
**/build/

# Eclipse IDE 설정
.settings/
**/.settings/

# JAR 라이브러리 (모든 하위 경로)
**/WEB-INF/lib/*.jar

# Tomcat 서버 설정 (계정 정보 포함 가능)
Servers/

# 컴파일된 클래스 파일
*.class

# 로그 파일
*.log

# 실습 완료 프로젝트 - 모두 정상 추적 중
# JSP0819, JSP0828, JSP0904, JSP0911, JSP0918, JSP1008, JSP1012, JSPSource, EXAM1019, BookMarket 추적 대상
```

### 신규 프로젝트 개별 `.gitignore` (`JSP1008`, `JSP1012`, `JSPSource`, `EXAM1019` 공통)
```gitignore
# Eclipse 빌드 결과물 및 IDE 설정
/build/
/.settings/
/src/main/webapp/WEB-INF/lib/*.jar
*.class
*.log
```

> 점검 결과: 신규 4개 프로젝트가 통째로 무시되는 규칙은 없으며(0번 원칙), `git status`상 `JSPSource/WEB-INF/lib/*.jar`, `build/`, `.settings/`는 추적 목록에 나타나지 않음을 확인했습니다.

---

## 🗓️ 2026-09-22 (오후 18:49)

### 변경사항 요약
| 구분 | 내용 |
|------|------|
| ➕ 추가 | `JSP0918/` 프로젝트 — 유효성 검사(JavaScript Validation) 실습 (8장) |
| ➕ 추가 | `JSP0918/src/main/webapp/` — 9개 JSP 파일 (validation01~05 + 02~05 process) |
| ➕ 추가 | `JSP0918/.gitignore` — 다른 프로젝트와 동일한 표준 패턴으로 신규 생성 (이전까지 누락 상태였음) |
| 🔧 변경 | `BookMarket/src/main/webapp/` — 정적 리소스 경로를 `css/`, `images/` → `resources/{css,images,js}/`로 재구성 |
| ➕ 추가 | `BookMarket/src/main/webapp/resources/js/validation.js` — 도서 등록 폼(`addBook.jsp`) 클라이언트 사이드 유효성 검사 (8장 부분 반영) |
| 🔧 변경 | `BookMarket/src/main/webapp/addBook.jsp` — CSS/JS 경로 변경, 필드 `id` 속성 추가, 제출 버튼을 `submit` → `button`+`onclick="CheckAddBook()"`으로 전환 |
| 🔧 변경 | `BookMarket/src/main/webapp/processAddBook.jsp` — 이미지 저장 경로를 `webapp/images` → `webapp/resources/images`로 변경, 파라미터명 `unitsInStock` → `unitInStock`으로 수정 |
| ➕ 추가 | `notes/2026-09-18.md` — JSP0918 실습 정리 노트 (8장: 유효성 검사, 전체 원본 코드 + 동작 원리 + 발견된 이슈) |
| 🔧 변경 | `notes/BookMarket.md` — 8장(유효성 검사) 진행 현황 반영, 전체 코드 갱신, 마크다운 코드펜스 오류(단일 백틱) 및 표 안 오탈자(`ddBook.jsp` 등) 정정, 발견된 이슈 섹션 신설 |
| 🔧 변경 | 루트 `.gitignore` 주석 — 추적 대상 프로젝트 목록에 `JSP0918` 추가 |

> ⚠️ 이번 실습에서 클라이언트 검증 스크립트(`validation.js`)와 `processAddBook.jsp`의 파라미터 처리에서 버그 여러 건이 발견되었습니다. 상세 내용은 [`notes/BookMarket.md`](../notes/BookMarket.md)의 "발견된 이슈" 섹션과 [`notes/2026-09-18.md`](../notes/2026-09-18.md)의 동일 섹션 참고. 코드 수정은 진행하지 않았으며 다음 실습 시 확인 필요.

### 현재 디렉토리 구조

```
JSPLecture/                                  ← Eclipse 워크스페이스 루트
│
├── .gitignore                               ← ✅ JSP0918 추적 대상 주석 추가
├── .project                                 ← 워크스페이스 메타 파일
├── DirectoryStructure.md                    ← 📄 이 파일
│
├── .metadata/                               ← Eclipse 런타임 데이터 (gitignore됨)
│
├── JSP0819/                                 ← 1~2장 실습 프로젝트
├── JSP0828/                                 ← 3~4장 실습 프로젝트 (액션 태그 & JavaBeans)
├── JSP0904/                                 ← 5장 실습 프로젝트 (JSP 내장 객체)
├── JSP0911/                                 ← 7장 실습 프로젝트 (파일 업로드)
│   (위 4개 프로젝트는 이전 항목에서 구조 변경 없음 — 하단 과거 이력 참고)
│
├── JSP0918/                                 ← 🆕 8장 실습 프로젝트 (유효성 검사)
│   ├── .classpath / .project / .gitignore   ← ✅ 오늘 .gitignore 신규 생성 (표준 패턴)
│   ├── .settings/                           ← gitignore됨
│   ├── build/classes/                       ← gitignore됨
│   └── src/main/
│       ├── java/                            ← Java 소스 (비어있음)
│       └── webapp/
│           ├── validation01.jsp             ← ✅ 검증 없음 — alert로 값 확인만
│           ├── validation02.jsp             ← ✅ 빈 값(공백) 체크
│           ├── validation02_process.jsp     ← ✅ 02 제출 처리
│           ├── validation03.jsp             ← ✅ 길이(자릿수) 체크
│           ├── validation03_process.jsp     ← ✅ 03 제출 처리
│           ├── validation04.jsp             ← ✅ 문자 종류(영문/숫자) 체크
│           ├── validation04_process.jsp     ← ✅ 04 제출 처리
│           ├── validation05.jsp             ← ✅ 정규식 기반 회원가입 종합 검증
│           ├── validation05_process.jsp     ← ✅ 05 제출 처리 (전체 필드 출력)
│           └── META-INF/MANIFEST.MF
│
├── BookMarket/                              ← 📚 누적 메인 프로젝트 (현재: 8장 부분 반영)
│   ├── .classpath / .project / .gitignore
│   ├── .settings/                           ← gitignore됨
│   ├── build/classes/                       ← gitignore됨
│   └── src/main/
│       ├── java/
│       │   ├── dto/Book.java                ← ✅ [4장] 도서 DTO
│       │   └── dao/BookRepository.java      ← ✅ [4장] 도서 목록 저장소
│       └── webapp/
│           ├── Welcome0819.jsp              ← ✅ [2장] Bootstrap 시작 페이지
│           ├── welcome.jsp                  ← ✅ [3장] 모듈화
│           ├── menu.jsp / footer.jsp        ← ✅ [3장] 헤더/푸터 부품
│           ├── books.jsp                    ← ✅ [4장] 도서 목록 페이지
│           ├── book.jsp                     ← ✅ [5장] 도서 상세 정보 페이지
│           ├── addBook.jsp                  ← 🔧 [6/7/8장] 도서 등록 폼 — 리소스 경로 변경 + 클라이언트 검증 연동
│           ├── processAddBook.jsp           ← 🔧 [7장] 등록 처리 — 이미지 경로/파라미터명 수정
│           ├── META-INF/
│           └── resources/                   ← 🆕 정적 리소스 통합 폴더 (기존 css/, images/ 대체)
│               ├── css/
│               │   └── bootstrap.min.css
│               ├── js/
│               │   └── validation.js        ← 🆕 [8장] 도서 등록 폼 클라이언트 검증
│               └── images/
│                   ├── ISBN1234.jpg / ISBN1235.jpg / ISBN1236.jpg  ← seed 이미지
│                   ├── ISBN12341234.png     ← 🆕 실습 중 업로드 테스트 이미지
│                   └── Thumbs.db            ← Windows 캐시 (gitignore됨)
│
└── Servers/                                 ← Tomcat 로컬 설정 (gitignore됨)
    └── Tomcat v9.0 Server at localhost-config/
        └── tomcat-users.xml                 ← ⚠️ 계정 정보 포함 가능
```

### .gitignore 현황 (루트)
```gitignore
# Eclipse 워크스페이스 메타데이터
.metadata/

# 컴파일 결과물 (모든 하위 프로젝트 포함)
build/
**/build/

# Eclipse IDE 설정
.settings/
**/.settings/

# JAR 라이브러리 (모든 하위 경로)
**/WEB-INF/lib/*.jar

# Tomcat 서버 설정 (계정 정보 포함 가능)
Servers/

# 컴파일된 클래스 파일
*.class

# 로그 파일
*.log

# 실습 완료 프로젝트 - 모두 정상 추적 중
# JSP0819, JSP0828, JSP0904, JSP0911, JSP0918, BookMarket 추적 대상
```

### JSP0918 개별 `.gitignore` (신규)
```gitignore
# Eclipse 빌드 결과물 및 IDE 설정
/build/
/.settings/
/src/main/webapp/WEB-INF/lib/*.jar
*.class
*.log
```

---

## 🗓️ 2026-09-11 (오후 20:50)

### 변경사항 요약
| 구분 | 내용 |
|------|------|
| 🔧 변경 | `BookMarket/.gitignore` — OS 임시 생성 파일(`Thumbs.db` 등) 포함 최신화 |
| ➕ 추가 | `notes/BookMarket.md` — BookMarket 메인 프로젝트 전용 분리 누적 정리 문서 신규 작성 |
| 📄 문서화 | BookMarket 전체 Java DTO/DAO 및 JSP 모듈 코드 전체 원본 발췌 명시 |

---

## 🗓️ 2026-09-11 (오후 20:40)

### 변경사항 요약
| 구분 | 내용 |
|------|------|
| 🔧 변경 | 각 하위 프로젝트(`BookMarket/`, `JSP0819/`, `JSP0828/`, `JSP0904/`, `JSP0911/`)마다 개별 `.gitignore` 생성 및 전수 정비 |
| 🔧 변경 | 루트 `.gitignore` — `**/build/`, `**/.settings/` 등 하위 디렉토리 재귀 패턴 강화 |
| 🔍 검토 | 전체 워크스페이스 및 `notes/` 실습 정리 문서 (`2026-08-19.md`, `2026-08-28.md`, `2026-09-04.md`, `2026-09-11.md`) 검토 완료 |

### 현재 디렉토리 구조

```
JSPLecture/                                  ← Eclipse 워크스페이스 루트
│
├── .gitignore                               ← ✅ 루트 재귀 패턴 보강 (build, .settings, jar 등)
├── .project                                 ← 워크스페이스 메타 파일
├── DirectoryStructure.md                    ← 📄 이 파일
│
├── .metadata/                               ← Eclipse 런타임 데이터 (gitignore됨)
│
├── JSP0819/                                 ← 1~2장 실습 프로젝트
│   ├── .classpath / .project / .gitignore   ← ✅ 프로젝트별 .gitignore 적용
│   ├── .settings/                           ← Eclipse IDE 설정 (gitignore됨)
│   ├── build/classes/                       ← 컴파일 결과물 (gitignore됨)
│   └── src/main/
│       ├── java/                            ← Java 소스 (비어있음)
│       └── webapp/
│           ├── Hello0819.jsp                ← ✅ 첫 번째 JSP 실습
│           ├── Welcome.jsp                  ← ✅ 쇼핑몰 환영 페이지
│           ├── META-INF/MANIFEST.MF
│           └── WEB-INF/lib/
│
├── JSP0828/                                 ← 3~4장 실습 프로젝트 (액션 태그 & JavaBeans)
│   ├── .classpath / .project / .gitignore   ← ✅ 프로젝트별 .gitignore 생성
│   ├── .settings/                           ← gitignore됨
│   ├── build/classes/                       ← gitignore됨
│   └── src/main/
│       ├── java/dao/
│       │   ├── Calculator.java              ← ✅ JavaBean — 세제곱 계산
│       │   └── Person.java                  ← ✅ JavaBean — id/name 프로퍼티
│       └── webapp/
│           ├── first.jsp / second.jsp       ← ✅ jsp:forward 실습
│           ├── firstInclude.jsp / secondInclude.jsp ← ✅ jsp:include 실습
│           ├── include.jsp / include_date.jsp
│           ├── param01.jsp / param01_data.jsp
│           ├── useBean01~04.jsp             ← ✅ jsp:useBean 실습
│           ├── setProperty.jsp / getProperty01~02.jsp
│           ├── META-INF/MANIFEST.MF
│           └── WEB-INF/lib/
│
├── JSP0904/                                 ← 5장 실습 프로젝트 (JSP 내장 객체)
│   ├── .classpath / .project / .gitignore   ← ✅ 프로젝트별 .gitignore 생성
│   ├── .settings/                           ← gitignore됨
│   ├── build/classes/                       ← gitignore됨
│   └── src/main/
│       ├── java/                            ← Java 소스 (비어있음)
│       └── webapp/
│           ├── form01.jsp ~ form06.jsp       ← ✅ HTML 폼 태그 실습
│           ├── form04_process.jsp           ← ✅ getParameter() 개별 처리
│           ├── form05_process.jsp           ← ✅ getParameterValues() 배열 처리
│           ├── form06_process.jsp           ← ✅ getParameterNames() Enumeration 처리
│           ├── out01.jsp / out02.jsp / out02_process.jsp ← ✅ out 내장 객체
│           ├── request.jsp / process.jsp    ← ✅ request 기본 메서드
│           ├── request01.jsp / request01_process.jsp ← ✅ 로그인 폼 처리
│           ├── request02.jsp                ← ✅ 요청 헤더 전체 출력
│           ├── request03.jsp                ← ✅ request 상세 정보 출력
│           ├── index.jsp / index_process.jsp ← ✅ 체크박스 처리
│           ├── response.jsp                 ← ✅ sendRedirect (Google)
│           ├── response01.jsp / response01_process.jsp / response01_success.jsp / response01_failed.jsp ← ✅ 로그인 리다이렉트
│           ├── response02.jsp               ← ✅ setIntHeader("Refresh", 5)
│           ├── response03.jsp               ← ✅ sendError(404)
│           ├── META-INF/MANIFEST.MF
│           └── WEB-INF/lib/
│
├── JSP0911/                                 ← 7장 실습 프로젝트 (파일 업로드)
│   ├── .classpath / .project / .gitignore   ← ✅ 프로젝트별 .gitignore 생성
│   ├── .settings/                           ← gitignore됨
│   ├── build/classes/                       ← gitignore됨
│   └── src/main/
│       ├── java/                            ← Java 소스 (비어있음)
│       └── webapp/
│           ├── fileupload01.jsp             ← ✅ 단일 파일 업로드 폼 (cos.jar)
│           ├── fileupload01_process.jsp     ← ✅ MultipartRequest 처리 — 파라미터+파일 정보 출력
│           ├── fileupload02.jsp             ← ✅ 다중 파일(3개) 업로드 폼
│           ├── fileupload02_process.jsp     ← ✅ 3개 파일 처리 — 결과 테이블 출력
│           ├── fileupload03.jsp             ← ✅ 단일 파일 폼 (Commons FileUpload)
│           ├── fileupload03_process.jsp     ← ✅ DiskFileUpload + FileItem 처리
│           ├── fileupload04.jsp             ← ✅ 텍스트+파일 혼합 폼
│           ├── fileupload04_process.jsp     ← ✅ isFormField()로 폼/파일 분기 처리
│           ├── META-INF/MANIFEST.MF
│           └── WEB-INF/lib/                ← cos.jar, commons-fileupload.jar (gitignore됨)
│
├── BookMarket/                              ← 📚 누적 메인 프로젝트 (현재: 5장까지 완료)
│   ├── .classpath / .project / .gitignore   ← ✅ 프로젝트별 .gitignore 적용
│   ├── .settings/                           ← gitignore됨
│   ├── build/classes/                       ← gitignore됨
│   └── src/main/
│       ├── java/
│       │   ├── dto/Book.java                ← ✅ [4장] 도서 DTO
│       │   └── dao/BookRepository.java      ← ✅ [4장] 도서 목록 저장소
│       └── webapp/
│           ├── Welcome0819.jsp              ← ✅ [2장] Bootstrap 시작 페이지
│           ├── welcome.jsp                  ← ✅ [3장] 모듈화
│           ├── menu.jsp / footer.jsp        ← ✅ [3장] 헤더/푸터 부품
│           ├── books.jsp                    ← ✅ [4장] 도서 목록 페이지
│           ├── META-INF/
│           └── WEB-INF/lib/
│
└── Servers/                                 ← Tomcat 로컬 설정 (gitignore됨)
    └── Tomcat v9.0 Server at localhost-config/
        └── tomcat-users.xml                 ← ⚠️ 계정 정보 포함 가능
```

### .gitignore 현황 (루트)
```gitignore
# Eclipse 워크스페이스 메타데이터
.metadata/

# 컴파일 결과물 (모든 하위 프로젝트 포함)
build/
**/build/

# Eclipse IDE 설정
.settings/
**/.settings/

# JAR 라이브러리 (모든 하위 경로)
**/WEB-INF/lib/*.jar

# Tomcat 서버 설정 (계정 정보 포함 가능)
Servers/

# 컴파일된 클래스 파일
*.class

# 로그 파일
*.log

# 실습 완료 프로젝트 - 모두 정상 추적 중
# JSP0819, JSP0828, JSP0904, JSP0911, BookMarket 추적 대상
```

### 각 하위 프로젝트별 .gitignore 표준 구조
```gitignore
# Eclipse 빌드 결과물 및 IDE 설정
/build/
/.settings/
/src/main/webapp/WEB-INF/lib/*.jar
*.class
*.log
```

---

## 🗓️ 2026-09-11 (오후 14:47)

### 변경사항 요약
| 구분 | 내용 |
|------|------|
| ➕ 추가 | `JSP0911/` 프로젝트 — 파일 업로드 실습 (7장) |
| ➕ 추가 | `JSP0911/src/main/webapp/` — 8개 JSP 파일 (fileupload01~04 + process) |
| 🔧 변경 | 루트 `.gitignore` — `/JSP0904/` 임시 제외 해제, JSP0904·JSP0911 모두 추적 대상 |
| ➕ 추가 | `notes/2026-09-04.md` — JSP0904 실습 정리 노트 (5장: 내장 객체) |
| ➕ 추가 | `notes/2026-09-11.md` — JSP0911 실습 정리 노트 (7장: 파일 업로드) |

### 현재 디렉토리 구조

```
JSPLecture/                                  ← Eclipse 워크스페이스 루트
│
├── .gitignore                               ← ✅ /JSP0904/ 임시 제외 해제 (전 프로젝트 추적)
├── .project                                 ← 워크스페이스 메타 파일
├── DirectoryStructure.md                    ← 📄 이 파일
│
├── .metadata/                               ← Eclipse 런타임 데이터 (gitignore됨)
│
├── JSP0819/                                 ← 1~2장 실습 프로젝트
│   ├── .classpath / .project / .gitignore
│   ├── .settings/                           ← Eclipse IDE 설정 (gitignore됨)
│   ├── build/classes/                       ← 컴파일 결과물 (gitignore됨)
│   └── src/main/
│       ├── java/                            ← Java 소스 (비어있음)
│       └── webapp/
│           ├── Hello0819.jsp                ← ✅ 첫 번째 JSP 실습
│           ├── Welcome.jsp                  ← ✅ 쇼핑몰 환영 페이지
│           ├── META-INF/MANIFEST.MF
│           └── WEB-INF/lib/
│
├── JSP0828/                                 ← 3~4장 실습 프로젝트 (액션 태그 & JavaBeans)
│   ├── .classpath / .project
│   ├── .settings/                           ← gitignore됨
│   ├── build/classes/                       ← gitignore됨
│   └── src/main/
│       ├── java/dao/
│       │   ├── Calculator.java              ← ✅ JavaBean — 세제곱 계산
│       │   └── Person.java                  ← ✅ JavaBean — id/name 프로퍼티
│       └── webapp/
│           ├── first.jsp / second.jsp       ← ✅ jsp:forward 실습
│           ├── firstInclude.jsp / secondInclude.jsp ← ✅ jsp:include 실습
│           ├── include.jsp / include_date.jsp
│           ├── param01.jsp / param01_data.jsp
│           ├── useBean01~04.jsp             ← ✅ jsp:useBean 실습
│           ├── setProperty.jsp / getProperty01~02.jsp
│           ├── META-INF/MANIFEST.MF
│           └── WEB-INF/lib/
│
├── JSP0904/                                 ← ✅ 5장 실습 프로젝트 (JSP 내장 객체) — gitignore 해제
│   ├── .classpath / .project
│   ├── .settings/                           ← gitignore됨
│   ├── build/classes/                       ← gitignore됨
│   └── src/main/
│       ├── java/                            ← Java 소스 (비어있음)
│       └── webapp/
│           ├── form01.jsp ~ form06.jsp       ← ✅ HTML 폼 태그 실습 (text, password, radio, checkbox, select, textarea)
│           ├── form04_process.jsp           ← ✅ getParameter() 개별 처리
│           ├── form05_process.jsp           ← ✅ getParameterValues() 배열 처리
│           ├── form06_process.jsp           ← ✅ getParameterNames() Enumeration 처리
│           ├── out01.jsp / out02.jsp / out02_process.jsp ← ✅ out 내장 객체
│           ├── request.jsp / process.jsp    ← ✅ request 기본 메서드
│           ├── request01.jsp / request01_process.jsp ← ✅ 로그인 폼 처리
│           ├── request02.jsp                ← ✅ 요청 헤더 전체 출력
│           ├── request03.jsp                ← ✅ request 상세 정보 출력
│           ├── index.jsp / index_process.jsp ← ✅ 체크박스 처리
│           ├── response.jsp                 ← ✅ sendRedirect (Google)
│           ├── response01.jsp / response01_process.jsp / response01_success.jsp / response01_failed.jsp ← ✅ 로그인 리다이렉트
│           ├── response02.jsp               ← ✅ setIntHeader("Refresh", 5)
│           ├── response03.jsp               ← ✅ sendError(404)
│           ├── META-INF/MANIFEST.MF
│           └── WEB-INF/lib/
│
├── JSP0911/                                 ← 🆕 7장 실습 프로젝트 (파일 업로드)
│   ├── .classpath / .project
│   ├── .settings/                           ← gitignore됨
│   ├── build/classes/                       ← gitignore됨
│   └── src/main/
│       ├── java/                            ← Java 소스 (비어있음)
│       └── webapp/
│           ├── fileupload01.jsp             ← ✅ 단일 파일 업로드 폼 (cos.jar)
│           ├── fileupload01_process.jsp     ← ✅ MultipartRequest 처리 — 파라미터+파일 정보 출력
│           ├── fileupload02.jsp             ← ✅ 다중 파일(3개) 업로드 폼
│           ├── fileupload02_process.jsp     ← ✅ 3개 파일 처리 — 결과 테이블 출력
│           ├── fileupload03.jsp             ← ✅ 단일 파일 폼 (Commons FileUpload)
│           ├── fileupload03_process.jsp     ← ✅ DiskFileUpload + FileItem 처리
│           ├── fileupload04.jsp             ← ✅ 텍스트+파일 혼합 폼
│           ├── fileupload04_process.jsp     ← ✅ isFormField()로 폼/파일 분기 처리
│           ├── META-INF/MANIFEST.MF
│           └── WEB-INF/lib/                ← cos.jar, commons-fileupload.jar (gitignore됨)
│
├── BookMarket/                              ← 📚 누적 메인 프로젝트 (현재: 5장까지 완료)
│   ├── .classpath / .project / .gitignore
│   ├── .settings/                           ← gitignore됨
│   ├── build/classes/                       ← gitignore됨
│   └── src/main/
│       ├── java/
│       │   ├── dto/Book.java                ← ✅ [4장] 도서 DTO
│       │   └── dao/BookRepository.java      ← ✅ [4장] 도서 목록 저장소
│       └── webapp/
│           ├── Welcome0819.jsp              ← ✅ [2장] Bootstrap 시작 페이지
│           ├── welcome.jsp                  ← ✅ [3장] 모듈화
│           ├── menu.jsp / footer.jsp        ← ✅ [3장] 헤더/푸터 부품
│           ├── books.jsp                    ← ✅ [4장] 도서 목록 페이지
│           ├── META-INF/
│           └── WEB-INF/lib/
│
└── Servers/                                 ← Tomcat 로컬 설정 (gitignore됨)
    └── Tomcat v9.0 Server at localhost-config/
        └── tomcat-users.xml                 ← ⚠️ 계정 정보 포함 가능
```

### .gitignore 현황 (루트)
```gitignore
# Eclipse 워크스페이스 메타데이터
.metadata/

# 컴파일 결과물 (모든 하위 프로젝트 포함)
build/

# Eclipse IDE 설정
.settings/

# JAR 라이브러리
**/WEB-INF/lib/*.jar

# Tomcat 서버 설정 (계정 정보 포함 가능)
Servers/

# 컴파일된 클래스 파일
*.class

# 로그 파일
*.log

# 실습 완료 프로젝트 - 모두 정상 추적 중
# JSP0904, JSP0911 추적 대상 (임시 제외 해제: 2026-09-11)
```

> ✅ `/JSP0904/` 임시 제외 라인 삭제 → JSP0904, JSP0911 모두 Git 추적 대상으로 전환

---

## 🗓️ 2026-09-04 (오후 13:35)

### 변경사항 요약
| 구분 | 내용 |
|------|------|
| ➕ 추가 | `JSP0828/` 프로젝트 — 액션 태그 & JavaBeans 실습 (4장) |
| ➕ 추가 | `JSP0828/src/main/webapp/` — 15개 JSP 실습 파일 |
| ➕ 추가 | `JSP0828/src/main/java/dao/` — `Calculator.java`, `Person.java` |
| 🔧 변경 | `BookMarket/` — 3장(모듈화), 4장(도서목록) 파일 추가 |
| ➕ 추가 | `BookMarket/src/main/webapp/` — `welcome.jsp`, `menu.jsp`, `footer.jsp`, `books.jsp` |
| ➕ 추가 | `BookMarket/src/main/java/dto/Book.java` — 도서 DTO (JavaBean) |
| ➕ 추가 | `BookMarket/src/main/java/dao/BookRepository.java` — 도서 목록 저장소 |
| 🔧 변경 | 루트 `.gitignore` — 하위 경로 `**/WEB-INF/lib/*.jar` 패턴으로 보강 |
| ➕ 추가 | `GEMINI.md` — 에이전트 행동 지침 문서 신규 생성 |
| ➕ 추가 | `notes/2026-08-19.md`, `notes/2026-08-28.md` — 수업 정리 노트 |

### 현재 디렉토리 구조

```
JSPLecture/                                  ← Eclipse 워크스페이스 루트
│
├── .gitignore                               ← ✅ **/WEB-INF/lib/*.jar 등 보강
├── .project                                 ← 워크스페이스 메타 파일
├── DirectoryStructure.md                    ← 📄 이 파일
│
├── .metadata/                               ← Eclipse 런타임 데이터 (gitignore됨)
│
├── JSP0819/                                 ← 1~2장 실습 프로젝트
│   ├── .classpath / .project / .gitignore
│   ├── .settings/                           ← Eclipse IDE 설정 (gitignore됨)
│   ├── build/classes/                       ← 컴파일 결과물 (gitignore됨)
│   └── src/main/
│       ├── java/                            ← Java 소스 (비어있음)
│       └── webapp/
│           ├── Hello0819.jsp                ← ✅ 첫 번째 JSP 실습
│           ├── Welcome.jsp                  ← ✅ 쇼핑몰 환영 페이지
│           ├── META-INF/MANIFEST.MF
│           └── WEB-INF/lib/
│
├── JSP0828/                                 ← 🆕 3~4장 실습 프로젝트 (액션 태그 & JavaBeans)
│   ├── .classpath / .project
│   ├── .settings/                           ← Eclipse IDE 설정 (gitignore됨)
│   ├── build/classes/                       ← 컴파일 결과물 (gitignore됨)
│   └── src/main/
│       ├── java/dao/
│       │   ├── Calculator.java              ← ✅ JavaBean — 세제곱 계산
│       │   └── Person.java                  ← ✅ JavaBean — id/name 프로퍼티
│       └── webapp/
│           ├── first.jsp                    ← ✅ jsp:forward 실습
│           ├── second.jsp                   ← ✅ forward 목적지 (날짜 출력)
│           ├── firstInclude.jsp             ← ✅ jsp:include 실습
│           ├── secondInclude.jsp            ← ✅ include 목적지
│           ├── include.jsp                  ← ✅ include 액션 태그
│           ├── include_date.jsp             ← ✅ 포함될 날짜 출력 부품
│           ├── param01.jsp                  ← ✅ jsp:param 파라미터 전달
│           ├── param01_data.jsp             ← ✅ 파라미터 수신 및 출력
│           ├── useBean01.jsp                ← ✅ useBean — java.util.Date
│           ├── useBean02.jsp                ← ✅ useBean — Calculator
│           ├── useBean03.jsp                ← ✅ useBean — Person (scope=request)
│           ├── useBean04.jsp                ← ✅ useBean + include 조합
│           ├── setProperty.jsp              ← ✅ jsp:setProperty
│           ├── getProperty01.jsp            ← ✅ jsp:getProperty
│           ├── getProperty02.jsp            ← ✅ setProperty + getProperty 전체 흐름
│           ├── META-INF/MANIFEST.MF
│           └── WEB-INF/lib/
│
├── JSP0904/                                 ← ⏸️ gitignore 처리 중 (추후 공개 예정)
│
├── BookMarket/                              ← 📚 누적 메인 프로젝트 (현재: 4장까지 완료)
│   ├── .classpath / .project / .gitignore
│   ├── .settings/                           ← gitignore됨
│   ├── build/classes/                       ← gitignore됨
│   └── src/main/
│       ├── java/
│       │   ├── dto/
│       │   │   └── Book.java                ← ✅ [4장] 도서 DTO (JavaBean, Serializable)
│       │   └── dao/
│       │       └── BookRepository.java      ← ✅ [4장] 도서 목록 저장소 (하드코딩 3권)
│       └── webapp/
│           ├── Welcome0819.jsp              ← ✅ [2장] Bootstrap 적용 시작 페이지
│           ├── welcome.jsp                  ← ✅ [3장] include 디렉티브로 모듈화
│           ├── menu.jsp                     ← ✅ [3장] 네비게이션 헤더 부품
│           ├── footer.jsp                   ← ✅ [3장] 푸터 부품
│           ├── books.jsp                    ← ✅ [4장] 도서 목록 페이지 (JavaBeans)
│           ├── META-INF/
│           └── WEB-INF/lib/
│
└── Servers/                                 ← Tomcat 로컬 설정 (gitignore됨)
    └── Tomcat v9.0 Server at localhost-config/
        └── tomcat-users.xml                 ← ⚠️ 계정 정보 포함 가능
```

### .gitignore 현황 (루트)
```gitignore
# Eclipse 워크스페이스 메타데이터
.metadata/

# 컴파일 결과물 (모든 하위 프로젝트 포함)
build/

# Eclipse IDE 설정
.settings/

# JAR 라이브러리 (모든 하위 경로)
**/WEB-INF/lib/*.jar

# Tomcat 서버 설정 (계정 정보 포함 가능)
Servers/

# 컴파일된 클래스 파일
*.class

# 로그 파일
*.log

# 실습 중 임시 제외 프로젝트
/JSP0904/
```

> ✅ 이전 패턴(`/WEB-INF/lib/*.jar`)의 `/` prefix 문제를 `**/WEB-INF/lib/*.jar`로 수정하여
> 모든 하위 프로젝트의 JAR 파일이 올바르게 gitignore 처리됩니다.

---

## 🗓️ 2026-08-19 (오후 16:00)

### 변경사항 요약
| 구분 | 내용 |
|------|------|
| ➕ 추가 | `BookMarket/` 프로젝트 신규 생성 |
| ➕ 추가 | `DirectoryStructure.md` 문서 생성 |
| ✅ 개선 | 루트 `.gitignore` 항목 1개 → 7개로 보강 |

### 현재 디렉토리 구조

```
JSPLecture/                                  ← Eclipse 워크스페이스 루트
│
├── .gitignore                               ← ✅ 7개 규칙으로 보강됨
├── .project                                 ← 워크스페이스 메타 파일 (Eclipse)
├── DirectoryStructure.md                    ← 📄 이 파일
│
├── .metadata/                               ← Eclipse 런타임 데이터 (gitignore됨)
│   ├── .lock / .log
│   ├── .mylyn/ / .plugins/
│   └── version.ini
│
├── JSP0819/                                 ← 첫 번째 실습 프로젝트
│   ├── .classpath                           ← 클래스패스 설정 (JRE 21, Tomcat 9.0)
│   ├── .project / .gitignore
│   ├── .settings/                           ← Eclipse 프로젝트별 IDE 설정 (7개 파일)
│   ├── build/classes/                       ← 컴파일 결과물 (gitignore됨)
│   └── src/main/
│       ├── java/                            ← Java 소스 (비어있음)
│       └── webapp/
│           ├── Hello0819.jsp                ← ✅ 실습 파일
│           ├── Welcome.jsp                  ← ✅ 실습 파일
│           ├── META-INF/MANIFEST.MF
│           └── WEB-INF/lib/                 ← JAR 라이브러리 (비어있음)
│
├── BookMarket/                              ← 🆕 두 번째 실습 프로젝트 (신규)
│   ├── .classpath / .project / .gitignore
│   ├── .settings/                           ← Eclipse 프로젝트별 IDE 설정 (7개 파일)
│   ├── build/classes/                       ← 컴파일 결과물 (gitignore됨)
│   └── src/main/
│       ├── java/                            ← Java 소스 (비어있음)
│       └── webapp/
│           ├── Welcome0819.jsp              ← ✅ 실습 파일
│           ├── welcome.jsp                  ← ✅ 실습 파일
│           ├── menu.jsp                     ← ✅ 실습 파일 (네비게이션 메뉴)
│           ├── footer.jsp                   ← ✅ 실습 파일 (푸터)
│           ├── META-INF/
│           └── WEB-INF/lib/                 ← JAR 라이브러리 (비어있음)
│
└── Servers/                                 ← Tomcat 로컬 설정 (gitignore됨)
    ├── .project / .settings/
    └── Tomcat v9.0 Server at localhost-config/
        ├── server.xml / web.xml / context.xml
        ├── catalina.policy / catalina.properties
        └── tomcat-users.xml                 ← ⚠️ 계정 정보 포함 가능
```

### .gitignore 현황 (루트)
```gitignore
/.metadata/
/build/
/WEB-INF/lib/*.jar
/.settings/
Servers/
/*.class
/.log
```

> ⚠️ 현재 패턴 앞의 `/`로 인해 루트 직속 폴더에만 적용됩니다.
> `JSP0819/build/`, `BookMarket/build/` 등 하위 경로에도 적용하려면
> 앞의 `/`를 제거하여 `build/`, `.settings/` 형태로 변경하세요.

---

## 🗓️ 2026-08-19 (오전 10:48)

### 변경사항 요약
| 구분 | 내용 |
|------|------|
| 🆕 최초 | 워크스페이스 최초 분석 |
| ➕ 추가 | `JSP0819/` 프로젝트 생성 |

### 현재 디렉토리 구조

```
JSPLecture/                                  ← Eclipse 워크스페이스 루트
│
├── .gitignore                               ← /.metadata/ 만 등록됨
├── .project                                 ← 워크스페이스 메타 파일 (Eclipse)
│
├── .metadata/                               ← Eclipse 런타임 데이터 (gitignore됨)
│   ├── .lock                                ← 워크스페이스 잠금 파일
│   ├── .log                                 ← Eclipse 런타임 로그 (316KB)
│   ├── .mylyn/                              ← Mylyn 태스크 관리 플러그인 데이터
│   ├── .plugins/                            ← Eclipse 플러그인 런타임 상태
│   └── version.ini                          ← Eclipse 버전 정보
│
├── JSP0819/                                 ← 첫 번째 JSP 실습 프로젝트
│   ├── .classpath                           ← 클래스패스 설정 (JRE 21, Tomcat 9.0)
│   ├── .project / .gitignore
│   ├── .settings/                           ← Eclipse IDE 설정 (7개 파일)
│   ├── build/classes/                       ← 컴파일 결과물 (비어있음)
│   └── src/main/
│       ├── java/                            ← Java 소스 (비어있음)
│       └── webapp/
│           ├── Hello0819.jsp                ← ✅ 실습 파일
│           ├── Welcome.jsp                  ← ✅ 실습 파일
│           ├── META-INF/MANIFEST.MF
│           └── WEB-INF/lib/                 ← JAR 라이브러리 (비어있음)
│
└── Servers/                                 ← Eclipse Tomcat 서버 설정
    ├── .project / .settings/
    └── Tomcat v9.0 Server at localhost-config/
        ├── server.xml                       ← Tomcat 서버 설정
        ├── web.xml                          ← Tomcat 기본 웹 설정
        ├── context.xml / catalina.policy / catalina.properties
        └── tomcat-users.xml                 ← ⚠️ 계정 정보 포함 가능
```

### .gitignore 현황 (루트)
```gitignore
/.metadata/
```

---

<!--
==============================================
  새 항목 추가 방법 (TEMPLATE)
  - "변경 이력" 섹션 바로 아래에 복사해서 붙여넣기
==============================================

## 🗓️ YYYY-MM-DD (오전/오후 HH:MM)

### 변경사항 요약
| 구분 | 내용 |
|------|------|
| ➕ 추가 | `프로젝트명/` 신규 생성 |
| 🔧 변경 | ... |
| 🗑️ 삭제 | ... |

### 현재 디렉토리 구조
```
JSPLecture/
...
```

### .gitignore 현황 (루트)
```gitignore
...
```

---
==============================================
-->