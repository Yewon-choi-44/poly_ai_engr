# 👁️ ComputerVisionLab 수업 및 실습 관리 지침

이 워크스페이스는 컴퓨터비전실습 과목(CNN, YOLO, OpenCV, 공정데이터분석, RAG 등)의 수업 내용, 실습 코드(.py/.ipynb), 학습 모델, 데이터셋을 기록하고 체계적으로 관리하는 공간입니다. 이미 `README.md`(실습·학습 일지)와 `DirectoryStructure.md`(디렉토리 구조 누적 기록)라는 두 문서로 관리 체계가 잡혀 있으며, 이 파일은 그 체계를 유지·운영하기 위한 AI 행동 지침입니다.

---

## 0. 작업 시작 전 최우선 점검 — `.gitignore` 및 저장소 범위

어떤 작업이든 시작하기 전에 **가장 먼저** 다음 두 가지를 점검한다.

- **`.gitignore` 최신 상태 확인**: 새로 생긴 산출물(모델 가중치, 데이터셋 폴더, 압축파일, `__pycache__` 등)이 무시 목록에 없다면 즉시 추가한다. 현재 `.gitignore`는 `data/`, `notes/`, `synthetic_capacitors/`, 모델 가중치(`*.pt`, `*.pth`, `*.ckpt`, `*.onnx`, `*.h5` 등), 압축파일(`*.zip`, `*.tar.gz`), `__pycache__/`, 가상환경(`.venv/`, `venv/`)을 이미 추적 제외하고 있다.
- **저장소 범위 확인**: 이 폴더의 `.git`은 `ComputerVisionLab/`이나 `2ndTerm/`이 아니라 **훨씬 상위인 `C:\Users\AI-00\Desktop\하이테크_`**에 있다(`git rev-parse --show-toplevel`로 확인). 즉 `2ndTerm/` 아래의 `ServerProgramming`, `AIFramework`, `AISystemDevelopmentandOperationsPracticum`뿐 아니라, `하이테크_` 바로 아래의 `AI_DataPreprocessing`, `Database_SQL`, `기계학습프로그래밍`, `웹프로그래밍`, `자바프로그래밍` 등 **다른 학기·다른 과목 폴더까지 전부 같은 git 저장소를 공유**한다. 따라서:
  - `git status`/`git add`/`git commit` 등은 항상 `ComputerVisionLab/` 경로로 범위를 제한한다 (예: `git status -- .`, `git add ComputerVisionLab/...`).
  - 다른 과목 폴더에 있는 변경 사항(예: `ServerProgramming/...`, `자바프로그래밍/...`)은 이 워크스페이스 작업과 무관하므로 손대거나 커밋에 포함하지 않는다.

---

## 1. 프로젝트 구조 원칙

이 워크스페이스에는 현재 다음과 같은 최상위 디렉토리가 존재합니다.

| 폴더/파일 | 역할 |
| :--- | :--- |
| `0820_Thu/` | 1주차 — CNN 구조 이해 및 전이학습(Transfer Learning) 실습 |
| `0825_Tus/` | 2주차 — YOLOv8 Object Detection & Instance Segmentation 실습 |
| `0907_Mon/` | 공정데이터분석 및 최적화 실습 |
| `0920Th/` | RAG(Retrieval-Augmented Generation) 실습 |
| `0921_Mo/` | Python 클래스(OOP) 기초 실습 (클래스 변수, 네임스페이스 등) |
| `HW/` | Kuffers 데이터셋 분류 과제 스크립트 및 결과 시각화 |
| `notes/` | 수업 교안·이론 강의 자료 (PDF, Git 미추적) |
| `data/` | 학습/평가용 데이터셋 (MNIST, FashionMNIST, kuffers, YOLO 데이터셋 등, Git 미추적) |
| `synthetic_capacitors/` | 합성 커패시터 결함 검출 이미지 데이터셋 (Defective/Good, Git 미추적) |
| `.vscode/` | VSCode/Python 환경 설정 |
| `README.md` | 프로젝트 개요 + 날짜별 실습·학습 일지 (최상단 누적) |
| `DirectoryStructure.md` | 디렉토리 구조 변동 히스토리 (날짜별 전체 트리 스냅샷 누적) |

