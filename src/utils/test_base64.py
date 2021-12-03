from src.utils.base64 import base64decode, base64encode
import re

def test_base64():
    assert base64decode(base64encode('テキスト')) == 'テキスト'
    assert re.match(r'[a-zA-Z0-9]+', base64encode('テキスト'))
