from fastapi import Request
from fastapi.responses import JSONResponse


async def auth_middleware(request: Request, call_next):
    response = await call_next(request)
    if response.status_code == 401:
        return JSONResponse(status_code=401, payload={"message": "Not connected."})
    return response