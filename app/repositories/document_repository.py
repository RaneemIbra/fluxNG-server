from typing import Dict, Any, Optional
from supabase import AsyncClient

class DocumentRepository:
    def __init__(self, client: AsyncClient):
        self.client = client

    async def get_by_id(self, document_id: str, user_id: str) -> Optional[Dict[str, Any]]:
        response = await self.client.table("documents").select("*").eq("id", document_id).eq("user_id", user_id).execute()
        return response.data[0] if response.data else None

    async def insert_record(self, data: Dict[str, Any]) -> Dict[str, Any]:
        response = await self.client.table("documents").insert(data).execute()
        return response.data[0]