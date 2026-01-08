from fastapi import FastAPI

app = FastAPI(title="Green Productivity")

@app.get("/")
def health_check():
    return {"status": "ok"}
