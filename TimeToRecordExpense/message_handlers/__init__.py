import linebot.models

from TimeToRecordExpense import config
from TimeToRecordExpense.message_handlers import message_event_handler

handler = linebot.WebhookHandler(config.LINE_CHANNEL_SECRET)

handler.add(linebot.models.MessageEvent, message=linebot.models.TextMessage)
