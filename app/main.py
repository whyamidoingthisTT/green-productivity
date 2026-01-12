from fastapi import FastAPI
from app.api.v1 import task, focus, reflection

app = FastAPI(title="Green Productivity API")

app.include_router(task.router, prefix="/api/v1/tasks", tags=["Tasks"])
app.include_router(focus.router, prefix="/api/v1/focus", tags=["Focus Sessions"])
app.include_router(reflection.router, prefix="/api/v1/reflections", tags=["Daily Reflections"])

@app.get("/")
def health_check():
    return {"status": "ok"}
