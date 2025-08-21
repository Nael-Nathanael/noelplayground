from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    """Return hello world."""
    return {"message": "Hello, world!"}

@app.get("/world")
async def hello():
    """PPLSPCLAS"""
    return {"message": "Hello"}