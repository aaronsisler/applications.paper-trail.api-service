from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from app.routers import institutions_router, users_router
from app.routers.intake import intake_raw_account_transactions_router

app = FastAPI()

# REST Based
app.include_router(institutions_router.router)
app.include_router(users_router.router)

# Event Based
app.include_router(intake_raw_account_transactions_router.router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def main():
    return RedirectResponse(url="/docs/")


@app.get("/health")
def get_application_health():
    return {"status": "UP"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
