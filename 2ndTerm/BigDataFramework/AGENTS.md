# 📚 BigDataFramework 수업 및 실습 관리 지침

이 워크스페이스는 빅데이터프레임워크 과목의 수업 자료 및 실습 코드를 관리하는 공간입니다.
실습 정리 및 디렉토리 관리 요청 시 아래 원칙을 항상 준수합니다.

---

## 0. 작업 시작 전 최우선 점검 — `.gitignore` 및 저장소 범위

어떤 작업이든 시작하기 전에 **가장 먼저** 다음 두 가지를 점검한다.

- **`.gitignore` 최신 상태 확인**: 새 실습 프로젝트(`exam{N}/`, `flexblog/`, `todolist/` 유형)가 추가될 때 `node_modules/`, `dist/`, `.vite/`, `*.tsbuildinfo` 등 빌드 산출물이 여전히 무시되는지 확인한다. 이 저장소는 이미 `node_modules/`, 빌드 캐시, 환경변수 파일, OS 임시파일, 그리고 `notes/` 폴더 전체(강의 PDF 등 대용량 자료)까지 폭넓게 gitignore하고 있다 — 다른 두 과목 저장소(`ServerProgramming`은 `notes/*.md`를 추적, `ComputerVisionLab`도 `notes/`를 추적)와 달리 **이 저장소는 `notes/`를 통째로 Git에서 제외**하는 점에 유의한다.
- **저장소 범위 확인**: 이 폴더의 `.git`은 `BigDataFramework/`이나 `2ndTerm/`이 아니라 **훨씬 상위인 `C:\Users\AI-00\Desktop\하이테크_`**에 있다(`git rev-parse --show-toplevel`로 확인 가능). 즉 `2ndTerm/` 아래의 `ComputerVisionLab`, `ServerProgramming`, `AIFramework`, `AISystemDevelopmentandOperationsPracticum`뿐 아니라, `하이테크_` 바로 아래의 `AI_DataPreprocessing`, `Database_SQL`, `기계학습프로그래밍`, `웹프로그래밍`, `자바프로그래밍` 등 **다른 학기·다른 과목 폴더까지 전부 같은 git 저장소를 공유**한다. 따라서:
  - `git status`/`git add`/`git commit` 등은 항상 `BigDataFramework/` 경로로 범위를 제한한다 (예: `git status -- .`, `git add BigDataFramework/...`).
  - 다른 과목 폴더의 변경 사항은 이 워크스페이스 작업과 무관하므로 손대거나 커밋에 포함하지 않는다.

---

## 1. 일별 실습 아카이빙 원칙 (`daily_practice/`)
- 실습 코드는 `daily_practice/YYMMDD_요일/` (예: `daily_practice/260821_fri/`, `daily_practice/260827_thu/`) 폴더 아래에 날짜별로 모아둡니다.
- `exam1/src`, `exam2/src` 등 하위 실습 프로젝트에서 작성한 개별 `.vue` 컴포넌트, 페이지 파일(`src/pages/`), 스크립트(`.js`, `.ts`)를 해당 날짜 폴더로 수집/보관합니다.

## 2. 실습 정리 마크다운 문서화 (`YYYY-MM-DD.md`)
- 각 날짜 폴더 내에 `YYYY-MM-DD.md` 문서를 작성하여 당일 실습 내용을 체계적으로 정리합니다.
- **필수 포함 항목**:
  1. **개별 실습/페이지 컴포넌트 (`*.vue`)**: 전체 코드 및 핵심 동작 원리 설명
  2. **실행 환경 및 진입 구조**:
     - 단일 컴포넌트 교체 방식(`exam1`): 대응되는 부모 컴포넌트(`App.vue`) 및 임포트/렌더링 코드
     - 라우팅 방식(`exam2` 등): 파일 기반 라우팅 경로 매핑(URL), `<router-view>` 및 Vuetify 루트 구조
  3. **스크립트/테스트 코드 (`*.js`, `*.ts`)**: 문법 테스트, 유틸리티, 백업 스크립트 등
  4. **TypeScript 및 UI 라이브러리 연동**: TypeScript 인터페이스/타입, Vuetify 3 컴포넌트(`v-*`) 속성 및 활용법
  5. **💡 핵심 문법 정리 표 (Key Takeaways)**: 당일 학습한 Vue 3 (Reactivity, Computed, Binding, v-model 등) 및 Vuetify/JS 주요 개념 요약

## 3. 디렉토리 구조 및 변경 이력 누적 (`DirectoryStructure.md`)
- 새로운 실습, 폴더, 설정 파일이 추가될 때마다 `DirectoryStructure.md`의 `## 변경 이력 (Changelog)` 섹션 최상단에 새 날짜를 추가합니다.
- **필수 포함 내용**:
  - 변경사항 요약 표 (`➕ 추가`, `🔧 변경`, `🗑️ 삭제`)
  - 해당 시점의 전체 디렉토리 구조 트리 (설명 주석 포함)
  - 세부 설명 및 실습 내용

## 4. Git 및 저장소 관리
- `node_modules/`, `dist/`, `.env`, OS 임시파일 등 대용량/임시 파일이 깃에 추적되지 않도록 루트 `.gitignore` 상태를 항상 준수합니다.
- 루트 `README.md`의 바로가기 링크를 항상 최신 상태로 유지합니다.
- 0번 원칙대로, 이 저장소는 `하이테크_` 전체를 아우르는 git 저장소의 일부입니다. 커밋 범위를 `BigDataFramework/`으로 항상 제한하세요.

## 5. AI 어시스턴트 행동 원칙
- **역할**: 실습 코드(`.vue`, `.ts`, `.js` 등)는 직접 작성·수정하지 않는다. AI의 역할은 `daily_practice/*.md` 작성, `DirectoryStructure.md`/`README.md` 갱신, `.gitignore` 관리 등 **기록과 정리**로 한정한다. (Spring_2026, ComputerVisionLab, ServerProgramming 워크스페이스와 동일한 원칙이며, 이 저장소에서 다르게 운영하고 싶다면 언제든 조정 가능하다.)
- **새 실습 발견 시**: `daily_practice/`나 `DirectoryStructure.md`에 아직 반영되지 않은 날짜별 프로젝트나 파일을 발견하면, 임의로 코드를 고치지 않고 기존 형식(2번, 3번 원칙)에 맞춰 기록하거나 먼저 사용자에게 알린다.
- **보안**: `.env` 등 민감 정보가 포함된 파일은 절대 Git에 커밋하지 않는다.
- **`exam0902/AGENTS.md`와의 관계**: `exam0902/` 하위의 `AGENTS.md`는 이 파일과 별개로, Vue/Vite 스캐폴딩이 자동 생성한 프로젝트 전용 규칙 파일이다(코드 스타일, 스택 정보 등). 이 워크스페이스 루트의 `AGENTS.md`(본 파일)를 덮어쓰거나 대체하지 않으며, 서로 다른 스코프이므로 건드리지 않는다.
