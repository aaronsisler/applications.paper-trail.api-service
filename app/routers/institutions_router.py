from fastapi import APIRouter

from app.models.supported_institution import SupportedInstitution

router = APIRouter(
    prefix="/institutions",
    responses={404: {"description": "Not found"}},
)


@router.get("/supported/{supported_institution}")
def get_supported_institution(supported_institution: SupportedInstitution):
    supported_institution_message_suffix = "is a supported institution!"

    match supported_institution:
        case SupportedInstitution.CITI:
            return {"supported_institution": supported_institution,
                    "message": f"Citi {supported_institution_message_suffix}"}
        case SupportedInstitution.AMERICAN_EXPRESS:
            return {"supported_institution": supported_institution,
                    "message": f"American Express {supported_institution_message_suffix}"}
        case _:
            # Make this an invalid type/etc. that returns a 400 based HTTP status code
            return {"institution_type": supported_institution, "message": "This is not a supported institution"}
