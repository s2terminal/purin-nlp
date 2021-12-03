from os import makedirs
from os.path import exists
from urllib.parse import urlencode

import requests

from src.utils.base64 import base64encode


class SaveRequest():
    # 絶対パスはやめて環境変数から受け取ったほうが良い
    LOCAL_SAVE_DIR = '/app/data/save_request'

    def __init__(self, url: str, params: dict[str, str]) -> None:
        self.url = url
        self.params = params
        self.filename = f'{self._hash()}.html'

    def _hash(self):
        return base64encode("".join([self.url, urlencode(self.params)]))

    def get_response(self) -> str:
        if self._exists_local():
            print('use local data')
            return self._load_local()
        print('use HTTP get')
        response = requests.get(self.url, params=self.params)
        ret = response.text
        self._save_local(ret)
        return ret

    def _exists_local(self):
        return exists(f'{self.LOCAL_SAVE_DIR}/{self.filename}')

    def _load_local(self) -> str:
        with open(f'{self.LOCAL_SAVE_DIR}/{self.filename}', mode='r') as f:
            return f.read()

    def _save_local(self, content: str):
        makedirs(self.LOCAL_SAVE_DIR, exist_ok=True)
        with open(f'{self.LOCAL_SAVE_DIR}/{self.filename}', mode='w') as f:
            f.write(content)
