# 📁 BigDataFramework 디렉토리 구조 기록

> 빅데이터프레임워크 과목 수업 및 실습 아카이브 워크스페이스
> 변경사항이 생길 때마다 날짜별로 디렉토리 구조의 스냅샷과 변경 내역을 누적하여 기록합니다.

---

## 변경 이력 (Changelog)

<!-- 새 항목은 맨 위에 추가하세요 (최신순) -->

---

## 🗓️ 2026-08-21 (금)

### 변경사항 요약
| 구분 | 내용 |
|------|------|
| 🆕 최초 | 빅데이터프레임워크 워크스페이스 초기화 및 분석 |
| ➕ 추가 | `notes/` - 1회차 강의 자료(`2026_빅데이터프레임워크_1.pdf`) 추가 |
| ➕ 추가 | `daily_practice/260821_fri/` - 당일 실습 코드 및 컴포넌트별 상세 정리 문서(`2026-08-21.md`) 작성 |
| ➕ 추가 | `exam1/` - Vite 기반 Vue 3 실습 프로젝트 구성 및 컴포넌트 실습 |
| ➕ 추가 | `exam1/src/components/RawHTML.vue` - 원시 HTML 렌더링(`v-html` vs `{{ }}`) 컴포넌트 추가 |
| ➕ 추가 | `exam1/src/components/AttrBind1.vue` - 속성 바인딩 기본(`v-bind`, `:`) 컴포넌트 추가 |
| ➕ 추가 | `exam1/src/components/AttrBind2.vue` - 불리언 속성 바인딩(`:disabled`) 컴포넌트 추가 |
| ➕ 추가 | `DirectoryStructure.md` 및 `README.md` 문서 생성 |
| ➕ 추가 | `.gitignore` - 전역 깃 무시 규칙(의존성, 빌드 산출물, 환경변수, OS/IDE 임시파일 등) 추가 |
| ➕ 추가 | `GEMINI.md` - 워크스페이스 전용 실습 아카이빙 및 디렉토리 관리 규칙 등록 |

### 현재 디렉토리 구조

```text
BigDataFramework/                            ← 빅데이터프레임워크 워크스페이스 루트
│
├── .gitignore                               ← 🚫 Git 제외 규칙 (전역 적용)
├── GEMINI.md                                ← ⚙️ 워크스페이스 실습 관리 규칙
├── README.md                                ← 📄 프로젝트 소개 문서
├── DirectoryStructure.md                    ← 📄 디렉토리 구조 및 변경 이력 기록 (본 문서)
├── package-lock.json                        ← 루트 패키지 락 파일
│
├── notes/                                   ← 📖 강의 자료 및 이론 노트
│   └── 2026_빅데이터프레임워크_1.pdf         ← 1회차 수업 PDF 교안
│
├── daily_practice/                          ← 📂 날짜별 수업 실습 아카이브
│   └── 260821_fri/                          ← 🧪 8월 21일 실습 모음
│       ├── 2026-08-21.md                    ← 📝 당일 실습 코드 분석 및 컴포넌트별 정리 문서
│       ├── test.js                          ← JS 기초 테스트
│       └── test1.js                         ← JS 기초 테스트 2
│
└── exam1/                                   ← 🛠️ Vue 3 + Vite 실습 프로젝트
    ├── index.html                           ← HTML 엔트리 포인트
    ├── package.json                         ← 프로젝트 의존성 및 스크립트 설정
    ├── package-lock.json
    ├── jsconfig.json                        ← JS 프로젝트 설정
    ├── vite.config.js                       ← Vite 번들러 설정
    ├── README.md                            ← 프로젝트 안내
    ├── node_modules/                        ← 프로젝트 종속성 (빌드 모듈)
    ├── public/
    │   └── favicon.ico                      ← 파비콘
    └── src/
        ├── main.js                          ← 앱 엔트리 포인트 (createApp)
        ├── App.vue                          ← 메인 루트 컴포넌트
        ├── App copy.vue                     ← 루트 컴포넌트 백업본
        ├── ButtonCounter.vue                ← 카운터 버튼 컴포넌트
        ├── TextInterpolation.vue            ← 텍스트 보간법 컴포넌트
        ├── assets/                          ← 정적 리소스 (CSS, 로고 등)
        │   ├── base.css
        │   ├── main.css
        │   └── logo.svg
        └── components/                      ← Vue 컴포넌트
            ├── RawHTML.vue                  ← 원시 HTML 렌더링 실습 컴포넌트
            ├── AttrBind1.vue                ← 🆕 속성 바인딩 기본(v-bind, :) 실습 컴포넌트
            ├── AttrBind2.vue                ← 🆕 불리언 속성 바인딩(:disabled) 실습 컴포넌트
            ├── HelloWorld.vue
            ├── TheWelcome.vue
            ├── WelcomeItem.vue
            └── icons/                       ← SVG 아이콘 컴포넌트 (5개)
```

### 세부 설명 및 실습 내용
1. **`notes/` (이론 강의 자료)**
   - 빅데이터 프레임워크 수업 교안 보관.
2. **`daily_practice/260821_fri/` (날짜별 실습 및 정리 문서)**
   - [`2026-08-21.md`](file:///C:/Users/AI-00/Desktop/하이테크_/2ndTerm/BigDataFramework/daily_practice/260821_fri/2026-08-21.md):
     - JS 기본 문법 (`test.js`, `test1.js`)
     - 실습 1: 텍스트 보간법 (`TextInterpolation.vue` ↔ `App.vue`)
     - 실습 2: 반응형 버튼 카운터 (`ButtonCounter.vue` ↔ `App.vue`)
     - 실습 3: 원시 HTML 렌더링 (`RawHTML.vue` ↔ `App.vue`, `v-html` vs `{{ }}`)
     - 실습 4: 속성 바인딩 기본 (`AttrBind1.vue` ↔ `App.vue`, `v-bind`, `:`)
     - 실습 5: 불리언 속성 바인딩 (`AttrBind2.vue` ↔ `App.vue`, `:disabled`, Truthy/Falsy)
     - 핵심 문법 정리 표 (Key Takeaways) 수록
3. **`exam1/` (Vite 프로젝트 실습)**
   - Vite 기반 Vue 3 단일 페이지 애플리케이션(SPA) 프로젝트 구성.
   - 단일 파일 컴포넌트(SFC) 작성 및 `App.vue`와 자식 컴포넌트 연동 실습.

---

<!--
==============================================
  새 항목 추가 방법 (TEMPLATE)
  - "변경 이력" 구분선 바로 아래에 복사해서 최신순으로 붙여넣기
==============================================

## 🗓️ YYYY-MM-DD (요일)

### 변경사항 요약
| 구분 | 내용 |
|------|------|
| ➕ 추가 | `폴더명/` 또는 `파일명` 추가 |
| 🔧 변경 | ... |
| 🗑️ 삭제 | ... |

### 현재 디렉토리 구조
```text
BigDataFramework/
│
├── ...
```

### 세부 설명 및 실습 내용
- 실습 및 변경 내용 상세 기술

---
==============================================
-->
