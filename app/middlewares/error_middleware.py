import json

from starlette import status
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse, Response


class ErrorMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)

        if response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY:
            content = await self.load_content(response)

            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content=content,
                headers=dict(response.headers)
            )

        return response

    async def load_content(self, response: Response):
        body = b""
        async for chunk in response.body_iterator:
            body += chunk

        return json.loads(body.decode())
