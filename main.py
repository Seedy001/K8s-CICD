from fastapi import FastAPI
import os
import socket

app = FastAPI(title="Demo App", version=os.getenv("APP_VERSION", "v2"))


@app.get("/")
def root():
    return {
        "message": "🎉 Hello from demo-app V3 - survived node failure!",
        "version": os.getenv("APP_VERSION", "v3"),
        "pod": socket.gethostname(),
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/ready")
def ready():
    return {"status": "ready"}

@app.get("/compute/{n}")
def compute(n: int):
    if n < 0:
        return {"error": "n must be >= 0"}
    return {"n": n, "sum": n * (n + 1) // 2}