from dataclasses import dataclass
from enum import Enum
from typing import Callable, Optional

import backoff
import httpx


class HttpMethodEnum(str, Enum):
    GET = "GET"
    POST = "POST"


@dataclass
class APIRequest:
    base_url: str

    @backoff.on_exception(
        wait_gen=backoff.expo,
        exception=httpx.RequestError,
        max_tries=3,
        jitter=backoff.random_jitter,
    )
    def request(
        self,
        method: HttpMethodEnum,
        endpoint: str = "",
        headers: Optional[dict] = None,
        params: Optional[dict] = None,
        auth=None,
    ) -> httpx.Response:
        response = self.build_request_action(method)(
            f"{self.base_url}{endpoint}",
            headers=headers,
            params=params,
            auth=auth,
        )
        response.raise_for_status()

        return response

    @staticmethod
    def build_request_action(method: HttpMethodEnum) -> Callable:
        if method not in HttpMethodEnum:
            raise ValueError(f"Invalid Http Method: {method}")

        return {
            HttpMethodEnum.GET: httpx.get,
            HttpMethodEnum.POST: httpx.post,
        }.get(
            method
        )  # type: ignore
