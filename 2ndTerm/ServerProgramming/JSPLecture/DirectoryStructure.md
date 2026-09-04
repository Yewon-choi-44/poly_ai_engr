# 📁 JSPLecture 디렉토리 구조 기록

> Eclipse IDE 기반 JSP/Servlet 웹 프로젝트 워크스페이스
> 변경사항이 생길 때마다 날짜별로 기록합니다.

---

## 변경 이력 (Changelog)

<!-- 새 항목은 맨 위에 추가하세요 (최신순) -->

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