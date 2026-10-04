from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from app.services.cybersecurity_services import (
    CybersecurityService
)


router = APIRouter(
    prefix="/api",
    tags=["Cybersecurity"]
)


service = None


class AnalyzeRequest(BaseModel):

    features: dict[str, float] = Field(
        default_factory=dict
    )


@router.get("/health")
def health():

    return {
        "status": "healthy",
        "service": "RAG Cybersecurity Assistant"
    }


@router.post("/analyze")
def analyze(request: AnalyzeRequest):

    global service

    try:

        if service is None:
            service = CybersecurityService()

        result = service.analyze(
            request.features
        )

        return result

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )