# 📁 디렉토리 구조 관리 대장 (Directory Structure Log)

본 문서는 `ComputerVisionLab` 저장소의 디렉토리 구조 변동 사항 및 파일 구성 히스토리를 누적식으로 기록·관리하는 문서입니다.

---

## 📅 [2026-09-21] - 공정데이터분석·RAG·OOP 실습 3건 아카이빙 및 AGENTS.md 신설

2026-09-07, 2026-09-20, 2026-09-21에 진행된 실습 3건(`0907_Mon`, `0920Th`, `0921_Mo`)이 기존 디렉토리 구조 문서에 반영되지 않은 채 누적되어 있어, 이번에 한꺼번에 정리했습니다. 아울러 Spring_2026 저장소의 `AGENTS.md`를 참고해 이 저장소에도 동일한 이름의 AI 행동 지침 파일을 신설했습니다.

### 🌳 현재 전체 디렉토리 트리 (Current Tree)

```text
ComputerVisionLab/
├── .vscode/                                                  # VSCode 환경 설정
│   └── settings.json
├── 0820_Thu/                                                 # [2026-08-20] 1주차 CNN 및 전이학습 실습
│   ├── Own_ML_Class.py                                       # 커스텀 머신러닝/딥러닝 유틸리티 및 모델 클래스
│   ├── mnist_cnn.py                                          # MNIST CNN 모델 학습 및 평가 스크립트
│   ├── 실습_CNN_Transfer_수정_ipynb의_사본.ipynb                 # CNN 및 전이학습 실습 주피터 노트북
│   ├── mnist_clf.pth                                         # 학습된 분류기 가중치 모델
│   ├── mnist_cnn.pt                                          # MNIST CNN 체크포인트 모델
│   └── mnist_cnn.pth                                         # MNIST CNN 가중치 모델
├── 0825_Tus/                                                 # [2026-08-25] 2주차 YOLO Detection & Segmentation 실습
│   ├── Custom Workflow Instance Segmentation.v1i.yolov8.zip     # YOLOv8 Instance Segmentation 데이터셋 (압축본)
│   ├── Custom Workflow Instance Segmentation.v1i.yolov8-obb.zip # YOLOv8 OBB(Oriented Bounding Box) 데이터셋 (압축본)
│   ├── 실습_yolo_detect.ipynb                                   # YOLO 객체 탐지(Object Detection) 실습 노트북
│   └── 실습_YOLO_SEG.ipynb                                      # YOLO 인스턴스 세그멘테이션 실습 노트북
├── 0907_Mon/                                                 # [2026-09-07] 반도체 공정데이터분석 및 최적화 실습
│   └── 실습_공정데이터분석및최적화.ipynb                            # SECOM EDA → 피처선택 → SMOTEENN → 모델비교 → SHAP → SPC 관리도
├── 0920Th/                                                   # [2026-09-20] RAG 파이프라인 구축 실습
│   └── 실습_RAG_ppt_수정본.ipynb                                 # PDF 생성 → 청킹 → FAISS → LCEL RAG → 메타데이터 필터링 → Multi-turn
├── 0921_Mo/                                                  # [2026-09-21] Python 객체지향(OOP) 클래스 기초 실습
│   ├── __pycache__/                                          # Python 바이트코드 캐시 (Git 미추적)
│   ├── class_example.py                                      # 사칙연산 클래스 및 상속(MoreCalc) 실습
│   ├── class_simple.py                                       # 절차지향/객체지향 비교 + Student/Bus/Subway 협력 구조 실습
│   ├── classNameSpace.py                                     # 클래스 변수 vs 인스턴스 변수 네임스페이스 실습 (GameChar)
│   ├── classVarTest.py                                       # 클래스 변수 기반 Account 계좌 클래스
│   └── main.py                                               # Account 클래스 임포트, 랜덤 출금 시뮬레이션 데모
├── HW/                                                       # 과제 및 실습 과제 스크립트
│   ├── Own_ML_Class_kuffers.py                               # Kuffers 데이터셋 분류용 커스텀 클래스
│   ├── kuffers_cnn.py                                        # Kuffers CNN 기본 학습 스크립트
│   ├── kuffers_cnn_hw.py                                     # Kuffers 과제 구현 스크립트 (기본)
│   ├── kuffers_cnn_hw_1.py                                   # Kuffers 과제 구현 스크립트 (버전 1)
│   ├── kuffers_cnn_hw_2.py                                   # Kuffers 과제 구현 스크립트 (버전 2)
│   ├── Figure_1.png                                          # 과제 결과 시각화 그래프 1
│   └── Figure_1_1.png                                        # 과제 결과 시각화 그래프 2
├── notes/                                                    # 수업 교안 및 이론 강의 자료 (PDF)
│   ├── 0.Introduction.pdf                                    # 강의 소개
│   ├── 1.opencv_기초.pdf                                       # OpenCV 기초 강의 자료
│   ├── 1.디스플레이·반도체_공정을_위한_머신비전과_딥러닝_AI_Part_1_수정.pdf
│   ├── 1.디스플레이·반도체_공정을_위한_머신비전과_딥러닝_AI_Part_1_수정-복사.pdf
│   ├── 2.opencv-그래픽기능.pdf                                   # OpenCV 그래픽 기능 강의 자료
│   ├── 2.디스플레이·반도체_공정을_위한_머신비전과_딥러닝_AI_Part_2_수정.pdf
│   ├── 2.디스플레이·반도체_공정을_위한_머신비전과_딥러닝_AI_Part_2_수정-복사.pdf
│   ├── 3.반도체_공정_데이터_분석과_불량_원인_규명_EDA·RandomForest·XGBoost·SHAP·SMOTE_수정.pdf
│   ├── 3.영상처리_color_histo.pdf
│   ├── 3-1.영상처리_이진화.pdf
│   ├── 3-2.영상처리_모폴로지.pdf
│   ├── 3-3.영상처리_Edge.pdf
│   ├── 4.산업용_LLM_기초이론_및_제조업_적용사례_수정.pdf
│   └── 5.LLM_활용_실무_Part_1_RAG_시스템_원리와_구축.pdf
├── data/                                                     # 학습 및 평가 데이터셋 모음
│   ├── MNIST/                                                # MNIST 손글씨 데이터셋
│   ├── FashionMNIST/                                         # Fashion-MNIST 의류 데이터셋
│   ├── kuffers/                                              # Kuffers 불량 검출 데이터셋 (TrainSet/TestSet/TestAll)
│   ├── Custom Workflow Instance Segmentation.v1i.yolov8/     # YOLOv8 Instance Segmentation 데이터셋 (train/valid/test)
│   └── Custom Workflow Instance Segmentation.v1i.yolov8-obb/ # YOLOv8 OBB 데이터셋 (train/valid/test)
├── synthetic_capacitors/                                     # 합성 커패시터 결함 검출 데이터셋
│   ├── Defective/                                            # 불량 커패시터 이미지 (Defective_000.png ~ 099.png, 100장)
│   └── Good/                                                 # 정상 커패시터 이미지 (Good_000.png ~ 099.png, 100장)
├── .gitignore                                                # Git 추적 제외 설정
├── AGENTS.md                                                 # AI 어시스턴트 행동 지침 (신규)
├── README.md                                                 # 프로젝트 메인 개요 문서
└── DirectoryStructure.md                                     # 디렉토리 구조 누적 관리 문서 (본 파일)
```

