from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    """Application settings"""
    app_name: str = "Image Recognition Service"
    app_version: str = "2.0.0"
    debug: bool = False
    
    # Google API
    google_api_key: str = ""
    google_cloud_credentials: str = ""
    
    # Redis
    redis_url: str = "redis://localhost:6379"
    cache_ttl_hours: int = 24
    
    # Rate limiting
    rate_limit_requests: int = 100
    rate_limit_window_seconds: int = 60
    
    # Authentication
    api_keys: list = []
    
    # Service settings
    max_file_size: int = 10 * 1024 * 1024  # 10MB
    allowed_extensions: list = ["jpg", "jpeg", "png", "gif", "webp"]
    batch_max_concurrent: int = 3
    
    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()