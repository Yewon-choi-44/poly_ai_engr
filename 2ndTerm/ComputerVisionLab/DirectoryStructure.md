# 📁 디렉토리 구조 관리 대장 (Directory Structure Log)

본 문서는 `ComputerVisionLab` 저장소의 디렉토리 구조 변동 사항 및 파일 구성 히스토리를 누적식으로 기록·관리하는 문서입니다.

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
