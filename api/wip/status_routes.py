from fastapi import APIRouter

######################################################
## Router for status
######################################################

status_router = APIRouter(tags=["status"])

@status_router.get("/ping")
def ping():
    # Mocked response for testing
    return {"message": "Pong!"}

@status_router.get("/health")
def health():
    # Mocked response for testing
    return {"status": "healthy"}