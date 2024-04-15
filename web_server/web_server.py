import os
import zlib
import socket

import redis
import httpx
import requests

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Web Server")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
REDIS_PORT = os.environ.get("REDIS_PORT", "6379")
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD", "")
MODEL_SERVER_URL = os.environ.get("MODEL_SERVER_URL", "http://localhost:8080")


@app.on_event("startup")
async def initialize():
    global redis_pool
    print(f"creating redis connection with {REDIS_HOST=} {REDIS_PORT=}")
    redis_pool = redis.ConnectionPool(
        host=REDIS_HOST,
        port=REDIS_PORT,
        password=REDIS_PASSWORD,
        db=0,
        decode_responses=True,
    )


def get_redis():
    return redis.Redis(connection_pool=redis_pool)


async def check_cached(inp_text: str):
    hash = zlib.adler32(inp_text.encode("utf-8"))
    cache = get_redis()

    out_text = cache.get(hash)

    return out_text if out_text else None


@app.post("/textgen")
async def generate(inp_text: str):
    infer_cache = await check_cached(inp_text)

    if infer_cache == None:
        async with httpx.AsyncClient() as client:
            try:
                url = f"{MODEL_SERVER_URL}/generate"
                query_param = {"inp_text": inp_text}
                response = requests.post(url, params=query_param)
                # response = await client.post(url, params=query_param)
                return response.text

            except Exception as e:
                print(f"ERROR :: {e}")
                raise HTTPException(status_code=500, detail="Error from Model Endpoint")

    return f"[cached]: {infer_cache}"


@app.get("/")
async def root():
    return {
        "message": f"Welcome to EMLO-S17 Web Server @ {socket.gethostbyname(socket.gethostname())}"
    }


@app.get("/health")
async def health():
    return {"message": "ok"}


# uvicorn web_server:app --host 0.0.0.0 --port 9080 --reload
