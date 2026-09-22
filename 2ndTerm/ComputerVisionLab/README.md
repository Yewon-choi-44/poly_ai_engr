# 👁️ 컴퓨터비전실습 (Computer Vision Lab)

컴퓨터비전실습 과목의 수업 내용, 실습 코드, 학습 모델 및 데이터셋을 기록하고 체계적으로 관리하는 저장소입니다.

---

## 📁 디렉토리 구조 (Directory Structure)

> 💡 디렉토리 구조 변동 및 히스토리 관리는 [DirectoryStructure.md](file:///C:/Users/AI-00/Desktop/%ED%95%98%EC%9D%B4%ED%85%8C%ED%81%AC_/2ndTerm/ComputerVisionLab/DirectoryStructure.md)에서 누적식으로 기록됩니다.

```text
ComputerVisionLab/
├── .vscode/                                                  # VSCode 환경 설정
├── 0820_Thu/                                                 # 1주차 CNN 및 전이학습 실습 파일
├── 0825_Tus/                                                 # 2주차 YOLO Detection & Segmentation 실습 파일
├── 0907_Mon/                                                 # 반도체 공정데이터분석 및 최적화 실습 (SECOM)
├── 0920Th/                                                   # RAG(검색증강생성) 파이프라인 구축 실습
├── 0921_Mo/                                                  # Python 객체지향(OOP) 클래스 기초 실습
├── HW/                                                       # Kuffers 데이터셋 실습 및 과제 스크립트
├── notes/                                                    # 수업 교안 및 이론 강의 자료 (PDF)
├── data/                                                     # 이미지 데이터셋 (MNIST, FashionMNIST, kuffers, YOLO 등)
├── synthetic_capacitors/                                     # 합성 커패시터 결함 검출 데이터셋 (Defective/Good)
├── .gitignore                                                # Git 추적 제외 설정
├── AGENTS.md                                                 # AI 어시스턴트 행동 지침
├── README.md                                                 # 프로젝트 메인 개요 문서
└── DirectoryStructure.md                                     # 디렉토리 구조 누적 관리 문서
```

---

## 📅 실습 및 학습 일지 (Changelog)

### 2026-09-21
- **수업 주제**: Python 객체지향(OOP) 클래스 기초 — 생성자, 상속, 클래스 변수 vs 인스턴스 변수, 객체 간 협력
- **주요 작업 내용**:
  - 사칙연산 클래스(`FourCalc`)와 이를 상속한 `MoreCalc`로 생성자 오버라이딩, `super()` 호출 실습
  - 절차 지향과 객체 지향의 차이를 등굣길 예시로 설명하고, Java 클래스 문법과 Python 클래스 문법을 나란히 비교
  - `Student`/`Bus`/`Subway` 클래스로 서로 다른 객체가 메서드 호출을 통해 협력(메시지 전달)하는 구조 실습
  - `GameChar` 클래스로 클래스 변수(모든 인스턴스 공유)와 인스턴스 변수(`__dict__`로 확인)의 네임스페이스 차이 실습
  - `Account` 클래스로 클래스 변수(`cntAccount`, `uniqAccountNum`, `total`)를 활용한 계좌 시스템 예제 구현, `main.py`에서 랜덤 출금 시뮬레이션 실행
- **추가/수정된 파일**:
  - `0921_Mo/class_example.py`: 사칙연산 클래스 및 상속(`MoreCalc`) 실습
  - `0921_Mo/class_simple.py`: 절차지향/객체지향 비교 설명 + `Student`/`Bus`/`Subway` 협력 구조 실습
  - `0921_Mo/classNameSpace.py`: 클래스 변수 vs 인스턴스 변수 네임스페이스 실습 (`GameChar`)
  - `0921_Mo/classVarTest.py`: 클래스 변수 기반 `Account` 계좌 클래스 구현
  - `0921_Mo/main.py`: `Account` 클래스를 임포트해 랜덤 출금 시뮬레이션을 실행하는 데모 스크립트

### 2026-09-20
- **수업 주제**: RAG(Retrieval-Augmented Generation) 파이프라인 구축 — 문서 청킹부터 Multi-turn 응답까지
- **주요 작업 내용**:
  - `reportlab`으로 한글(나눔고딕) 마이크로LED 공정 매뉴얼 PDF를 코드로 직접 생성해 실습용 문서로 사용
  - `PyPDFLoader` + `RecursiveCharacterTextSplitter`(chunk_size=1000, overlap=200)로 문서 로드 및 청킹
  - `BAAI/bge-m3` HuggingFace 임베딩으로 청크를 벡터화하고 FAISS Vector DB 구축·저장, 유사도 검색(`similarity_search`) 테스트
  - 최신 LangChain LCEL 방식(`RunnableLambda` + `PromptTemplate` + Retriever)으로 단발성 RAG 체인 구성 — 구버전 `RetrievalQA`/`langchain.chains` 대신 직접 연결하는 방식으로 수정, API 키 없이도 동작하는 실습용 시뮬레이션 LLM(`PracticeSimulatedLLM`) 사용
  - 메타데이터(`equipment`, `doc_type`)를 청크에 부여해 필터링 검색 실습
  - 대화 이력을 파이썬 리스트로 직접 관리하는 Multi-turn RAG 구현 (구버전 `ConversationBufferMemory`/`ConversationalRetrievalChain` 대신)
  - 5개 질의로 전체 RAG 파이프라인 종합 성능(충실도·환각 방지·검색 품질) 검증
- **추가/수정된 파일**:
  - `0920Th/실습_RAG_ppt_수정본.ipynb`: RAG 파이프라인 실습 노트북 (PDF 생성 → 청킹 → FAISS → LCEL RAG → 메타데이터 필터링 → Multi-turn → 종합 검증)

### 2026-09-07
- **수업 주제**: 반도체 공정데이터분석 및 공정 최적화 — 불균형 데이터 처리, 모델 비교, SHAP 기반 원인 규명
- **주요 작업 내용**:
  - UCI SECOM 반도체 공정 데이터셋(센서 데이터 + Pass/Fail 라벨) 직접 로드, 결측률·불량 발생 시계열 EDA
  - RandomForest 특징 중요도(MDI) 기준으로 원본 센서 변수를 상위 50개로 차원 축소
  - `SMOTEENN`으로 학습 데이터의 클래스 불균형(정상/불량) 완화
  - RandomForest·XGBoost 학습 및 Recall/F1/ROC-AUC 비교 평가, 이후 LightGBM까지 포함한 "모델 3종 × 데이터셋 3종(Original/SMOTE/SMOTEENN)" 3x3 교차 실험 설계
  - SHAP(Summary/Waterfall/Dependence Plot)으로 불량 판정에 가장 크게 기여하는 변수와 그 방향성(임계값) 분석
  - SHAP으로 찾은 핵심 변수에 대해 3-Sigma 규칙 기반 SPC(X-bar 관리도)를 그려 이상치(Outlier) 시각화, 공정 개선 방향 도출
- **추가/수정된 파일**:
  - `0907_Mon/실습_공정데이터분석및최적화.ipynb`: SECOM 데이터 EDA → 피처 선택 → 불균형 처리 → 모델 비교 → SHAP 원인 규명 → SPC 관리도 전체 파이프라인 실습 노트북

### 2026-08-26
- **수업 주제**: 저장소 구조 개편, YOLO 실습 아카이빙 및 Kuffers 과제 정리
- **주요 작업 내용**:
  - 일자별 실습 폴더(`0820_Thu`, `0825_Tus`), 과제(`HW`), 교안(`notes`) 디렉토리 분리 및 체계화
  - YOLOv8 기반 Object Detection 및 Instance Segmentation 실습 자료 정리
  - Kuffers 결함 분류 과제 코드 및 결과 시각화 그래프 아카이빙
  - 디렉토리 구조 변동 사항 누적 관리 문서(`DirectoryStructure.md`) 신설
- **추가/수정된 파일**:
  - `0825_Tus/실습_yolo_detect.ipynb`, `0825_Tus/실습_YOLO_SEG.ipynb`: YOLO 탐지 및 인스턴스 세그멘테이션 실습 주피터 노트북
  - `HW/kuffers_cnn_hw*.py`, `HW/Own_ML_Class_kuffers.py`: Kuffers 데이터셋 분류 및 과제 스크립트
  - `notes/*.pdf`: 머신비전, 디스플레이/반도체 AI, 산업용 LLM 이론 PDF 교안 (총 7건)
  - `data/Custom Workflow Instance Segmentation.v1i.yolov8(-obb)/`: YOLOv8 세그멘테이션 및 OBB 데이터셋
  - `synthetic_capacitors/`: 커패시터 결함 검출용 합성 이미지 데이터셋 (`Defective/`, `Good/`)
  - `DirectoryStructure.md`: 디렉토리 구조 누적 관리 문서
  - `README.md`: 최신 디렉토리 개요 및 학습 일지 업데이트

### 2026-08-20
- **수업 주제**: CNN 구조 이해 및 전이학습(Transfer Learning) 기초 실습
- **추가 및 업데이트된 파일**:
  - `실습_CNN_Transfer_수정_ipynb의_사본.ipynb`: CNN 모델 실습 및 전이학습 예제 주피터 노트북
  - `data/FashionMNIST/`: 실습 진행 중 추가 다운로드된 Fashion-MNIST 의류 데이터셋
  - `mnist_cnn.pt`, `mnist_cnn.pth`: CNN 학습 실행 결과로 생성 및 업데이트된 가중치 모델 파일
  - `README.md`: 전체 디렉토리 구조 최신화 및 일자별 히스토리 아카이빙 체계 구축

---

## 📝 수업 일지 작성 템플릿 (Template)

새로운 수업이나 실습이 있을 때마다 아래 템플릿을 복사하여 최상단에 추가해 주세요:

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
