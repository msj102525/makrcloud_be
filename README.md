# MarkCloud Backend

FastAPI 기반 상표 검색 API 프로젝트입니다.  
국내 상표 데이터를 활용하여 상표명을 기반으로 필터링하거나, 조건 검색 기능을 제공합니다.

## 🗂 프로젝트 구조

```
markcloude_be/
├── app/
│   ├── crud/       # 데이터 처리 (CRUD 작업)
│   ├── data/       # JSON 샘플 데이터 저장
│   ├── endpoint/   # API 라우터
│   ├── schemas/    # Pydantic 스키마 정의
│   ├── service/    # 서비스 로직
│   └── main.py     # 앱 진입점
├── .env            # 환경 변수 설정 (직접 생성 필요)
├── requirements.txt # 의존성 목록
└── README.md       # 프로젝트 설명 파일
```

## 🚀 시작하기

### 설치 및 실행 방법

1. 프로젝트 클론
   ```bash
   git clone https://github.com/msj102525/makrcloud_be.git
   cd markcloude_be
   ```

2. 가상 환경 설정
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # source .venv/bin/activate  # Mac/Linux
   ```

3. 패키지 설치
   ```bash
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. 환경 설정
   - 프로젝트 루트 디렉토리에 `.env` 파일 생성
   - 환경 설정 추가: `ENV=dev` 또는 `ENV=dep`

5. 서버 실행
   ```bash
   python app/main.py
   ```

6. API 문서 확인
   - 브라우저에서 `http://localhost:8000/docs` 접속하여 Swagger UI 확인

## ⚙️ 주요 기능

### 구현된 기능
- 상표명 검색 API
- 한글 또는 영문 상표명으로 상표를 검색할 수 있는 API입니다.
- GET /trademarks/search?productName={productName}

- 상표의 등록일을 기준으로 상표를 검색할 수 있는 API입니다.
- GET /trademarks/registration-date?startDate={startDate}&endDate={endDate}
- 시작일과 종료일을 입력받아 해당 범위에 해당하는 상표들을 반환합니다.

## 🔧 로깅 시스템

서비스 및 API 단에서 다음과 같은 로깅 처리가 구현되어 있습니다:
- .env파일의 ENV=dev 
- 요청 시작/종료 시간 기록
- API 처리 시간 측정
- 예외 상황 로깅
- 서비스/CRUD 단계별 에러 추적
- .env파일의 ENV=dep
- log파일로 쌓이게끔 처리

## 💬 문의 및 기여
msj102525@gmail.com
