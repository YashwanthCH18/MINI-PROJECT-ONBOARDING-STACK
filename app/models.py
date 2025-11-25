from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List, Any
from datetime import datetime, date


class CareerPreferences(BaseModel):
    """Career preferences embedded in profile."""
    roles_targeted: Optional[List[str]] = None
    min_target_lpa: Optional[float] = None
    preferred_locations: Optional[List[str]] = None


class Education(BaseModel):
    """Education information."""
    degree: Optional[str] = None
    field: Optional[str] = None
    institution: Optional[str] = None
    year: Optional[int] = None


class OnboardingProfileUpdate(BaseModel):
    """Request model for updating onboarding profile."""
    full_name: Optional[str] = None
    date_of_birth: Optional[date] = None
    secondary_email: Optional[EmailStr] = None
    address: Optional[str] = None
    linkedin_url: Optional[str] = None
    github_username: Optional[str] = None
    skills: Optional[List[str]] = None
    career_preferences: Optional[Any] = None  # JSONB field
    education: Optional[Any] = None  # JSONB field
    onboarding_completed: Optional[bool] = False
    profile_photo_url: Optional[str] = None
    govt_id_url: Optional[str] = None


class OnboardingProfileResponse(BaseModel):
    """Response model for onboarding profile."""
    id: str
    full_name: Optional[str] = None
    date_of_birth: Optional[date] = None
    secondary_email: Optional[str] = None
    address: Optional[str] = None
    linkedin_url: Optional[str] = None
    github_username: Optional[str] = None
    skills: Optional[List[str]] = None
    career_preferences: Optional[Any] = None
    education: Optional[Any] = None
    onboarding_completed: bool
    profile_photo_url: Optional[str] = None
    govt_id_url: Optional[str] = None
    api_keys: Optional[Any] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None



