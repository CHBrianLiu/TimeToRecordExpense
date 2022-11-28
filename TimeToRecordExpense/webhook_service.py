import logging

import linebot.exceptions
from fastapi import FastAPI, Header, Request, Response

from TimeToRecordExpense import message_handlers

app = FastAPI()


@app.post("/callback")
async def callback(request: Request, x_line_signature: str = Header()):
    body = (await request.body()).decode("utf-8")
    try:
        message_handlers.handler.handle(body, x_line_signature)
    except linebot.exceptions.InvalidSignatureError:
        logging.warning("invalid request: signature validation failed.")
        return Response(status_code=400)
    return Response(status_code=200)
