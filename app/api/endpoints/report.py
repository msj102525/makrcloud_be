import logging
from fastapi import APIRouter, HTTPException, Request
from typing import List
import time

from app.common.controller_logging import *

from app.schemas.report import (
    LocalStoreRedux,
)
from app.service.local_store_basic_info import (
    select_local_store_info_redux_by_store_business_number as service_select_local_store_info_redux_by_store_business_number,
)

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/store/info/redux", response_model=LocalStoreRedux)
async def select_report_store_info_redux(store_business_id: str, request: Request):
    start_time = time.time()
    endpoint = "select_report_store_info_redux"

    # 전체 요청 파라미터 로깅
    log_request_start(endpoint, request)
    try:
        result = service_select_local_store_info_redux_by_store_business_number(
            store_business_id
        )

        process_time = round(time.time() - start_time, 4)

        log_request_end(endpoint, process_time, result)  # 로깅 호출

        return result

    except HTTPException as http_ex:
        process_time = round(time.time() - start_time, 4)
        log_error(endpoint, store_business_id, process_time, http_ex)  # 로깅 호출
        raise http_ex

    except Exception as e:
        process_time = round(time.time() - start_time, 4)
        error_msg = f"Unexpected error while processing request: {str(e)}"
        log_error(endpoint, store_business_id, process_time, e)  # 로깅 호출
        raise HTTPException(status_code=500, detail=error_msg)
