from dataclasses import dataclass

from pydantic import BaseModel
from requests.api_request import APIRequest, HttpMethodEnum


class SpotifyToken(BaseModel):
    access_token: str
    token_type: str


@dataclass
class Spotify:
    client_id: str
    client_secret: str

    def get_spotify_token(self) -> SpotifyToken:
        HEADERS = {"Content-Type": "application/x-www-form-urlencoded"}
        params = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }
        url = "https://accounts.spotify.com"
        response = APIRequest(base_url=url).request(
            method=HttpMethodEnum.POST, endpoint="/api/token", headers=HEADERS, params=params
        )
        token = response.json()
        return SpotifyToken(access_token=token.get("access_token"), token_type=token.get("token_type"))

    def get_recommandation(self, market: str, genre: str) -> list:
        token = self.get_spotify_token()
        HEADERS = {"Authorization": f"{token.token_type} {token.access_token}", "Content-Type": "application/json"}
        params = {"limit": 10, "market": market, "seed_genres": genre}
        url = "https://api.spotify.com"
        response = APIRequest(base_url=url).request(
            method=HttpMethodEnum.GET, endpoint="/v1/recommendations", headers=HEADERS, params=params
        )
        tracks = [track["external_urls"]["spotify"] for track in response.json()["tracks"]]
        return tracks
