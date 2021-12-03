from json import dumps, loads
from os import environ

from src.utils.requests.save_request import SaveRequest
import requests


class SaveTwitterAPI(SaveRequest):
    LOCAL_SAVE_DIR = 'save_request/twitter'
    TWITTER_API_SEARCH_URL = 'https://api.twitter.com/2/tweets/search/recent'

    def __init__(self, query: str) -> None:
        super().__init__(self.TWITTER_API_SEARCH_URL, {'query': query})

    def _http_request(self) -> str:
        token = environ['TWITTER_BEARER_TOKEN']
        res = requests.get(self.url,
                           params=self.params,
                           headers={'Authorization': f'Bearer {token}'})
        return dumps(res.json())

    def get_response(self):
        res_str = super().get_response()
        return loads(res_str)
