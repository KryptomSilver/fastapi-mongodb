from fastapi import FastAPI
from routes.user import user

app = FastAPI(
    title="REST API with FastAPI and MongoDB",
    description="This is a simple REST API using FastAPI and MongoDB",
    version="1.0.0"
)

app.include_router(user)
