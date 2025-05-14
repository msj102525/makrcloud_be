import logging
from fastapi import APIRouter, HTTPException, Request
import time

from app.utils.controller_logging import *

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/")
async def root(request: Request):
    start_time = time.time()
    endpoint = "root"

    log_request_start(endpoint, request)
    try:
        result = "TradeMarkAPI! - 문승종"

        return result

    except HTTPException as http_ex:
        process_time = round(time.time() - start_time, 4)
        log_error(endpoint, process_time, http_ex)
        raise http_ex

    except Exception as e:
        process_time = round(time.time() - start_time, 4)
        error_msg = f"Unexpected error while processing request: {str(e)}"
        log_error(endpoint, process_time, e)
        raise HTTPException(status_code=500, detail=error_msg)
