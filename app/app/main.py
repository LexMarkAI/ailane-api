from fastapi import FastAPI

app = FastAPI(title="AIlane API")

@app.get("/")
def root():
    return {"status": "running", "service": "AIlane API"}

@app.get("/health")
def health():
    return {"ok": True}
