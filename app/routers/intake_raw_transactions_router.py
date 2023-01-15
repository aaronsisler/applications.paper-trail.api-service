from fastapi import APIRouter

router = APIRouter(
    prefix="/intake/raw-transactions",
    responses={404: {"description": "Not found"}},
)


@router.post("/", status_code=200)
def post_intake_raw_transactions():
    return;
