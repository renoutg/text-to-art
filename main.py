from fastapi import FastAPI, Query, Response, Path, HTTPException, BackgroundTasks
from fastapi.responses import PlainTextResponse
from typing import Annotated
from enum import Enum
from art import text2art

class Font(str, Enum):
    random = "random"
    python_fontbro = "python-fontbro"
    block = "block"
    cybermedium = "cybermedium"
    alpha = "alpha"
    crawford = "crawford"
    impossible = "impossible"

app = FastAPI()

@app.get("/text_to_art/{font}/", response_class=PlainTextResponse)
def text_to_art(
    font: Font = Path(description="Font which should be used to print the art"),
    text: Annotated[str, Query(description="Text which should be converted to art")] = None,
):
    """
    Convert regular text to ascii art text
    """

    ascii_art = text2art(text,font=font)
    return ascii_art
