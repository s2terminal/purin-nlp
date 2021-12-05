from typing import Any

from src.utils.requests.save_twitter_api import SaveTwitterAPI

import pandas

import streamlit
st = streamlit  # type: Any


def some_twitter_apis(query: str, times: int):
    next_token = None
    df = None
    for _i in range(times):
        req = SaveTwitterAPI(query, next_token=next_token)
        res = req.get_response()
        next_token = res.get('meta', {}).get('next_token', None)
        if df is None:
            df = pandas.DataFrame(res['data'])
        else:
            df = pandas.concat([df, pandas.DataFrame(res['data'])])
    if type(df) is pandas.DataFrame:
        filepath = 'data/twitter_api_data.tsv'
        df.to_csv(filepath, sep='\t')
        return filepath


def fetch_twitter(keyword: str):
    if st.button("Twitterから取得"):
        filepath = some_twitter_apis(keyword, 20)
        st.write(f"`{filepath}`に保存されました")
