from typing import Union

from fastapi import FastAPI
from starlette.responses import RedirectResponse

from app.routers import institutions_router, users_router

app = FastAPI()

app.include_router(institutions_router.router)
app.include_router(users_router.router)


@app.get("/")
def main():
    return RedirectResponse(url="/docs/")


@app.get("/health")
def get_application_health():
    return {"status": "UP"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
