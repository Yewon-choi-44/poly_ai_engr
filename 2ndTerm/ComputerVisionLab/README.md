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
├── HW/                                                       # Kuffers 데이터셋 실습 및 과제 스크립트
├── notes/                                                    # 수업 교안 및 이론 강의 자료 (PDF)
├── data/                                                     # 이미지 데이터셋 (MNIST, FashionMNIST, kuffers, YOLO 등)
├── synthetic_capacitors/                                     # 합성 커패시터 결함 검출 데이터셋 (Defective/Good)
├── .gitignore                                                # Git 추적 제외 설정
├── README.md                                                 # 프로젝트 메인 개요 문서
└── DirectoryStructure.md                                     # 디렉토리 구조 누적 관리 문서
```

---

## 📅 실습 및 학습 일지 (Changelog)

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
