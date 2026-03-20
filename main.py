from fastapi import FastAPI
from app.routes.issues import router as issues_router

# Run promptly with: fastapi dev main.py
app = FastAPI()

# Include the issues router
app.include_router(issues_router)



    