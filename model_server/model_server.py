import os
import zlib
import socket

import redis

from transformers import GPT2Tokenizer, GPT2LMHeadModel


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Model Server")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

HF_MODEL = os.environ.get("HF_MODEL", "gpt2")
REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
REDIS_PORT = os.environ.get("REDIS_PORT", "6379")
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD", "")


@app.on_event("startup")
async def initialize():
    # initializes model, categories, redis connection
    global model
    global tokenizer
    print(f"loading model {HF_MODEL=}...")
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2", pad_token_id=tokenizer.eos_token_id)
    model.eval()
    print(f"loaded model {HF_MODEL=}")

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
    # Here, we re-use our connection pool
    # not creating a new one
    return redis.Redis(connection_pool=redis_pool)


async def write_to_cache(inp_text: str, out_text: str) -> None:
    cache = get_redis()

    hash = zlib.adler32(inp_text.encode("utf-8"))
    cache.set(hash, out_text)


@app.post("/generate")
async def generate(inp_text: str):
    encoded_input = tokenizer.encode(inp_text, return_tensors="pt")
    out = model.generate(encoded_input, max_new_tokens=100)
    out_text = tokenizer.decode(out[0], skip_special_tokens=True)

    await write_to_cache(inp_text, out_text)
    return out_text


@app.get("/health")
async def health():
    return {"message": "ok"}


@app.get("/")
async def root():
    return {
        "message": f"Welcome to EMLO-S17 Model Server @ {socket.gethostbyname(socket.gethostname())}"
    }


# uvicorn model_server:app --host 0.0.0.0 --port 8080 --reload