### 🔄 주요 변경 세부사항 (Changelog Detail)
- **`0907_Mon/` 아카이빙**: SECOM 반도체 공정 데이터 기반 불량 예측·원인분석 실습(2026-09-07 진행분)을 뒤늦게 구조 문서에 반영. EDA → RandomForest 피처 선택 → SMOTEENN 불균형 처리 → 모델 비교(RandomForest/XGBoost/LightGBM) → SHAP 원인 규명 → SPC 관리도까지 전체 파이프라인이 노트북 하나에 담겨 있음.
- **`0920Th/` 아카이빙**: RAG 파이프라인 구축 실습(2026-09-20 진행분) 반영. 문서 생성 → 청킹 → FAISS 임베딩 → LCEL 방식 RAG → 메타데이터 필터링 → Multi-turn 대화까지 단계별로 구성.
- **`0921_Mo/` 아카이빙**: Python 객체지향(OOP) 클래스 기초 실습(2026-09-21 진행분) 반영. 상속, 클래스 변수/인스턴스 변수, 객체 간 협력 구조를 다루는 스크립트 5개.
- **`AGENTS.md` 신설**: `D:\Spring_2026\AGENTS.md`를 참고해 이 저장소 전용 AI 행동 지침 파일을 작성. 이 저장소의 기존 관례(README.md 학습일지 + DirectoryStructure.md 누적 기록)를 그대로 공식화했고, `.git`이 상위 `2ndTerm/` 디렉토리에 있어 다른 과목 폴더와 저장소를 공유한다는 점을 반영해 git 작업 범위 제한 원칙을 추가.
- **`README.md` 갱신**: 최상단 디렉토리 구조 개요에 `0907_Mon`, `0920Th`, `0921_Mo`, `AGENTS.md`를 추가하고, "실습 및 학습 일지"에 세 날짜(2026-09-07, 2026-09-20, 2026-09-21) 항목을 신설.

