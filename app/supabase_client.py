from supabase import create_client, Client
from app.config import settings


class SupabaseClient:
    """Supabase client wrapper for database operations."""
    
    _instance: Client = None
    
    @classmethod
    def get_client(cls) -> Client:
        """Get or create Supabase client instance."""
        if cls._instance is None:
            cls._instance = create_client(
                settings.SUPABASE_URL,
                settings.SUPABASE_KEY
            )
        return cls._instance


# Convenience function to get the client
def get_supabase() -> Client:
    """Get Supabase client instance."""
    return SupabaseClient.get_client()