새로운 실습 날짜 폴더가 추가될 때는 위 표에 반드시 항목을 추가한다.

---

## 2. 일별 실습 기록 원칙

이 워크스페이스는 Spring_2026처럼 날짜별로 별도의 정리 문서(`daily_practice/*.md`)를 만드는 대신, **`README.md` 안의 "실습 및 학습 일지" 섹션에 날짜별 항목을 최상단에 추가**하고, 구조가 바뀔 때마다 **`DirectoryStructure.md`에 전체 트리 스냅샷을 새 날짜 블록으로 누적**하는 방식을 이미 쓰고 있다. 새 문서 체계를 만들지 말고 이 기존 체계를 그대로 따른다.

### 2-1. `README.md` 갱신 — 실습 일지

`README.md`에 이미 정의된 템플릿(파일 하단 "수업 일지 작성 템플릿" 참고)을 그대로 사용해 "실습 및 학습 일지" 섹션 최상단에 추가한다.

```markdown
### YYYY-MM-DD
- **수업 주제**: [수업 주제 및 핵심 키워드]
- **주요 작업 내용**:
  - [작업 요약 1]
  - [작업 요약 2]
- **추가/수정된 파일**:
  - `파일명.py` (또는 `.ipynb`): 파일의 역할 및 구현 내용
  - `data/...`: 새로 사용된 데이터셋
  - `*.pth` / `*.pt`: 학습/저장된 모델 가중치
```

### 2-2. `DirectoryStructure.md` 갱신 — 구조 히스토리

디렉토리 구조에 변동이 생길 때마다(새 날짜 폴더 추가, 파일 대규모 이동 등) `## 📅 [YYYY-MM-DD] - 제목` 형식의 새 블록을 **최상단에** 추가하고, 그 시점의 전체 디렉토리 트리(주석 포함)와 "주요 변경 세부사항"을 함께 기록한다. 기존 블록은 삭제하거나 덮어쓰지 않고 그대로 누적 보존한다.

---

## 3. 데이터/모델 파일 취급 원칙

- `data/`, `notes/`, `synthetic_capacitors/`와 모델 가중치 파일(`*.pt`, `*.pth`, `*.onnx` 등)은 `.gitignore`로 Git 추적에서 제외되어 있다. 새로운 종류의 대용량 산출물(예: 새 데이터셋 형식, 새 가중치 확장자)이 생기면 0번 원칙에 따라 `.gitignore`에 반영부터 한다.
- `README.md`/`DirectoryStructure.md`에 파일을 기록할 때도 대용량 바이너리는 존재 사실과 크기/개수만 기록하고, 내용 자체를 문서에 옮기지 않는다(예: "Defective_000.png ~ 099.png, 100장" 형태).

---

## 4. Git 커밋 컨벤션

이 저장소에서 실제로 쓰인 커밋 메시지 스타일을 따른다: `[N주차] YYMMDD(요일) 설명` 형식.

```
[2주차] 20260826(수) README, DS.md updated
[2주차] 20260826(수) kuffers, Yolo 과제 추가
[260820(목)] mnist_cnn 실습
```

커밋 전 항상 `git status -- .`로 `ComputerVisionLab/` 범위만 확인하고, 다른 과목 폴더의 변경 사항이 섞여 들어가지 않았는지 점검한다.

---

## 5. AI 어시스턴트 행동 원칙

- **역할**: 실습 코드(.py, .ipynb)는 직접 작성·수정하지 않는다. AI의 역할은 `README.md`/`DirectoryStructure.md` 갱신, 구조 점검, `.gitignore` 관리 등 **기록과 정리**로 한정한다. (Spring_2026 워크스페이스와 동일한 원칙을 적용한 것이며, 이 저장소에서 다르게 운영하고 싶다면 언제든 조정 가능하다.)
- **새 실습 발견 시**: `README.md`/`DirectoryStructure.md`에 아직 반영되지 않은 날짜 폴더나 파일을 발견하면, 임의로 코드를 고치지 않고 우선 사용자에게 알리거나(또는 명시적으로 "정리해달라"는 요청이 있을 때) 기존 템플릿에 맞춰 기록한다.
- **보안**: API 키, 인증 정보 등 민감 정보가 포함된 파일은 절대 Git에 커밋하지 않는다.
