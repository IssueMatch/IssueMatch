from fastapi import FastAPI

app = FastAPI(
    title="IssueMatch Recommender",
    description="Recommendation engine for GitHub issues",
    version="0.1.0",
)


@app.get("/internal/v1/health")
async def health_check():
    return {
        "status": "ok",
        "service": "recommender"
    }