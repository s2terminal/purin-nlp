from src.utils.requests.save_twitter_api import SaveTwitterAPI

import pandas


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
        df.to_csv('data/twitter_api_data.tsv', sep='\t')


if __name__ == '__main__':
    some_twitter_apis('プリン', 20)