---

## 📅 [2026-08-26] - 디렉토리 구조 개편 및 YOLO·과제·교안 아카이빙

기존 루트 디렉토리에 모여 있던 실습 파일들을 일자별 폴더(`0820_Thu`, `0825_Tus`), 과제(`HW`), 교안(`notes`) 등으로 분류하여 체계화하였으며, 신규 실습(YOLO Detection/Segmentation) 및 합성 커패시터 데이터셋이 추가되었습니다.

### 🌳 현재 전체 디렉토리 트리 (Current Tree)

```text
ComputerVisionLab/
├── .vscode/                                                  # VSCode 환경 설정
│   └── settings.json
├── 0820_Thu/                                                 # [2026-08-20] 1주차 CNN 및 전이학습 실습
│   ├── Own_ML_Class.py                                       # 커스텀 머신러닝/딥러닝 유틸리티 및 모델 클래스
│   ├── mnist_cnn.py                                          # MNIST CNN 모델 학습 및 평가 스크립트
│   ├── 실습_CNN_Transfer_수정_ipynb의_사본.ipynb                 # CNN 및 전이학습 실습 주피터 노트북
│   ├── mnist_clf.pth                                         # 학습된 분류기 가중치 모델
│   ├── mnist_cnn.pt                                          # MNIST CNN 체크포인트 모델
│   └── mnist_cnn.pth                                         # MNIST CNN 가중치 모델
├── 0825_Tus/                                                 # [2026-08-25] 2주차 YOLO Detection & Segmentation 실습
│   ├── Custom Workflow Instance Segmentation.v1i.yolov8.zip     # YOLOv8 Instance Segmentation 데이터셋 (압축본)
│   ├── Custom Workflow Instance Segmentation.v1i.yolov8-obb.zip # YOLOv8 OBB(Oriented Bounding Box) 데이터셋 (압축본)
│   ├── 실습_yolo_detect.ipynb                                   # YOLO 객체 탐지(Object Detection) 실습 노트북
│   └── 실습_YOLO_SEG.ipynb                                      # YOLO 인스턴스 세그멘테이션 실습 노트북
├── HW/                                                       # 과제 및 실습 과제 스크립트
│   ├── Own_ML_Class_kuffers.py                               # Kuffers 데이터셋 분류용 커스텀 클래스
│   ├── kuffers_cnn.py                                        # Kuffers CNN 기본 학습 스크립트
│   ├── kuffers_cnn_hw.py                                     # Kuffers 과제 구현 스크립트 (기본)
│   ├── kuffers_cnn_hw_1.py                                   # Kuffers 과제 구현 스크립트 (버전 1)
│   ├── kuffers_cnn_hw_2.py                                   # Kuffers 과제 구현 스크립트 (버전 2)
│   ├── Figure_1.png                                          # 과제 결과 시각화 그래프 1
│   └── Figure_1_1.png                                        # 과제 결과 시각화 그래프 2
├── notes/                                                    # 수업 교안 및 이론 강의 자료 (PDF)
│   ├── 0.Introduction.pdf                                    # 강의 소개
│   ├── 1.디스플레이·반도체_공정을_위한_머신비전과_딥러닝_AI_Part_1_수정.pdf
│   ├── 1.디스플레이·반도체_공정을_위한_머신비전과_딥러닝_AI_Part_1_수정-복사.pdf
│   ├── 2.디스플레이·반도체_공정을_위한_머신비전과_딥러닝_AI_Part_2_수정.pdf
│   ├── 2.디스플레이·반도체_공정을_위한_머신비전과_딥러닝_AI_Part_2_수정-복사.pdf
│   ├── 3.반도체_공정_데이터_분석과_불량_원인_규명_EDA·RandomForest·XGBoost·SHAP·SMOTE_수정.pdf
│   └── 4.산업용_LLM_기초이론_및_제조업_적용사례_수정.pdf
├── data/                                                     # 학습 및 평가 데이터셋 모음
│   ├── MNIST/                                                # MNIST 손글씨 데이터셋
│   ├── FashionMNIST/                                         # Fashion-MNIST 의류 데이터셋
│   ├── kuffers/                                              # Kuffers 불량 검출 데이터셋 (TrainSet/TestSet/TestAll)
│   ├── Custom Workflow Instance Segmentation.v1i.yolov8/     # YOLOv8 Instance Segmentation 데이터셋 (train/valid/test)
│   └── Custom Workflow Instance Segmentation.v1i.yolov8-obb/ # YOLOv8 OBB 데이터셋 (train/valid/test)
├── synthetic_capacitors/                                     # 합성 커패시터 결함 검출 데이터셋
│   ├── Defective/                                            # 불량 커패시터 이미지 (Defective_000.png ~ 099.png, 100장)
│   └── Good/                                                 # 정상 커패시터 이미지 (Good_000.png ~ 099.png, 100장)
├── .gitignore                                                # Git 추적 제외 설정
├── README.md                                                 # 프로젝트 메인 개요 문서
└── DirectoryStructure.md                                     # 디렉토리 구조 누적 관리 문서 (본 파일)
```

