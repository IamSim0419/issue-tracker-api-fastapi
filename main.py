from fastapi import FastAPI
from app.routes.issues import router as issues_router
from app.middleware.timer import timer_middleware
from fastapi.middleware.cors import CORSMiddleware

# Run promptly with: fastapi dev main.py
# Or with uvicorn: uvicorn main:app --reload
app = FastAPI()

app.middleware("http")(timer_middleware) # add our timer middleware to the app

# Add CORS middleware to allow requests from any origin (for development purposes)
app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"]
    )

# Include the issues router
app.include_router(issues_router)



    