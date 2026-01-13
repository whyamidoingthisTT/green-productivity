from fastapi import FastAPI

# 🔹 Force SQLAlchemy model registration (NO name collision)
from app.models import task as task_model
from app.models import focus_session as focus_model
from app.models import reflection as reflection_model

# 🔹 API routers (ALISED clearly)
from app.api.v1 import task as task_api
from app.api.v1 import focus as focus_api
from app.api.v1 import reflection as reflection_api
from app.api.v1 import analytics as analytics_api

app = FastAPI(title="Green Productivity API")

# 🔹 Register routers
app.include_router(task_api.router, prefix="/api/v1/tasks", tags=["Tasks"])
app.include_router(focus_api.router, prefix="/api/v1/focus", tags=["Focus Sessions"])
app.include_router(reflection_api.router, prefix="/api/v1/reflections", tags=["Daily Reflections"])
app.include_router(analytics_api.router, prefix="/api/v1/analytics", tags=["Analytics"])

@app.get("/")
def health_check():
    return {"status": "ok"}
