from src.utils.requests.save_twitter_api import SaveTwitterAPI
from time import sleep


def some_twitter_apis(query: str, times: int):
    next_token = None
    for _i in range(times):
        sleep(1)
        req = SaveTwitterAPI(query, next_token=next_token)
        res = req.get_response()
        next_token = res.get('meta', {}).get('next_token', None)


if __name__ == '__main__':
    some_twitter_apis('プリン', 20)
