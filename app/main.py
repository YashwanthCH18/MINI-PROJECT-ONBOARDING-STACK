from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import onboarding
from mangum import Mangum

# Create FastAPI application
app = FastAPI(
    title="Onboarding Profile Stack API",
    description="Microservice for managing user onboarding profiles",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual frontend origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(onboarding.router)


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "onboarding-stack"}


@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "service": "Onboarding Profile Stack",
        "version": "1.0.0",
        "endpoints": {
            "health": "/health",
            "docs": "/docs",
            "onboarding": "/v1/onboarding"
        }
    }

# Lambda Handler
handler = Mangum(app)
