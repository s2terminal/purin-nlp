from typing import Any
from os import makedirs
from os.path import join

from src.utils.requests.save_twitter_api import SaveTwitterAPI

import pandas

import streamlit
st = streamlit  # type: Any


def some_twitter_apis(query: str, times: int):
    next_token = None
    df = None
    progress_bar = st.progress(0)
    for i in range(times):
        progress_bar.progress(i / times)
        req = SaveTwitterAPI(query, next_token=next_token)
        res = req.get_response()
        next_token = res.get('meta', {}).get('next_token', None)
        if df is None:
            df = pandas.DataFrame(res['data'])
        else:
            df = pandas.concat([df, pandas.DataFrame(res['data'])])
    if type(df) is pandas.DataFrame:
        st.write(df)
        filedir = 'data/twitter_api_data'
        filepath = join(filedir, f'{query}.tsv')
        makedirs(filedir, exist_ok=True)
        df.to_csv(filepath, sep='\t')
        return filepath


def fetch_twitter(keyword: str):
    keyword = st.text_input("検索クエリ", keyword)
    if st.button("Twitterから取得"):
        filepath = some_twitter_apis(keyword, 20)
        st.write(f"`{filepath}`に保存されました")
