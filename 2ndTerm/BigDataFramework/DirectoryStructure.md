# 📁 BigDataFramework 디렉토리 구조 기록

> 빅데이터프레임워크 과목 수업 및 실습 아카이브 워크스페이스
> 변경사항이 생길 때마다 날짜별로 디렉토리 구조의 스냅샷과 변경 내역을 누적하여 기록합니다.

---

## 변경 이력 (Changelog)

<!-- 새 항목은 맨 위에 추가하세요 (최신순) -->

---

## 🗓️ 2026-09-02 (수)

### 변경사항 요약
| 구분 | 내용 |
|------|------|
| ➕ 추가 | `notes/` - 4회차 강의 자료(`2026_빅데이터프레임워크_4.pdf`) 추가 |
| ➕ 추가 | `daily_practice/260902_wed/` - 당일 실습 코드 아카이빙 및 상세 실습 정리 문서(`2026-09-02.md`) 작성 |
| ➕ 추가 | `exam0902/` - Vue 3 + Vuetify 3 + Vue Router + TypeScript 기반의 세 번째 실습 프로젝트 신규 구성 |
| ➕ 추가 | `exam0902/src/components/BlogPost.vue` - Props 기본 전달 자식 컴포넌트 추가 |
| ➕ 추가 | `exam0902/src/pages/BlogPage.vue` - BlogPost 정적 Props 전달 부모 페이지 추가 |
| ➕ 추가 | `exam0902/src/pages/BlogPageVFor.vue` - v-for 반복문 연동 Props 전달 부모 페이지 추가 |
| ➕ 추가 | `exam0902/src/components/BlogPostEmit.vue` - 자식 컴포넌트 커스텀 이벤트 발신(`defineEmits`) 실습 컴포넌트 추가 |
| ➕ 추가 | `exam0902/src/pages/BlohPageEmit.vue` - 부모 컴포넌트 이벤트 수신 및 동적 상태 변경 페이지 추가 |
| ➕ 추가 | `exam0902/src/pages/BlogPageEmitStandalone.vue` - 개별 포스트 상태 제어 테스트 페이지 추가 |
| ➕ 추가 | `exam0902/src/components/ChildComp.vue` - Vue 3.4+ `defineModel()` 양방향 바인딩 실습 컴포넌트 추가 |
| ➕ 추가 | `exam0902/src/pages/ParentComp.vue` - `ChildComp`와 단일 `v-model` 바인딩 부모 페이지 추가 |
| ➕ 추가 | `exam0902/src/components/ChildCompIn.vue` / `ChildCompIn2.vue` - 전통적 `modelValue` + `update:modelValue` 양방향 바인딩 자식 컴포넌트 추가 |
| ➕ 추가 | `exam0902/src/pages/ParentCompIn.vue` / `ParentCompIn2.vue` - 전통적 props/emit 기반 양방향 바인딩 부모 페이지 추가 |
| ➕ 추가 | `exam0902/src/components/ChildCompParam.vue` - 다중 `defineModel('title')`, `defineModel('subtitle')` 자식 컴포넌트 추가 |
| ➕ 추가 | `exam0902/src/pages/ParentCompParam.vue` - 다중 `v-model:title`, `v-model:subtitle` 바인딩 부모 페이지 추가 |
| ➕ 추가 | `exam0902/src/components/ChildCompParam2.vue` - 3개 인수(`title`, `subtitle`, `content`) `defineModel` 자식 컴포넌트 추가 |
| ➕ 추가 | `exam0902/src/pages/ParentCompParam2.vue` - 3개 인수 `v-model` 바인딩 부모 페이지 추가 |
| ➕ 추가 | `exam0902/src/components/AlertBox.vue` - 기본 `<slot />` 컨텐츠 배포 실습 컴포넌트 추가 |
| ➕ 추가 | `exam0902/src/pages/ComponentSlot.vue` - `AlertBox` 슬롯 렌더링 부모 페이지 추가 |
| ➕ 추가 | `exam0902/src/pages/YesNoQuestion.vue` - `watch` 반응형 감시자 및 fetch API(`https://yesno.wtf/api`) 비동기 연동 페이지 추가 |
| ➕ 추가 | `exam0902/src/pages/TemplateRef.vue` - DOM 엘리먼트 및 `v-for` 요소 템플릿 참조(`ref`) 실습 페이지 추가 |
| ➕ 추가 | `exam0902/src/components/ChildExpose.vue` - 자식 컴포넌트 `defineExpose` 노출 속성 실습 컴포넌트 추가 |
| ➕ 추가 | `exam0902/src/pages/ComponentRef.vue` - 자식 컴포넌트 인스턴스 템플릿 참조 및 메서드 호출 페이지 추가 |
| ➕ 추가 | `exam0902/src/components/LifeCycleHookComp.vue` - `onMounted`, `onUpdated`, `onUnmounted` 라이프사이클 훅 실습 컴포넌트 추가 |
| ➕ 추가 | `exam0902/src/pages/LifeCycleHookPage.vue` - 조건부 렌더링(`v-if`)을 통한 라이프사이클 실행 시점 관찰 페이지 추가 |
| ➕ 추가 | `PracticeFile/` - Vuetify 3 인스타그램 클론 프로젝트 리소스 및 컴포넌트 폴더 추가 |
| ➕ 추가 | `PracticeFile/pages/Instagram.vue` - Vuetify 3 기반 인스타그램 메인 레이아웃 엔트리 페이지 추가 |
| ➕ 추가 | `PracticeFile/components/MainNavUnf.vue` - 좌측 내비게이션 Drawer 컴포넌트 추가 |
| ➕ 추가 | `PracticeFile/components/AppBarUnf.vue` - 상단 검색/액션 AppBar 컴포넌트 추가 |
| ➕ 추가 | `PracticeFile/components/ProfilePageUnf.vue` - 중앙 메인 피드 그리드 컴포넌트 추가 |
| ➕ 추가 | `PracticeFile/components/RightNavUnf.vue` - 우측 프로필 정보 Drawer 컴포넌트 추가 |
| ➕ 추가 | `PracticeFile/assets/` - 인스타그램 로고 및 프로필 이미지 리소스 추가 |
| 🔧 변경 | `exam2/src/pages/VTextFields_2.vue` - `prepend-inner-icon`을 `mdi-abjad-arabic`으로 변경 |
| 🔧 변경 | `.gitignore` - 에디터/IDE 임시 파일(`.metadata/`) 제외 항목 추가 |
| 🔧 변경 | `README.md` - `exam0902/`, `PracticeFile/` 신규 프로젝트 바로가기 링크 최신화 |

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
│   ├── 2026_빅데이터프레임워크_1.pdf         ← 1회차 수업 PDF 교안
│   ├── 2026_빅데이터프레임워크_2.pdf         ← 2회차 수업 PDF 교안 (Vue 3 반응성 시스템)
│   ├── 2026_빅데이터프레임워크_3.pdf         ← 3회차 수업 PDF 교안 (Computed/Watch, 폼 바인딩, Vuetify 3)
│   └── 2026_빅데이터프레임워크_4.pdf         ← 4회차 수업 PDF 교안 (컴포넌트 심화, Props/Emit, Slot, Lifecycle)
│
├── scripts/                                 ← 🛠️ 워크스페이스 관리 및 자동화 스크립트
│   └── backup.js                            ← 아카이빙/백업 유틸리티 스크립트
│
├── daily_practice/                          ← 📂 날짜별 수업 실습 아카이브
│   ├── 260821_F/                            ← 🧪 8월 21일 실습 모음
│   │   ├── 2026-08-21.md                    ← 📝 당일 실습 코드 분석 및 컴포넌트별 정리 문서
│   │   ├── test.js                          ← JS 기초 테스트
│   │   └── test1.js                         ← JS 기초 테스트 2
│   ├── 260827_thu/                          ← 🧪 8월 27일 실습 모음
│   │   ├── 2026-08-27.md                    ← 📝 당일 실습 코드 분석 및 컴포넌트별 상세 정리 문서
│   │   └── *.vue                            ← 당일 실습 .vue 컴포넌트 (총 26개 파일)
│   └── 260902_wed/                          ← 🧪 9월 2일 실습 모음
│       ├── 2026-09-02.md                    ← 📝 당일 실습 코드 분석 및 컴포넌트별 상세 정리 문서
│       ├── *.vue                            ← 당일 실습 .vue 컴포넌트 (26개)
│       └── instagram_practice/              ← 📱 인스타그램 UI 실습 파일 및 에셋 아카이브
│
├── exam1/                                   ← 🛠️ Vue 3 + Vite 반응성 심화 실습 프로젝트
│   └── ... (기존 파일 유지)
│
├── exam2/                                   ← 🛠️ Vue 3 + Vuetify 3 + TS 실습 프로젝트
│   └── src/pages/
│       └── VTextFields_2.vue                ← 🔧 아이콘 속성 수정
│
├── exam0902/                                ← 🛠️ [신규] Vue 3 심화 + Vuetify 3 + TS 실습 프로젝트
│   ├── index.html                           ← HTML 엔트리 포인트
│   ├── package.json                         ← 프로젝트 의존성 (Vuetify, Vue-Router, TS 등)
│   ├── vite.config.mts                      ← Vite 번들러 설정
│   ├── tsconfig.json                        ← TS 설정
│   └── src/
│       ├── main.ts                          ← 앱 엔트리 포인트
│       ├── App.vue                          ← 메인 루트 컴포넌트 (<v-app>, <router-view>)
│       ├── components/                      ← 재사용 실습 컴포넌트
│       │   ├── BlogPost.vue                 ← 🆕 Props 기본 정의 컴포넌트
│       │   ├── BlogPostEmit.vue             ← 🆕 Emit 이벤트 발신 컴포넌트
│       │   ├── ChildComp.vue                ← 🆕 Vue 3.4+ defineModel 컴포넌트
│       │   ├── ChildCompIn.vue              ← 🆕 전통적 modelValue + update:modelValue 컴포넌트 1
│       │   ├── ChildCompIn2.vue             ← 🆕 전통적 modelValue + update:modelValue 컴포넌트 2
│       │   ├── ChildCompParam.vue           ← 🆕 2개 인수 다중 defineModel 컴포넌트
│       │   ├── ChildCompParam2.vue          ← 🆕 3개 인수 다중 defineModel 컴포넌트
│       │   ├── AlertBox.vue                 ← 🆕 기본 <slot /> 컨텐츠 배포 컴포넌트
│       │   ├── ChildExpose.vue              ← 🆕 defineExpose 자식 속성/메서드 노출 컴포넌트
│       │   └── LifeCycleHookComp.vue        ← 🆕 onMounted/onUpdated/onUnmounted 라이프사이클 컴포넌트
│       └── pages/                           ← 라우팅 페이지 컴포넌트
│           ├── index.vue                    ← 메인 홈
│           ├── BlogPage.vue                 ← 🆕 BlogPost Props 전달 부모 페이지
│           ├── BlogPageVFor.vue             ← 🆕 v-for 연동 BlogPost 페이지
│           ├── BlohPageEmit.vue             ← 🆕 BlogPostEmit 이벤트 수신 부모 페이지
│           ├── BlogPageEmitStandalone.vue   ← 🆕 개별 폰트 상태 제어 테스트 페이지
│           ├── ParentComp.vue               ← 🆕 ChildComp defineModel 연동 페이지
│           ├── ParentCompIn.vue             ← 🆕 ChildCompIn 전통적 v-model 연동 페이지
│           ├── ParentCompIn2.vue            ← 🆕 ChildCompIn2 전통적 v-model 연동 페이지
│           ├── ParentCompParam.vue          ← 🆕 ChildCompParam 다중 v-model 연동 페이지
│           ├── ParentCompParam2.vue         ← 🆕 ChildCompParam2 다중 v-model 연동 페이지
│           ├── ComponentSlot.vue            ← 🆕 AlertBox 슬롯 렌더링 부모 페이지
│           ├── YesNoQuestion.vue            ← 🆕 watch 반응형 감시 및 fetch API 연동 페이지
│           ├── TemplateRef.vue              ← 🆕 DOM/v-for 템플릿 참조(ref) 페이지
│           ├── ComponentRef.vue             ← 🆕 자식 인스턴스 참조 및 자식 메서드 호출 페이지
│           └── LifeCycleHookPage.vue        ← 🆕 컴포넌트 라이프사이클 훅 실행 시점 관찰 페이지
│
└── PracticeFile/                            ← 📱 [신규] Vuetify 3 인스타그램 레이아웃 클론 실습
    ├── assets/                              ← 로고 및 프로필 이미지
    │   ├── instagram_logo.png
    │   ├── leo_messi.jpg
    │   └── leo_messi_2.jpg
    ├── components/                          ← 인스타그램 UI 컴포넌트
    │   ├── MainNavUnf.vue                   ← 🆕 좌측 사이드바 Drawer (로고, 아바타, 피드 카운터, 메뉴)
    │   ├── AppBarUnf.vue                    ← 🆕 상단 앱바 (검색창, 새 글 작성 버튼, 알림/메시지 아이콘)
    │   ├── ProfilePageUnf.vue               ← 🆕 중앙 피드 카드 그리드 (Featured Stories)
    │   └── RightNavUnf.vue                  ← 🆕 우측 프로필 상세 Drawer (사진, 소개글, 위치)
    └── pages/
        └── Instagram.vue                    ← 🆕 인스타그램 메인 종합 레이아웃 엔트리
