from fastapi import APIRouter

# we export the router to be included in main.py
router = APIRouter(prefix="/api/v1/issues", tags=["issues"])

@router.get("/")
async def get_issues():
    return []


