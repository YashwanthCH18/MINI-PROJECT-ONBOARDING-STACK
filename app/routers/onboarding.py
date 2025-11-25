from fastapi import APIRouter, Depends, HTTPException, status
from app.auth import get_current_user, AuthUser
from app.supabase_client import get_supabase
from app.models import OnboardingProfileUpdate, OnboardingProfileResponse
from datetime import datetime

router = APIRouter(prefix="/v1/onboarding", tags=["Onboarding"])


@router.get("", response_model=OnboardingProfileResponse)
async def get_onboarding_profile(
    current_user: AuthUser = Depends(get_current_user)
):
    """
    Get the current user's onboarding profile.
    Auto-scoped to the authenticated user (jwt.sub).
    """
    supabase = get_supabase()
    
    try:
        # Query profiles table for the current user
        response = supabase.table("profiles").select("*").eq("id", current_user.user_id).execute()
        
        if not response.data or len(response.data) == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Profile not found"
            )
        
        return OnboardingProfileResponse(**response.data[0])
        
    except Exception as e:
        if isinstance(e, HTTPException):
            raise e
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error fetching profile: {str(e)}"
        )


@router.put("", response_model=OnboardingProfileResponse)
async def update_onboarding_profile(
    profile_data: OnboardingProfileUpdate,
    current_user: AuthUser = Depends(get_current_user)
):
    """
    Update or create the current user's onboarding profile.
    Auto-scoped to the authenticated user (jwt.sub).
    """
    supabase = get_supabase()
    
    try:
        # Prepare update data (exclude None values)
        update_data = profile_data.model_dump(exclude_none=True)
        
        # Convert date to string for Supabase
        if "date_of_birth" in update_data and update_data["date_of_birth"]:
            update_data["date_of_birth"] = update_data["date_of_birth"].isoformat()
        
        # Add updated_at timestamp
        update_data["updated_at"] = datetime.utcnow().isoformat()
        
        # Check if profile exists
        existing = supabase.table("profiles").select("id").eq("id", current_user.user_id).execute()
        
        if existing.data and len(existing.data) > 0:
            # Update existing profile
            response = supabase.table("profiles").update(update_data).eq("id", current_user.user_id).execute()
        else:
            # Create new profile
            update_data["id"] = current_user.user_id
            update_data["created_at"] = datetime.utcnow().isoformat()
            response = supabase.table("profiles").insert(update_data).execute()
        
        if not response.data or len(response.data) == 0:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to update profile"
            )
        
        return OnboardingProfileResponse(**response.data[0])
        
    except Exception as e:
        if isinstance(e, HTTPException):
            raise e
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error updating profile: {str(e)}"
        )
