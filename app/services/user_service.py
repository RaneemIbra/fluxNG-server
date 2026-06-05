from typing import Dict, Any
from fastapi import HTTPException, status
from ..repositories.user_repository import UserRepository

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def get_authenticated_profile(self, user_id: str, email: str) -> Dict[str, Any]:
        profile = await self.repository.get_user_profile(user_id)
        if not profile:
            return {"id": user_id, "email": email, "role": "authenticated"}
        return profile

    async def register_new_user(self, email: str, password: str) -> Dict[str, Any]:
        try:
            auth_response = await self.repository.create_auth_user(email=email, password=password)
            
            if not auth_response.user:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Registration failed. Check if user already exists."
                )
                
            return {
                "id": auth_response.user.id,
                "email": auth_response.user.email,
                "role": "authenticated"
            }
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Auth system failure: {str(e)}"
            )