import time
from fastapi import APIRouter, Query, Request, HTTPException
from typing import List
from app.utils.controller_logging import *
from schemas.trademark import Trademark
from service.trademark import (
    search_trademark_by_name as service_search_trademark_by_name,
    search_by_application_date as service_search_by_application_date,
)

router = APIRouter()


# GET /trademarks/search?name=JK
@router.get("/search", response_model=List[Trademark])
async def search_trademark_by_name(
    name: str = Query(..., description="상표명 한글 또는 영문"), request: Request = None
):
    start_time = time.time()
    endpoint = "search_by_name"
    log_request_start(endpoint, request)

    try:
        result = service_search_trademark_by_name(name)
        log_request_end(endpoint, round(time.time() - start_time, 4), result)
        return result

    except HTTPException as http_ex:
        log_error(endpoint, name, round(time.time() - start_time, 4), http_ex)
        raise http_ex

    except Exception as e:
        log_error(endpoint, name, round(time.time() - start_time, 4), e)
        raise HTTPException(status_code=500, detail="Internal server error")


# GET /trademarks/search-by-date?start_date=20000101&end_date=20150101
@router.get("/date", response_model=List[Trademark])
async def search_by_application_date(
    start_date: str = Query(..., description="출원일 시작 (YYYYMMDD)"),
    end_date: str = Query(..., description="출원일 종료 (YYYYMMDD)"),
    request: Request = None,
):
    start_time = time.time()
    endpoint = "search_by_application_date"
    log_request_start(endpoint, request)

    try:
        result = service_search_by_application_date(start_date, end_date)
        log_request_end(endpoint, round(time.time() - start_time, 4), result)
        return result

    except HTTPException as http_ex:
        log_error(
            endpoint,
            f"{start_date}-{end_date}",
            round(time.time() - start_time, 4),
            http_ex,
        )
        raise http_ex

    except Exception as e:
        log_error(
            endpoint, f"{start_date}-{end_date}", round(time.time() - start_time, 4), e
        )
        raise HTTPException(status_code=500, detail="Internal server error")
