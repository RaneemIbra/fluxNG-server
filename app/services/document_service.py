from typing import Dict, Any, Optional
from fastapi import HTTPException, status
from app.repositories.document_repository import DocumentRepository

class DocumentService:
    def __init__(self, repository: DocumentRepository):
        self.repository = repository

    async def retrieve_document(self, document_id: str, user_id: str) -> Dict[str, Any]:
        document = await self.repository.get_by_id(document_id, user_id)
        if not document:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Requested document record could not be found"
            )
        return document

    async def create_user_document(self, user_id: str, title: str, file_url: str) -> Dict[str, Any]:
        payload = {"title": title, "file_url": file_url, "user_id": user_id}
        return await self.repository.insert_record(payload)