from fastapi import FastAPI

from app.api.v1 import task as task_api
from app.api.v1 import focus as focus_api
from app.api.v1 import reflection as reflection_api
from app.api.v1 import analytics as analytics_api
from app.core.database import engine, Base

app = FastAPI(title="Green Productivity API")

app.include_router(task_api.router, prefix="/api/v1/tasks", tags=["Tasks"])
app.include_router(focus_api.router, prefix="/api/v1/focus", tags=["Focus Sessions"])
app.include_router(reflection_api.router, prefix="/api/v1/reflections", tags=["Daily Reflections"])
app.include_router(analytics_api.router, prefix="/api/v1/analytics", tags=["Analytics"])

@app.on_event('startup')
def startup():
    Base.metadata.create_all(bind=engine)
    
@app.get("/")
def health_check():
    return {"status": "ok"}
