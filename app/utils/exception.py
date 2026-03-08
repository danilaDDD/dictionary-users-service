from fastapi import HTTPException
from starlette import status


def raise_http_exception(status_code: int = status.HTTP_400_BAD_REQUEST, msg: str = None):
    raise HTTPException(status_code=status_code, detail=msg)