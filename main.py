from fastapi import FastAPI

app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "FastAPI is working!"}

# Test endpoint with query parameter
@app.get("/hello")
def say_hello(name: str = "World"):
    return {"message": f"Hello, {name}!"}
