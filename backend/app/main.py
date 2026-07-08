from fastapi import FastAPI

from app.api.analytics import router as analytics_router

app = FastAPI(
    title="HobbyFi Copilot API",
    version="1.0.0"
)

app.include_router(analytics_router)


@app.get("/")
def root():
    return {
        "message": "🚀 HobbyFi Copilot Backend Running"
    }