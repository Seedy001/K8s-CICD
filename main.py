from fastapi import FastAPI
import os
import socket

app = FastAPI(title="Demo App", version=os.getenv("APP_VERSION", "v1"))


@app.get("/")
def root():
    return {
        "message": "Hello from demo-app",
        "version": os.getenv("APP_VERSION", "v1"),
        "pod": socket.gethostname(),
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/ready")
def ready():
    return {"status": "ready"}
