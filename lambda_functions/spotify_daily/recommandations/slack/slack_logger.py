import os

from slack_sdk import WebClient


class SlackLogger:
    def __init__(self):
        token = os.getenv("SLACK_BOT_TOKEN")
        self.client = WebClient(token=token)

    def post(self, channel, message: str):
        self.client.chat_postMessage(channel=channel, text=message)


slack_logger = SlackLogger()


class logger:
    def __init__(self, context):
        self.context = context
        self.slack_logger = slack_logger

    def info(self, message: str):
        self.context.log.info(message)
