import logging
from fastapi import HTTPException
import time

from app.common.crud_logging import *


from app.schemas.report import (
    LocalStoreRedux,
)

logger = logging.getLogger(__name__)


def select_local_store_info_redux_by_store_business_number(
    store_business_id: str,
) -> LocalStoreRedux:

    crud_name = "select_local_store_info_redux_by_store_business_number"
    start_time = time.time()

    log_crud_start(crud_name)  # CRUD 시작 로깅

    try:
        with get_db_connection() as connection:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                select_query = """
                    SELECT 
                        CITY_NAME,
                        DISTRICT_NAME,
                        SUB_DISTRICT_NAME,
                        DETAIL_CATEGORY_NAME,
                        BIZ_DETAIL_CATEGORY_REP_NAME,
                        LOC_INFO_DATA_REF_DATE,
                        NICE_BIZ_MAP_DATA_REF_DATE,
                        POPULATION_DATA_REF_DATE,
                        BIZ_MAIN_CATEGORY_ID
                    FROM
                        REPORT 
                    WHERE STORE_BUSINESS_NUMBER = %s
                    ;
                """

                log_crud_query(
                    crud_name, select_query, (store_business_id,)
                )  # 쿼리 실행 로깅
                cursor.execute(select_query, (store_business_id,))
                row = cursor.fetchone()

                if not row:
                    raise HTTPException(
                        status_code=404,
                        detail=f"LocalStoreBasicInfo {store_business_id}에 해당하는 매장 정보를 찾을 수 없습니다.",
                    )

                detail_category_name = row["DETAIL_CATEGORY_NAME"]

                result = LocalStoreRedux(
                    city_name=row["CITY_NAME"],
                    district_name=row["DISTRICT_NAME"],
                    sub_district_name=row["SUB_DISTRICT_NAME"],
                    detail_category_name=detail_category_name,
                    biz_detail_category_rep_name=row["BIZ_DETAIL_CATEGORY_REP_NAME"]
                    or detail_category_name,
                    loc_info_data_ref_date=row["LOC_INFO_DATA_REF_DATE"],
                    nice_biz_map_data_ref_date=row["NICE_BIZ_MAP_DATA_REF_DATE"],
                    population_data_ref_date=row["POPULATION_DATA_REF_DATE"],
                    biz_main_category_id=row["BIZ_MAIN_CATEGORY_ID"],
                )

                return result

    except pymysql.Error as e:
        log_crud_error(crud_name, e)  # DB 오류 로깅
        raise HTTPException(status_code=503, detail=f"데이터베이스 연결 오류: {str(e)}")

    except Exception as e:
        log_crud_error(crud_name, e)  # 일반 오류 로깅
        raise HTTPException(status_code=500, detail=f"내부 서버 오류: {str(e)}")

