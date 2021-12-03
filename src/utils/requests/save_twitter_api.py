from json import dumps, loads
from os import environ

from src.utils.requests.save_request import SaveRequest
import requests


# see: https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent
class SaveTwitterAPI(SaveRequest):
    LOCAL_SAVE_DIR = 'save_request/twitter'
    TWITTER_API_SEARCH_URL = 'https://api.twitter.com/2/tweets/search/recent'
    FILENAME_EXTENSION = 'json'

    def __init__(self, query: str, next_token: str = None) -> None:
        params = {'query': query, 'max_results': 100}
        if next_token:
            params['next_token'] = next_token
        super().__init__(url=self.TWITTER_API_SEARCH_URL, params=params)

    def _http_request(self) -> str:
        token = environ['TWITTER_BEARER_TOKEN']
        res = requests.get(self.url,
                           params=self.params,
                           headers={'Authorization': f'Bearer {token}'})
        return dumps(res.json(), ensure_ascii=False)

    def get_response(self):
        res_str = super().get_response()
        return loads(res_str)
