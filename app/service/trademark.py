from fastapi import HTTPException
from typing import List
from app.utils.service_logging import *
from crud.trademark import (
    search_trademark_by_name as crud_search_trademark_by_name,
    search_by_application_date as crud_search_by_application_date,
)
import time
from schemas.trademark import Trademark


def search_trademark_by_name(name: str) -> List[Trademark]:
    start_time = time.time()
    service_name = "search_trademark_by_name"
    log_service_start(service_name)

    try:
        result = crud_search_trademark_by_name(name)
        log_service_end(service_name, round(time.time() - start_time, 4))
        return result
    except Exception as e:
        log_service_error(service_name, round(time.time() - start_time, 4), e)
        raise HTTPException(status_code=500, detail=str(e))


def search_by_application_date(start_date: str, end_date: str) -> List[Trademark]:
    start_time = time.time()
    service_name = "search_trademark_by_application_date"
    log_service_start(service_name)

    try:
        result = crud_search_by_application_date(start_date, end_date)
        log_service_end(service_name, round(time.time() - start_time, 4))
        return result
    except Exception as e:
        log_service_error(service_name, round(time.time() - start_time, 4), e)
        raise HTTPException(status_code=500, detail=str(e))
