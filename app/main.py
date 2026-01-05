from fastapi import FastAPI

# Create FastAPI instance
app = FastAPI(
    title="Task Manager API",
    description="Learning API Development from Scratch",
    version="1.0.0"
)

# Root endpoint
@app.get("/")
def read_root():
    """Welcome endpoint - your first API!"""
    return {
        "message": "Hello World! Welcome to your Task Manager API",
        "status": "running",
        "version": "1.0.0"
    }

# About endpoint
@app.get("/about")
def about():
    """Information about this API"""
    return {
        "name": "Task Manager API",
        "version": "1.0.0",
        "description": "My first API built while learning!",
        "author": "You!",
        "learning_module": "Module 2"
    }

# Health check endpoint
@app.get("/health")
def health_check():
    """Check if API is healthy"""
    return {
        "status": "healthy",
        "message": "API is running perfectly!"
    }

# Greeting endpoint with path parameter
@app.get("/hello/{name}")
def greet(name: str):
    """Greet someone by name"""
    return {
        "greeting": f"Hello, {name}!",
        "message": f"Welcome to the API, {name}"
    }
