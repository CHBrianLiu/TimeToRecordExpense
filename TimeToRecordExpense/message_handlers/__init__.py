from functools import partial

import linebot.models

from TimeToRecordExpense import config
from TimeToRecordExpense.message_handlers import message_event_handler

from .message_event_handler import handle_text_message_event

handler = linebot.WebhookHandler(config.LINE_CHANNEL_SECRET)
linebot_client = linebot.LineBotApi(config.LINE_CHANNEL_ACCESS_TOKEN)

handler.add(linebot.models.MessageEvent, message=linebot.models.TextMessage)(
    partial(handle_text_message_event, client=linebot_client)
)
