from pydantic import BaseModel
from typing import List, Optional

class Trademark(BaseModel):
    productName: Optional[str]
    productNameEng: Optional[str]
    applicationNumber: str
    applicationDate: Optional[str]
    registerStatus: Optional[str]
    publicationNumber: Optional[str]
    publicationDate: Optional[str]
    registrationNumber: Optional[List[str]]
    registrationDate: Optional[List[Optional[str]]]
    internationalRegNumbers: Optional[List[str]]
    internationalRegDate: Optional[str]
    priorityClaimNumList: Optional[List[str]]
    priorityClaimDateList: Optional[List[str]]
    asignProductMainCodeList: Optional[List[str]]
    asignProductSubCodeList: Optional[List[str]]
    viennaCodeList: Optional[List[str]]
