from os import makedirs
from os.path import exists, join
from urllib.parse import urlencode

import requests

from src.utils.base64 import base64encode


class SaveRequest():
    # 絶対パスはやめて環境変数から受け取ったほうが良い
    LOCAL_SAVE_BASE_DIR = '/app/data'
    LOCAL_SAVE_DIR = 'save_request'

    def __init__(self, url: str, params: dict[str, str]) -> None:
        self.url = url
        self.params = params
        self.filename = f'{self._hash()}.html'

    def _hash(self):
        return base64encode("".join([self.url, urlencode(self.params)]))

    def _local_save_dir(self):
        return join(self.LOCAL_SAVE_BASE_DIR, self.LOCAL_SAVE_DIR)

    def get_response(self) -> str:
        if self._exists_local():
            print('use local data')
            return self._load_local()
        print('use HTTP get')
        ret = self._http_request()
        self._save_local(ret)
        return ret

    def _http_request(self) -> str:
        res = requests.get(self.url, params=self.params)
        return res.text

    def _exists_local(self):
        return exists(join(self._local_save_dir(), self.filename))

    def _load_local(self) -> str:
        with open(join(self._local_save_dir(), self.filename), mode='r') as f:
            return f.read()

    def _save_local(self, content: str):
        makedirs(self._local_save_dir(), exist_ok=True)
        with open(join(self._local_save_dir(), self.filename), mode='w') as f:
            f.write(content)
