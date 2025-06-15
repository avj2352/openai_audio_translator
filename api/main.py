import logging
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, RedirectResponse
from scalar_fastapi import get_scalar_api_reference
# ..custom
from util.about import config, description
from resources.transcribe import transcribe_router
from resources.prompt import prompt_router

# Create the APP
app = FastAPI(
    title = config.title,
    version = config.version,
    description = description,
    openapi_tags = config.tags_metadata
)

# migration - create tables
# init()

# logging config
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s[%(filename)s:%(lineno)s-%(funcName)s()]-%(message)s",
    datefmt="%Y-%m-%d %H:%M:%S")
# Allow CORS
ALLOWED_HOSTS = ["*"]

# add module name in log outputs
logger = logging.getLogger(__name__)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# create scalar documentation
@app.get("/scalar", include_in_schema=False)
async def scalar_html():
    return get_scalar_api_reference(
        openapi_url=str(app.openapi_url),
        title=app.title,        
        dark_mode=True,        
        show_sidebar=True,        
        hide_download_button=False,
        hide_models=False
)


# redirect to swagger docs
@app.get("/", include_in_schema=False)
async def root():
    logger.debug("Redirecting to scalar swagger docs")
    return RedirectResponse(url='/scalar')


# flatten payload validations
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(_: Request, exc: RequestValidationError):
    errors = exc.errors()
    custom_errors = []
    for error in errors:
        field = "-".join(str(x) for x in error['loc'])
        msg = error["msg"]
        custom_errors.append({"field": field, "message": msg})
    return JSONResponse(
        status_code=400,
        content={
            "detail": "Validation Error",
            "message": custom_errors
        }
    )

app.include_router(router=transcribe_router, prefix='/transcribe', tags=["transcribe"])
app.include_router(router=prompt_router, prefix='/prompt', tags=["prompt"])

