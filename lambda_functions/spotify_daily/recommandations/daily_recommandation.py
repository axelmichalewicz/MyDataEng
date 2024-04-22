import logging
import os

from slack.slack_logger import slack_logger
from spotify.spotify_client import Spotify

logger: logging.Logger = logging.getLogger(__name__)

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SLACK_CHANNEL = os.getenv("CHANNEL_KEY")


def handler(event, context):
    tracks_recommandations = Spotify(
        client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET
    ).get_recommandation(market="US", genre="metal")
    logger.info("Recommandations picked by Spotify API")
    slack_logger.post(channel=SLACK_CHANNEL, message="Your daily recommandation are")
    for track in tracks_recommandations:
        slack_logger.post(channel=SLACK_CHANNEL, message=track)
    logger.info("Recommandations sent to slack")
