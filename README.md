# Pudding-Jigglypuff Disambiguation

```
$ docker-compose up
```

## データ取得
```
$ docker-compose run --rm app poetry run python src/tasks/fetch_twitter.py
```

open 'data/twitter_api_data.tsv'

## Testing
```
$ docker-compose run --rm app poetry run pytest
```
