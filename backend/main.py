import os
import secrets

from fastapi import Depends, FastAPI, HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse, RedirectResponse, Response
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from slowapi.errors import RateLimitExceeded
from starlette.exceptions import HTTPException
from starlette.middleware.base import BaseHTTPMiddleware

from routers import auth

app = FastAPI()
app.include_router(auth.router)

# CORS
ALLOWED_ORIGINS = os.getenv('ALLOWED_ORIGINS')
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# Root endpoint
@app.get("/")
def read_root():
    return {"message" : "Api working. Use /docs for documentation."}


# Set docs security and configuration
security = HTTPBasic()

USERNAME = os.getenv('DOCS_USERNAME')
PASSWORD = os.getenv('DOCS_PASSWORD')

def verify_credentials(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, USERNAME)
    correct_password = secrets.compare_digest(credentials.password, PASSWORD)

    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized",
            headers={"WWW-Authenticate" : "Basic"}
        )
    return True

@app.get("/docs", include_in_schema=False)
def custom_swagger_ui(credentials: bool = Depends(verify_credentials)):
    return get_swagger_ui_html(openapi_url="/openapi.json", title="Docs")

@app.get("/openapi.json", include_in_schema=False)
def openapi(credentials: bool = Depends(verify_credentials)):
    return get_openapi(title="My API", version="1.0.0", routes=app.routes)


# # Force HTTPS Middleware
# class HTTPSRedirectMiddleware(BaseHTTPMiddleware):
#     async def dispatch(self, request:  Request, call_next):
#         if request.url.scheme != "https":
#             url = request.url.replace(scheme="https")
#             return RedirectResponse(url=url)
#         response = await call_next(request)
#         return response
# app.add_middleware(HTTPSRedirectMiddleware)

# # Security Headers middleware
# class SecurityHeadersMiddleware(BaseHTTPMiddleware):
#     async def dispatch(self, request: Request, call_next):
#         response: Response = await call_next(request)
#         response.headers["X-Frame-Options"] = "DENY"
#         response.headers["X-Content-Type-Options"] = "nosniff"
#         response.headers["Content-Security-Policy"] = "default-src 'self'"
#         response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
#         response.headers["Referrer-Policy"] = "no-referrer"
#         return response
# app.add_middleware(SecurityHeadersMiddleware)

# Exception handlers
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"detail" : "Internal server error"})

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(status_code=exc.status_code, content={"detail" : exc.detail})

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(status_code=422, content={"detail" : exc.errors})

@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(status_code=429, content={"detail": "Too many requests, slow down!"})