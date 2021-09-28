from fastapi import FastAPI, HTTPException

from .weirdtext.decoder import decode
from .weirdtext.encoder import encode

app = FastAPI()


@app.get("/v1/encode", response_model=str)
def encode_text(text: str) -> str:
    return encode(text)


@app.get("/v1/decode", response_model=str)
def decode_text(text: str) -> str:
    try:
        return decode(text)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
