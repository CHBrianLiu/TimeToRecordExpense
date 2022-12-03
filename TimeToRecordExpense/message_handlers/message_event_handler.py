from linebot import LineBotApi
from linebot.models import (MessageAction, MessageEvent, QuickReply,
                            QuickReplyButton, TextMessage, TextSendMessage)

done_quick_reply_button = QuickReplyButton(
    action=MessageAction("Recorded", text="!done")
)


def handle_text_message_event(event: MessageEvent, client: LineBotApi):
    message: TextMessage = event.message
    if message.text == "!":
        quick_reply = QuickReply(items=[done_quick_reply_button])
        message = TextSendMessage(text="select", quick_reply=quick_reply)
        client.reply_message(event.reply_token, message)
