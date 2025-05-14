# MarkCloud Backend

FastAPI 기반 상표 검색 API 프로젝트입니다.  
국내 상표 데이터를 활용하여 상표명을 기반으로 필터링하거나, 조건 검색 기능을 제공합니다.

---

## 🗂 프로젝트 구조

markcloude_be/
├── app/
│ ├── crud/ # 데이터 처리 (CRUD)
│ ├── data/ # JSON 샘플 데이터 저장
│ ├── endpoint/ # API 라우터
│ ├── schemas/ # Pydantic 스키마 정의
│ ├── service/ # 서비스 로직
│ └── main.py # 앱 진입점
├── .env # 환경 변수 설정 (직접 생성 필요)
├── requirements.txt # 의존성 목록
└── README.md # 프로젝트 설명 파일

---

## 🚀 실행 순서
프로젝트 clone
터미널에서 프로젝트 경로로 이동 ex) D:\...\...\markcloude_be
python -m venv .venv  # 가상 환경 생성
.venv\Scripts\activate  # 가상 환경 활성화
python.exe -m pip install --upgrade pip
프로젝트루트디렉토리에 .env 파일 생성 ENV=dev || ENV=dep 필수 X
pip install -r requirements.txt  필수 패키지 설치
터미널 프로젝트루트디렉토리에서 python app/main.py 로 실행
python .\app\main.py
http/localhost:8000/docs Swagger 확인
구현된 기능
✅ 한또는 영문 상표명 기반 필터 검색 API
 상태별(등록, 출원, 거절 등) 상표 데이터 검색 API

📌 향후 검색 기능 추가 예정 (날짜 범위, 코드 기준 등)

🔧 로깅 시스템
서비스 및 API 단에서 다음과 같은 로깅 처리가 됩니다:

요청 시작/종료 시간

처리 시간 및 예외 로그

서비스/CRUD 단계별 에러 추적



