import os

import httpx


def send_message() -> None:
    url = f"https://discord.com/api/v9/channels/{os.getenv('CHANNEL_DISCORD')}/messages"
    auth = {"authorization": os.getenv("TOKEN_DISCORD")}
    msg = {"content": "$p"}
    httpx.post(url=url, headers=auth, data=msg)
