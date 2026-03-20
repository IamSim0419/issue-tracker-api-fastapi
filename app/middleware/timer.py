import time
from fastapi import Request

async def timer_middleware(request: Request, call_next):
    start = time.perf_counter() # start timer
    response = await call_next(request) # process request
    response.headers["X-Process-Time"] = f"{time.perf_counter() - start:.4f}s" # add header with elapsed time
    return response 











# To create folder and file using terminal commands:
# mkdir app/middleware && touch app/middleware/timer.py
