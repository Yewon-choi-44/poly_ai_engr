# 🖥️ 서버 프로그래밍 (Server Programming) 수업 및 실습 아카이브

서버 프로그래밍 과목의 강의 자료, JSP/Servlet 실습 프로젝트, 날짜별 정리 노트를 관리하는 저장소입니다.

- **교재**: 《쉽게 배우는 JSP 웹 프로그래밍(2판)》(송미영 저, 한빛아카데미)
- **실습 환경**: Eclipse IDE + Apache Tomcat 9.0 + JDK 21 + MySQL 8.0
- **핵심 프로젝트**: `BookMarket` (도서 쇼핑몰) — 장마다 기능을 누적해서 완성

디렉토리 구조의 날짜별 변경 내역과 트리 스냅샷은 [`JSPLecture/DirectoryStructure.md`](./JSPLecture/DirectoryStructure.md)에서 누적 관리합니다.

---

## 📌 빠른 바로가기

- 📂 [전체 디렉토리 구조 및 날짜별 변경 이력 (`JSPLecture/DirectoryStructure.md`)](./JSPLecture/DirectoryStructure.md)
- ⚙️ [워크스페이스 실습 관리 규칙 (`AGENTS.md`)](./AGENTS.md)
- 📚 [BookMarket 누적 정리 노트 (`notes/BookMarket.md`)](./notes/BookMarket.md)
- 📖 [전체 강의 장별 요약 (`notes/server-programming-course-summary.md`)](./notes/server-programming-course-summary.md)
- 🗂️ [강의 슬라이드 Ch00~Ch18 (`notes/ppt_40006/`)](./notes/ppt_40006/)
- 🛠️ [Eclipse 워크스페이스 (`JSPLecture/`)](./JSPLecture/)
- 📦 [교재 배포 소스 원본 (`source/`, Git 미추적)](./source/)

---

## 📝 날짜별 실습 정리 노트

| 날짜 | 교재 장 | 주제 | 실습 프로젝트 | 노트 |
|---|---|---|---|---|
| 2026-08-19 | 1·2장 | JSP 개요, 스크립트 태그 | `JSP0819` | [`2026-08-19.md`](./notes/2026-08-19.md) |
| 2026-08-28 | 3·4장 | 디렉티브 태그, 액션 태그 & JavaBeans | `JSP0828` | [`2026-08-28.md`](./notes/2026-08-28.md) |
| 2026-09-04 | 5장 | JSP 내장 객체 | `JSP0904` | [`2026-09-04.md`](./notes/2026-09-04.md) |
| 2026-09-11 | 7장 | 파일 업로드 | `JSP0911` | [`2026-09-11.md`](./notes/2026-09-11.md) |
| 2026-09-18 | 8장 | 유효성 검사 (JavaScript) | `JSP0918` | [`2026-09-18.md`](./notes/2026-09-18.md) |
| 2026-10-08 | 10장 | 시큐리티 (선언적 보안, FORM 인증) | `JSP1008` | [`2026-10-08.md`](./notes/2026-10-08.md) |
| 2026-10-12 | 11장 | 예외 처리 + 교재 전체 소스(`JSPSource`) 가져오기 | `JSP1012`, `JSPSource` | [`2026-10-12.md`](./notes/2026-10-12.md) |
| 2026-10-19 | 8·10·12장 | 종합 평가 (유효성 검사 + 보안 + 필터) | `EXAM1019` | [`2026-10-19.md`](./notes/2026-10-19.md) |

---

## 📚 BookMarket 진행 현황

| 장 | 기능 | 상태 |
|---|---|---|
| 1~7장 | 프로젝트 생성 → Bootstrap 시작 페이지 → 모듈화 → 도서 목록/상세 → 도서 등록 폼 → 이미지 업로드 | ✅ 완료 |
| 8장 | 도서 등록 폼 클라이언트 유효성 검사 (`validation.js`) | 🔶 진행 중 (버그 있음) |
| 9장 | 다국어 처리 — 언어 전환 링크만 추가 | 🔶 진행 중 |
| 10장 | 관리자 로그인으로 도서 등록 보호, 로그아웃 | ✅ 완료 (2026-10-08) |
| 11장~ | 예외 처리 페이지, 필터 로그, 장바구니(세션), 주문(쿠키), DB 연동, 회원, 게시판 | ⏳ 예정 |

자세한 코드와 이슈는 [`notes/BookMarket.md`](./notes/BookMarket.md) 참고.

---

## 📁 최상위 구조

```text
ServerProgramming/
├── AGENTS.md                ← AI 어시스턴트 정리 규칙
├── README.md                ← 이 문서
├── JSPLecture/              ← Eclipse 워크스페이스 (JSP0819 ~ JSP1012, JSPSource, EXAM1019, BookMarket)
│   └── DirectoryStructure.md
├── notes/                   ← 날짜별 노트, BookMarket 노트, 강의 요약, 슬라이드
└── source/                  ← 교재 배포 소스 원본 (BookMarket 장별 완성본, JSPBook, 실습환경 — Git 미추적)
```

> 🔒 `source/`(루트 `.gitignore`), `Servers/`(Tomcat `tomcat-users.xml` 계정 정보), `build/`, `.settings/`, `WEB-INF/lib/*.jar`는 Git 추적에서 제외되어 있습니다.
