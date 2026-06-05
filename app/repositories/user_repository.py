from typing import Dict, Any, Optional
from supabase import AsyncClient

class UserRepository:
    def __init__(self, client: AsyncClient):
        self.client = client

    async def get_user_profile(self, user_id: str) -> Optional[Dict[str, Any]]:
        response = await self.client.table("profiles").select("*").eq("id", user_id).execute()
        return response.data[0] if response.data else None

    async def create_auth_user(self, email: str, password: str) -> Dict[str, Any]:
        response = self.client.auth.sign_up({
            "email": email,
            "password": password
        })
        return response