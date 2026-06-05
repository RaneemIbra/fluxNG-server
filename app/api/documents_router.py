from fastapi import APIRouter, Depends
from app.core.security import get_current_user
from app.core.dependencies import async_supabase
from app.models.document_schema import DocumentCreateSchema
from app.repositories.document_repository import DocumentRepository
from app.services.document_service import DocumentService

router = APIRouter(prefix="/api/documents", tags=["Isolated Documents Engine"])

def resolve_document_service() -> DocumentService:
    return DocumentService(DocumentRepository(async_supabase))

@router.get("/{document_id}")
async def get_document_by_id(
    document_id: str,
    user = Depends(get_current_user),
    service: DocumentService = Depends(resolve_document_service)
):
    return await service.retrieve_document(document_id=document_id, user_id=user.id)

@router.post("", status_code=201)
async def add_document(
    payload: DocumentCreateSchema,
    user = Depends(get_current_user),
    service: DocumentService = Depends(resolve_document_service)
):
    return await service.create_user_document(user_id=user.id, title=payload.title, file_url=payload.file_url)