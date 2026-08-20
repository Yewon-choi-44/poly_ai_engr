# 👁️ 컴퓨터비전실습 (Computer Vision Lab)

컴퓨터비전실습 과목의 수업 내용, 실습 코드, 학습 모델 및 데이터셋을 기록하고 체계적으로 관리하는 저장소입니다.

---

## 📁 디렉토리 구조 (Directory Structure)

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
├── 실습_CNN_Transfer_수정_ipynb의_사본.ipynb      # CNN 및 전이학습(Transfer Learning) 실습 주피터 노트북 (과제)
├── mnist_clf.pth                                 # 학습 완료된 분류기 모델 가중치
├── mnist_cnn.pt                                  # MNIST CNN 체크포인트 모델
├── mnist_cnn.pth                                 # MNIST CNN 가중치 모델
├── .gitignore                                    # Git 추적 제외 설정
└── README.md                                     # 실습 진행 기록 및 디렉토리 구조 문서
```

---

## 📅 실습 및 학습 일지 (Changelog)

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
