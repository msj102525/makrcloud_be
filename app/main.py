from logging.config import dictConfig
import sys
import os
import logging
from logging.handlers import TimedRotatingFileHandler

from watchfiles import DefaultFilter

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from app.api.endpoints import report
from datetime import datetime

# .env 파일에서 환경 변수 로드
load_dotenv()

# 환경 설정 - 개발 모드인지 배포 모드인지 확인
# ENV 환경 변수가 없으면 기본값은 'dev'
ENV = os.getenv("ENV", "dev").lower()
print(f"Running in {ENV} mode")  # 현재 실행 모드 출력

# 로그 설정 기본값
log_level = "DEBUG" if ENV == "dev" else "INFO"
log_dir = "logs"  # 로그 파일이 저장될 디렉토리

# 로그 파일 이름에 날짜 추가 (예: logs/2025-03-21_app.log)
log_filename = os.path.join(log_dir, f"{datetime.now().strftime('%Y-%m-%d')}_app.log")
error_log_filename = os.path.join(
    log_dir, f"{datetime.now().strftime('%Y-%m-%d')}_error.log"
)
if ENV == "dep" and not os.path.exists(log_dir):
    os.makedirs(log_dir)

# 모드별 로깅 설정
if ENV == "dev":
    # 개발 모드 로깅 설정 - 콘솔 출력 중심
    log_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
            },
            "colored": {
                "()": "colorlog.ColoredFormatter",
                "format": "%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
                "log_colors": {
                    "DEBUG": "cyan",
                    "INFO": "green",
                    "WARNING": "yellow,bg_white",
                    "ERROR": "red",
                    "CRITICAL": "red,bg_white",
                },
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": "colored",
                "level": log_level,
            },
        },
        "root": {
            "level": log_level,
            "handlers": ["console"],
        },
    }
else:
    # 배포 모드 로깅 설정 - 날짜별 로그 파일 저장
    log_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
            },
        },
        "handlers": {
            "file": {
                "class": "logging.handlers.TimedRotatingFileHandler",
                "filename": log_filename,
                "when": "midnight",  # 자정마다 새로운 로그 파일 생성
                "interval": 1,  # 1일 단위
                "backupCount": 60,  # 최대 60일간 보관
                "formatter": "default",
                "encoding": "utf-8",
                "level": "INFO",
            },
            "error_file": {
                "class": "logging.handlers.TimedRotatingFileHandler",
                "filename": error_log_filename,
                "when": "midnight",
                "interval": 1,
                "backupCount": 30,
                "formatter": "default",
                "encoding": "utf-8",
                "level": "ERROR",
            },
        },
        "root": {
            "level": "INFO",
            "handlers": ["file", "error_file"],
        },
    }

# 로깅 설정 적용
dictConfig(log_config)

# 현재 모듈의 로거 생성
logger = logging.getLogger(__name__)

# 애플리케이션 시작 로그 기록
logger.info(f"Application starting in {ENV} mode")

# FastAPI 애플리케이션 생성
app = FastAPI()

# CORS 설정 추가 (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("ALLOWED_ORIGINS", "").split(
        ","
    ),  # 환경 변수에서 허용된 오리진 목록 가져오기 (쉼표로 구분)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logger.info(f"ALLOWED_ORIGINS: {os.getenv('ALLOWED_ORIGINS', '')}")

# API 라우터 등록 (report 관련 엔드포인트 추가)
app.include_router(report.router, prefix="/report")


def filter_git_changes(changes):
    return {
        change
        for change in changes
        if not any(".git" in str(changed_path) for (change, changed_path) in changes)
    }


# 스크립트를 직접 실행할 때의 진입점
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True if ENV == "dev" else False,
        reload_dirs=(["app/"] if ENV == "dev" else None),
        reload_includes=["*.py"],
        reload_excludes=[".git", "*.pyc", "__pycache__"],
    )
