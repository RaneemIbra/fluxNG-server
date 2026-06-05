from fastapi import APIRouter, Depends, status
from ..core.security import get_current_user
from ..core.dependencies import async_supabase
from ..models.user_schema import UserProfileResponseSchema, UserRegisterRequestSchema
from ..repositories.user_repository import UserRepository
from ..services.user_service import UserService

router = APIRouter(prefix="/api/users", tags=["Users subsystem"])

def resolve_user_service() -> UserService:
    return UserService(UserRepository(async_supabase))

@router.post("/register", response_model=UserProfileResponseSchema, status_code=status.HTTP_201_CREATED)
async def register_user(
    payload: UserRegisterRequestSchema,
    service: UserService = Depends(resolve_user_service)
):
    return await service.register_new_user(
        email=payload.email,
        password=payload.password
    )

@router.get("/me", response_model=UserProfileResponseSchema)
async def get_my_profile(
    current_user = Depends(get_current_user),
    service: UserService = Depends(resolve_user_service)
):
    return await service.get_authenticated_profile(
        user_id=current_user.id, 
        email=current_user.email
    )