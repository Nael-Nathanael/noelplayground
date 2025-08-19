from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    """Return hello world."""
    return {"message": "Hello, world!"}
