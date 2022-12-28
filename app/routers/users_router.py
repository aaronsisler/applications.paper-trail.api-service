from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    responses={404: {"description": "Not found"}},
)


@router.get("/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
