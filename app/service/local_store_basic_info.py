from fastapi import HTTPException
import logging
import os
from datetime import datetime, timezone, timedelta
import time

from app.common.service_logging import *


from app.crud.local_store_basic_info import (
    select_local_store_info_redux_by_store_business_number as crud_select_local_store_info_redux_by_store_business_number,
)
from app.schemas.report import (
    LocalStoreRedux,
)

logger = logging.getLogger(__name__)


def select_local_store_info_redux_by_store_business_number(
    store_business_id: str,
) -> LocalStoreRedux:
    start_time = time.time()
    service_name = "select_local_store_info_redux_by_store_business_number"

    log_service_start(service_name)  # 서비스 시작 로깅

    try:
        log_db_fetch(service_name)  # DB 조회 시작 로깅
        result = crud_select_local_store_info_redux_by_store_business_number(
            store_business_id
        )

        process_time = round(time.time() - start_time, 4)
        log_service_end(service_name, process_time)  # 서비스 종료 로깅

        return result

    except HTTPException as http_ex:
        process_time = round(time.time() - start_time, 4)
        log_service_error(service_name, process_time, http_ex)  # HTTP 예외 로깅
        raise

    except Exception as e:
        process_time = round(time.time() - start_time, 4)
        log_service_error(service_name, process_time, e)  # 일반 예외 로깅
        raise HTTPException(status_code=500, detail=str(e))

