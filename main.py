# FastAPI
from fastapi import FastAPI

# Routers
from routers import (
    category,
    tag,
)

# The FastAPI Instance
app = FastAPI(
    title="Mahi Blog API",
    version="1.0.0",
    summary="A simple Backend as our third project to use APIs in ReactJs",
    description="",
    openapi_tags=[
        {"name": "Application", "description": "Application endpoints like root and ping"},
        {"name": "Category", "description": "Category endpoint includes CRUD"},
        {"name": "Tag", "description": "Tag endpoint includes CRUD"},
    ]
)


@app.get("/", tags=["Application"])
async def root():
    return {"message": "Server is functioning"}


@app.get("/api", tags=["Application"])
async def api():
    return {"message": "Welcome to Mahi Todo List API"}


# Router
app.include_router(category.router, prefix="/api")
app.include_router(tag.router, prefix="/api")