```

### 세부 설명 및 실습 내용

1. **`notes/` (이론 강의 교안 누적)**
   - [`2026_빅데이터프레임워크_4.pdf`](file:///C:/Users/AI-00/Desktop/하이테크_/2ndTerm/BigDataFramework/notes/2026_빅데이터프레임워크_4.pdf): 컴포넌트 통신(Props/Emit), 양방향 바인딩(`v-model`, `defineModel`), 슬롯(`Slot`), 감시자(`watch`), 템플릿 참조(`Template Refs`, `defineExpose`), 라이프사이클 훅(`Lifecycle Hooks`), Vuetify 종합 레이아웃.

2. **`daily_practice/260902_wed/` (날짜별 실습 및 정리 문서)**
   - [`2026-09-02.md`](file:///C:/Users/AI-00/Desktop/하이테크_/2ndTerm/BigDataFramework/daily_practice/260902_wed/2026-09-02.md):
     - **Props 전달**: `BlogPost.vue` ↔ `BlogPage.vue`, `BlogPageVFor.vue` (`defineProps`)
     - **커스텀 이벤트**: `BlogPostEmit.vue` ↔ `BlohPageEmit.vue` (`defineEmits`, `$emit`)
     - **컴포넌트 양방향 바인딩**: `ChildComp.vue` (`defineModel`), `ChildCompIn.vue` (`modelValue`/`update:modelValue`), `ChildCompParam.vue`/`ChildCompParam2.vue` (다중 인자 `defineModel`)
     - **슬롯(Slot)**: `AlertBox.vue` ↔ `ComponentSlot.vue` (`<slot />`)
     - **반응형 감시자**: `YesNoQuestion.vue` (`watch` + `fetch API`)
     - **템플릿 참조 & Expose**: `TemplateRef.vue` (`ref`), `ChildExpose.vue` ↔ `ComponentRef.vue` (`defineExpose`)
     - **라이프사이클 훅**: `LifeCycleHookComp.vue` ↔ `LifeCycleHookPage.vue` (`onMounted`, `onUpdated`, `onUnmounted`)
     - **인스타그램 UI 클론**: `Instagram.vue`, `MainNavUnf.vue`, `AppBarUnf.vue`, `ProfilePageUnf.vue`, `RightNavUnf.vue`
     - **핵심 문법 요약 표 (Key Takeaways)** 수록.

3. **`exam0902/` (Vue 3 + Vuetify 3 + TS 실습 프로젝트)**
   - 파일 기반 라우팅을 지원하는 Vuetify 3 템플릿 프로젝트를 통해 Vue 3 심화 문법 실습.

4. **`PracticeFile/` (Vuetify 3 인스타그램 레이아웃 클론)**
   - `<v-app>`, `<v-app-bar>`, `<v-navigation-drawer>`, `<v-avatar>`, `<v-card>`, `<v-img>` 등 Vuetify 3 핵심 레이아웃 컴포넌트를 활용한 반응형 소셜 미디어 웹 UI 구현.

---

## 🗓️ 2026-08-27 (목)

### 변경사항 요약
| 구분 | 내용 |
|------|------|
| ➕ 추가 | `notes/` - 2회차(`2026_빅데이터프레임워크_2.pdf`), 3회차(`2026_빅데이터프레임워크_3.pdf`) 강의 자료 추가 |
| ➕ 추가 | `scripts/` - 아카이빙/백업 유틸리티 스크립트(`backup.js`) 추가 |
| ➕ 추가 | `daily_practice/260827_thu/` - 당일 실습 코드(26개) 아카이빙 및 상세 실습 정리 문서(`2026-08-27.md`) 작성 |
| ➕ 추가 | `exam1/src/components/RefExam.vue` - `ref()` 기본 반응형 변수 실습 컴포넌트 추가 |
| ➕ 추가 | `exam1/src/components/RefSetupExam.vue` - `<script setup>` 구문과 `ref()` 연동 실습 컴포넌트 추가 |
| ➕ 추가 | `exam1/src/components/ReactiveFn.vue` - `reactive()` 객체 기반 반응형 상태 실습 컴포넌트 추가 |
| ➕ 추가 | `exam1/src/components/ReactiveReDef.vue` - `reactive()` 재할당 제약 및 반응성 유지 기법 실습 컴포넌트 추가 |
| ➕ 추가 | `exam1/src/components/DeepReactivity.vue` - 중첩 객체/배열 깊은 반응성(Deep Reactivity) 실습 컴포넌트 추가 |
| ➕ 추가 | `exam1/src/components/ReactiveDiff1.vue` - `ref` vs `reactive` 기본 동작 및 원시값/객체 비교 실습 컴포넌트 추가 |
| ➕ 추가 | `exam1/src/components/ReactiveDiff2.vue` - `ref` vs `reactive` 구조분해할당 및 참조 교체 비교 실습 컴포넌트 추가 |
| ➕ 추가 | `exam1/src/components/PseudoRef.vue` - `ref()` Getter/Setter 내부 동작 원리(Pseudo-ref) 실습 컴포넌트 추가 |
| ➕ 추가 | `exam1/src/components/NextTick.vue` - DOM 비동기 업데이트 큐와 `nextTick()` 실행 시점 실습 컴포넌트 추가 |
| 🔧 변경 | `exam1/src/App.vue` - 최신 실습 컴포넌트(`DeepReactivity.vue`) 연동으로 변경 |
| ➕ 추가 | `exam2/` - Vuetify 3 + Vue Router + TypeScript 기반의 두 번째 실습 프로젝트 신규 구성 |
| ➕ 추가 | `exam2/src/pages/ComputedProp.vue` - `computed()` 계산된 속성 기본 실습 컴포넌트 추가 |
| ➕ 추가 | `exam2/src/pages/CachedPropFunc.vue` - `computed` 캐싱 vs `methods` 호출 비교 실습 컴포넌트 추가 |
| ➕ 추가 | `exam2/src/pages/WritableComputed.vue` - Getter/Setter를 가진 Writable Computed 실습 컴포넌트 추가 |
| ➕ 추가 | `exam2/src/pages/VueList.vue` - `v-for` 배열 목록 렌더링 실습 컴포넌트 추가 |
| ➕ 추가 | `exam2/src/pages/TodoList.vue` - `v-for` 기반 Todo 추가/삭제 반응성 실습 컴포넌트 추가 |
| ➕ 추가 | `exam2/src/pages/ClassBind.vue` - `:class` 객체 구문 동적 클래스 바인딩 실습 컴포넌트 추가 |
| ➕ 추가 | `exam2/src/pages/ArrayClassBind.vue` - `:class` 배열 구문 및 삼항 연산자 바인딩 실습 컴포넌트 추가 |
| ➕ 추가 | `exam2/src/pages/ClassBindComponent.vue` - 컴포넌트 루트 엘리먼트 클래스 상속 및 바인딩 실습 컴포넌트 추가 |
| ➕ 추가 | `exam2/src/pages/StyleBind.vue` - `:style` 인라인 스타일 객체 및 배열 바인딩 실습 컴포넌트 추가 |
| ➕ 추가 | `exam2/src/pages/TextFormBind.vue` - `v-model` 단일행/다중행(textarea) 텍스트 폼 바인딩 실습 컴포넌트 추가 |
| ➕ 추가 | `exam2/src/pages/CheckboxFormBind.vue` - `v-model` 단일(불리언) 및 다중(배열) 체크박스 바인딩 실습 컴포넌트 추가 |
| ➕ 추가 | `exam2/src/pages/RadioSelectFormBind_2.vue` - `v-model` 라디오 버튼 및 드롭다운 셀렉트 박스 바인딩 실습 컴포넌트 추가 |
| ➕ 추가 | `exam2/src/pages/VTextFields.vue` - Vuetify `v-text-field` 폼 컴포넌트 바인딩 실습 1 추가 |
| ➕ 추가 | `exam2/src/pages/VTextFields_2.vue` - Vuetify `v-text-field` 폼 컴포넌트 바인딩 실습 2 추가 |

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
│   ├── 2026_빅데이터프레임워크_1.pdf         ← 1회차 수업 PDF 교안
│   ├── 2026_빅데이터프레임워크_2.pdf         ← 2회차 수업 PDF 교안 (Vue 3 반응성 시스템)
│   └── 2026_빅데이터프레임워크_3.pdf         ← 3회차 수업 PDF 교안 (Computed/Watch, 폼 바인딩, Vuetify 3)
│
├── scripts/                                 ← 🛠️ 워크스페이스 관리 및 자동화 스크립트
│   └── backup.js                            ← 아카이빙/백업 유틸리티 스크립트
│
├── daily_practice/                          ← 📂 날짜별 수업 실습 아카이브
│   ├── 260821_F/                            ← 🧪 8월 21일 실습 모음
│   │   ├── 2026-08-21.md                    ← 📝 당일 실습 코드 분석 및 컴포넌트별 정리 문서
│   │   ├── test.js                          ← JS 기초 테스트
│   │   └── test1.js                         ← JS 기초 테스트 2
│   └── 260827_thu/                          ← 🧪 8월 27일 실습 모음
│       ├── 2026-08-27.md                    ← 📝 당일 실습 코드 분석 및 컴포넌트별 상세 정리 문서
│       └── *.vue                            ← 당일 실습 .vue 컴포넌트 (총 26개 파일)
│
├── exam1/                                   ← 🛠️ Vue 3 + Vite 반응성 심화 실습 프로젝트
│   ├── index.html                           ← HTML 엔트리 포인트
│   ├── package.json                         ← 프로젝트 의존성 및 스크립트 설정
│   ├── package-lock.json
│   ├── jsconfig.json                        ← JS 프로젝트 설정
│   ├── vite.config.js                       ← Vite 번들러 설정
│   ├── README.md                            ← 프로젝트 안내
│   ├── node_modules/                        ← 프로젝트 종속성 (빌드 모듈)
│   ├── public/
│   │   └── favicon.ico                      ← 파비콘
│   └── src/
│       ├── main.js                          ← 앱 엔트리 포인트 (createApp)
│       ├── App.vue                          ← 메인 루트 컴포넌트 (DeepReactivity 연동)
│       ├── App copy.vue                     ← 루트 컴포넌트 백업본
│       ├── ButtonCounter.vue                ← 카운터 버튼 컴포넌트
│       ├── TextInterpolation.vue            ← 텍스트 보간법 컴포넌트
│       ├── assets/                          ← 정적 리소스 (CSS, 로고 등)
│       │   ├── base.css
│       │   ├── main.css
│       │   └── logo.svg
│       └── components/                      ← Vue 컴포넌트
│           ├── RawHTML.vue                  ← 원시 HTML 렌더링 실습
│           ├── AttrBind1.vue                ← 속성 바인딩 기본 (v-bind, :)
│           ├── AttrBind2.vue                ← 불리언 속성 바인딩 (:disabled)
│           ├── AttrBind3.vue                ← 이미지 src 속성 바인딩
│           ├── AttrBind3_2.vue              ← 이벤트 기반 반응형 이미지 변경
│           ├── DynaAttr1.vue                ← 동적 인자 바인딩 (:[attributeName])
│           ├── DynaAttr2.vue                ← 다중 속성 객체 일괄 바인딩 (v-bind="obj")
│           ├── DynaAttr2_2.vue              ← v-html + 다중 속성 바인딩 응용 1
│           ├── DynaAttr2_2_1.vue            ← v-html + 다중 속성 바인딩 응용 2
│           ├── JSExpr.vue                   ← 템플릿 내 JS 표현식 평가
│           ├── CondRender.vue               ← 조건부 렌더링 기본 (v-if vs v-show)
│           ├── CondRender2.vue              ← 다중 조건부 렌더링 (v-if, v-else-if, v-else)
│           ├── EventHandler.vue             ← 이벤트 핸들러 함수 정의 및 호출
│           ├── RefExam.vue                  ← 🆕 ref() 기본 반응형 상태 실습
│           ├── RefSetupExam.vue             ← 🆕 <script setup> + ref() 실습
│           ├── ReactiveFn.vue               ← 🆕 reactive() 객체 반응형 상태 실습
│           ├── ReactiveReDef.vue            ← 🆕 reactive() 재할당 제약 및 반응성 유지
│           ├── DeepReactivity.vue           ← 🆕 중첩 객체/배열 깊은 반응성 실습
│           ├── ReactiveDiff1.vue            ← 🆕 ref vs reactive 기본 동작 비교
│           ├── ReactiveDiff2.vue            ← 🆕 ref vs reactive 구조분해 및 참조 교체 비교
│           ├── PseudoRef.vue                ← 🆕 ref의 Getter/Setter 내부 동작 원리
│           ├── NextTick.vue                 ← 🆕 DOM 비동기 업데이트 큐와 nextTick()
│           ├── HelloWorld.vue
│           ├── TheWelcome.vue
│           ├── WelcomeItem.vue
│           └── icons/                       ← SVG 아이콘 컴포넌트 (5개)
│
└── exam2/                                   ← 🛠️ Vue 3 + Vuetify 3 + TS 실습 프로젝트
    ├── index.html                           ← HTML 엔트리 포인트
    ├── package.json                         ← 프로젝트 의존성 (Vuetify, Vue-Router, TS 등)
    ├── package-lock.json
    ├── tsconfig.json                        ← TS 기본 설정
    ├── tsconfig.app.json                    ← 앱 TS 설정
    ├── tsconfig.node.json                   ← Vite/Node TS 설정
    ├── vite.config.mts                      ← Vite 번들러 설정 (Vuetify 플러그인 포함)
    ├── eslint.config.js                     ← ESLint 규칙 설정
    ├── env.d.ts                             ← TS 환경 선언
    ├── AGENTS.md                            ← 에이전트 설정 문서
    ├── README.md                            ← 프로젝트 안내
    ├── node_modules/                        ← 프로젝트 종속성
    ├── .vscode/
    │   └── extensions.json                  ← 권장 VS Code 확장
    ├── public/
    │   ├── favicon.ico                      ← 파비콘
    │   └── layers.css                       ← 스타일 레이어 설정
    └── src/
        ├── main.ts                          ← 앱 엔트리 포인트 (Vuetify, Router 플러그인 등록)
        ├── App.vue                          ← 메인 루트 컴포넌트 (<v-app>, <router-view>)
        ├── App copy.vue                     ← 루트 컴포넌트 백업본
        ├── typed-router.d.ts                ← 타입 라우터 선언
        ├── assets/                          ← 정적 리소스 (로고 등)
        │   ├── logo.png
        │   └── logo.svg
        ├── components/                      ← 공용 컴포넌트
        │   ├── HelloWorld.vue               ← Vuetify 웰컴 컴포넌트
        │   ├── MyComponent.vue              ← 단일 루트 엘리먼트 테스트 컴포넌트
        │   ├── MyMultiComponent.vue         ← 다중 루트 엘리먼트(Fragment) 테스트 컴포넌트
        │   └── README.md
        ├── pages/                           ← 라우팅 페이지 및 핵심 문법 실습 컴포넌트
        │   ├── index.vue                    ← 메인 홈 (HelloWorld)
        │   ├── ComputedProp.vue             ← 🆕 computed() 계산된 속성 기본
        │   ├── CachedPropFunc.vue           ← 🆕 computed 캐싱 vs methods 호출 비교
        │   ├── WritableComputed.vue         ← 🆕 getter/setter를 가진 Writable Computed
        │   ├── VueList.vue                  ← 🆕 v-for 배열 목록 렌더링
        │   ├── TodoList.vue                 ← 🆕 v-for 기반 Todo 리스트 실습
        │   ├── ClassBind.vue                ← 🆕 :class 객체 구문 바인딩
        │   ├── ArrayClassBind.vue           ← 🆕 :class 배열 구문 및 조건 바인딩
        │   ├── ClassBindComponent.vue       ← 🆕 컴포넌트 루트 엘리먼트 클래스 바인딩
        │   ├── StyleBind.vue                ← 🆕 :style 인라인 스타일 객체/배열 바인딩
        │   ├── TextFormBind.vue             ← 🆕 v-model 텍스트/textarea 입력 바인딩
        │   ├── CheckboxFormBind.vue         ← 🆕 v-model 체크박스(단일/다중 배열) 바인딩
        │   ├── RadioSelectFormBind copy.vue ← 🆕 라디오/셀렉트 폼 바인딩 백업
        │   ├── RadioSelectFormBind_2.vue    ← 🆕 v-model 라디오/드롭다운 셀렉트 바인딩
        │   ├── VTextFields.vue              ← 🆕 Vuetify v-text-field 폼 바인딩 1
        │   └── VTextFields_2.vue            ← 🆕 Vuetify v-text-field 폼 바인딩 2
        ├── plugins/                         ← 플러그인 설정
        │   ├── index.ts                     ← 플러그인 통합 등록 진입점
        │   ├── vuetify.ts                   ← Vuetify 인스턴스 생성 및 테마/아이콘 설정
        │   └── README.md
        ├── router/                          ← 라우터 설정
        │   └── index.ts                     ← Vue Router 인스턴스 및 라우팅 설정
        └── styles/                          ← 스타일 설정
            ├── settings.scss                ← Vuetify SASS 변수 커스터마이징
            └── README.md
```

