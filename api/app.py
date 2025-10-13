from fastapi import FastAPI

app = FastAPI(title="Dev API")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def root():
    return {"hello": "world"}