### 🔄 주요 변경 세부사항 (Changelog Detail)
- **일자별 실습 폴더 분리**:
  - `0820_Thu/`: 기존 루트 디렉토리에 위치하던 8월 20일 CNN 실습 파일 및 모델 파일(`mnist_cnn.*`, `Own_ML_Class.py`, 노트북)을 해당 폴더로 이동 정리.
  - `0825_Tus/`: 8월 25일 진행된 YOLO Detection(`실습_yolo_detect.ipynb`) 및 Segmentation(`실습_YOLO_SEG.ipynb`) 실습 노트북 및 데이터셋 압축파일 추가.
- **과제 폴더(`HW/`) 신설**:
  - Kuffers 데이터셋 분류 관련 스크립트(`kuffers_cnn*.py`, `Own_ML_Class_kuffers.py`) 및 결과 그래프(`Figure_*.png`)를 분리하여 과제 전용 폴더로 구성.
- **교안 폴더(`notes/`) 신설**:
  - 머신비전, 디스플레이/반도체 공정 딥러닝, LLM 관련 PDF 교안 7종을 아카이빙.
- **데이터셋 확장(`data/`, `synthetic_capacitors/`)**:
  - `data/` 내 YOLO Instance Segmentation 및 OBB 데이터셋 디렉토리 추가.
  - 신규 합성 커패시터 데이터셋 폴더(`synthetic_capacitors/` - Defective 100장, Good 100장) 추가.

---

## 📅 [2026-08-20] - 초기 디렉토리 구조 (Initial Structure)

```text
ComputerVisionLab/
├── data/                                         # 실습 및 학습용 데이터셋
│   ├── MNIST/                                    # MNIST 숫자 손글씨 데이터셋
│   ├── FashionMNIST/                             # Fashion-MNIST 의류 이미지 데이터셋
│   └── kuffers/                                  # Kuffers 데이터셋 (Train/Test/TestAll)
├── .vscode/                                      # VSCode 환경 설정
│   └── settings.json
├── Own_ML_Class.py                               # 커스텀 머신러닝/딥러닝 유틸리티 및 모델 클래스
├── mnist_cnn.py                                  # MNIST CNN 모델 학습 및 평가 스크립트
├── 실습_CNN_Transfer_수정_ipynb의_사본.ipynb      # CNN 및 전이학습(Transfer Learning) 실습 주피터 노트북
├── mnist_clf.pth                                 # 학습 완료된 분류기 모델 가중치
├── mnist_cnn.pt                                  # MNIST CNN 체크포인트 모델
├── mnist_cnn.pth                                 # MNIST CNN 가중치 모델
├── .gitignore                                    # Git 추적 제외 설정
└── README.md                                     # 실습 진행 기록 및 디렉토리 구조 문서
```