### 세부 설명 및 실습 내용

1. **`notes/` (이론 강의 교안 누적)**
   - [`2026_빅데이터프레임워크_2.pdf`](file:///C:/Users/AI-00/Desktop/하이테크_/2ndTerm/BigDataFramework/notes/2026_빅데이터프레임워크_2.pdf): Vue 3 반응성(Reactivity) 원리, `ref` vs `reactive`, 프록시 기반 상태 추적, `nextTick()`.
   - [`2026_빅데이터프레임워크_3.pdf`](file:///C:/Users/AI-00/Desktop/하이테크_/2ndTerm/BigDataFramework/notes/2026_빅데이터프레임워크_3.pdf): `computed` 계산된 속성, 클래스 및 스타일 바인딩, `v-for` 목록 렌더링, `v-model` 폼 바인딩, Vuetify 3 UI 라이브러리 기초.

2. **`scripts/` (워크스페이스 관리 스크립트)**
   - [`backup.js`](file:///C:/Users/AI-00/Desktop/하이테크_/2ndTerm/BigDataFramework/scripts/backup.js): 일별 실습 코드 백업 및 아카이빙을 위한 자동화 스크립트.

3. **`exam1/` (Vue 3 반응성 시스템 심화 실습)**
   - **`RefExam.vue` / `RefSetupExam.vue`**: 원시값/객체 모두 감쌀 수 있는 `ref()` 사용법 및 `<script setup>`에서의 자동 언래핑(`unref`) 실습.
   - **`ReactiveFn.vue` / `ReactiveReDef.vue`**: `reactive()`를 통한 객체 반응형 상태 생성, 재할당 시 반응성 상실 문제와 객체 속성 갱신을 통한 해결 기법.
   - **`DeepReactivity.vue`**: 중첩 객체 및 배열 내부 변경 시에도 트리거되는 깊은 반응성(Deep Reactivity) 검증.
   - **`ReactiveDiff1.vue` / `ReactiveDiff2.vue`**: `ref` vs `reactive`의 타입 제약, 구조 분해 할당(Destructuring) 시 반응성 보존 여부 비교.
   - **`PseudoRef.vue`**: Vue 내부의 `ref`가 getter/setter 객체 형태로 동작하는 메커니즘 분석.
   - **`NextTick.vue`**: 상태 변경 후 비동기로 일괄 처리되는 DOM 렌더링 큐와 `nextTick()`을 이용한 업데이트 직후 DOM 접근 실습.

4. **`exam2/` (Vue 3 + Vuetify 3 + Vue Router + TypeScript 신규 프로젝트 구성 및 실습)**
   - **Computed 속성**:
     - `ComputedProp.vue`: 종속 대상 반응형 변수 변경 시 자동 재계산되는 기본 `computed()`.
     - `CachedPropFunc.vue`: 의존성 변경 시에만 재계산되는 Computed 캐싱과 매번 재실행되는 Method 호출의 성능/동작 비교.
     - `WritableComputed.vue`: get/set 접근자를 정의하여 양방향 읽기/쓰기가 가능한 계산된 속성 실습.
   - **목록 렌더링 & 동적 바인딩**:
     - `VueList.vue` / `TodoList.vue`: `v-for`를 이용한 배열 순회 렌더링 및 동적 항목 추가/삭제.
     - `ClassBind.vue` / `ArrayClassBind.vue`: `:class`에 객체(`{ active: isActive }`) 및 배열(`[classA, classB]`) 형태의 동적 클래스 바인딩.
     - `ClassBindComponent.vue`: 자식 컴포넌트(`MyComponent`, `MyMultiComponent`)의 Root Element 및 `$attrs`에 클래스 상속 바인딩.
     - `StyleBind.vue`: `:style`을 활용한 camelCase/kebab-case 인라인 스타일 바인딩.
   - **폼 입력 바인딩 & Vuetify UI 컴포넌트**:
     - `TextFormBind.vue`: `v-model`을 활용한 text input 및 textarea 양방향 데이터 바인딩.
     - `CheckboxFormBind.vue`: 단일 체크박스(boolean) 및 다중 체크박스(배열 수집) 바인딩.
     - `RadioSelectFormBind_2.vue`: 라디오 버튼(`v-model`) 및 드롭다운 `<select>` 바인딩.
     - `VTextFields.vue` / `VTextFields_2.vue`: Vuetify 3의 `v-text-field` 컴포넌트와 Vue 3 반응형 상태 연동.

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
| ➕ 추가 | `exam1/src/components/AttrBind3.vue` - 이미지 `src` 속성 바인딩 컴포넌트 추가 |
| ➕ 추가 | `exam1/src/components/AttrBind3_2.vue` - 이벤트 기반 반응형 이미지 변경 컴포넌트 추가 |
| ➕ 추가 | `exam1/src/components/DynaAttr1.vue` - 동적 인자 바인딩(`:[attributeName]`) 컴포넌트 추가 |
| ➕ 추가 | `exam1/src/components/DynaAttr2.vue` - 다중 속성 객체 일괄 바인딩(`v-bind="object"`) 컴포넌트 추가 |
| ➕ 추가 | `exam1/src/components/DynaAttr2_2.vue` - `v-html` + 다중 속성 객체 바인딩 응용 1 추가 |
| ➕ 추가 | `exam1/src/components/DynaAttr2_2_1.vue` - `v-html` + 다중 속성 객체 바인딩 응용 2 추가 |
| ➕ 추가 | `exam1/src/components/JSExpr.vue` - 템플릿 내 자바스크립트 표현식 평가 컴포넌트 추가 |
| ➕ 추가 | `exam1/src/components/CondRender.vue` - 조건부 렌더링 기본(`v-if` vs `v-show`) 컴포넌트 추가 |
| ➕ 추가 | `exam1/src/components/CondRender2.vue` - 다중 조건부 렌더링(`v-if`, `v-else-if`, `v-else`) 컴포넌트 추가 |
| ➕ 추가 | `exam1/src/components/EventHandler.vue` - 이벤트 핸들러 함수 정의 및 호출 컴포넌트 추가 |
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
        ├── App.vue                          ← 메인 루트 컴포넌트 (CondRender2 연동)
        ├── App copy.vue                     ← 루트 컴포넌트 백업본
        ├── ButtonCounter.vue                ← 카운터 버튼 컴포넌트
        ├── TextInterpolation.vue            ← 텍스트 보간법 컴포넌트
        ├── assets/                          ← 정적 리소스 (CSS, 로고 등)
        │   ├── base.css
        │   ├── main.css
        │   └── logo.svg
        └── components/                      ← Vue 컴포넌트
            ├── RawHTML.vue                  ← 원시 HTML 렌더링 실습 컴포넌트
            ├── AttrBind1.vue                ← 속성 바인딩 기본(v-bind, :) 실습 컴포넌트
            ├── AttrBind2.vue                ← 불리언 속성 바인딩(:disabled) 실습 컴포넌트
            ├── AttrBind3.vue                ← 이미지 src 속성 바인딩 실습 컴포넌트
            ├── AttrBind3_2.vue              ← 이벤트 기반 반응형 이미지 변경 컴포넌트
            ├── DynaAttr1.vue                ← 동적 인자 바인딩(:[attributeName]) 실습 컴포넌트
            ├── DynaAttr2.vue                ← 다중 속성 객체 일괄 바인딩(v-bind="obj") 컴포넌트
            ├── DynaAttr2_2.vue              ← 🆕 v-html + 다중 속성 바인딩 응용 1
            ├── DynaAttr2_2_1.vue            ← 🆕 v-html + 다중 속성 바인딩 응용 2
            ├── JSExpr.vue                   ← 🆕 템플릿 내 JS 표현식 평가 컴포넌트
            ├── CondRender.vue               ← 🆕 조건부 렌더링 기본(v-if vs v-show)
            ├── CondRender2.vue              ← 🆕 다중 조건부 렌더링(v-if, v-else-if, v-else)
            ├── EventHandler.vue             ← 🆕 이벤트 핸들러 함수 정의 및 호출
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
     - 실습 6: 이미지 속성 바인딩 (`AttrBind3.vue` ↔ `App.vue`, `:src`)
     - 실습 7: 반응형 이미지 변경 (`AttrBind3_2.vue` ↔ `App.vue`, `@click`, `.value`)
     - 실습 8: 동적 인자 바인딩 (`DynaAttr1.vue` ↔ `App.vue`, `:[attributeName]`)
     - 실습 9: 다중 속성 객체 일괄 바인딩 (`DynaAttr2.vue` ↔ `App.vue`, `v-bind="obj"`)
     - 실습 10: v-html + 다중 속성 바인딩 1 (`DynaAttr2_2.vue` ↔ `App.vue`)
     - 실습 11: v-html + 다중 속성 바인딩 2 (`DynaAttr2_2_1.vue` ↔ `App.vue`)
     - 실습 12: 템플릿 내 JS 표현식 평가 (`JSExpr.vue` ↔ `App.vue`)
     - 실습 13: 조건부 렌더링 기본 (`CondRender.vue` ↔ `App.vue`, `v-if` vs `v-show`)
     - 실습 14: 다중 조건부 렌더링 (`CondRender2.vue` ↔ `App.vue`, `v-if`/`v-else-if`/`v-else`)
     - 실습 15: 이벤트 핸들러 함수 정의 (`EventHandler.vue` ↔ `App.vue`)
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
