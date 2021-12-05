# Pudding-Jigglypuff Disambiguation

```
$ docker-compose up
```

access http://localhost:8080/

`data/purin-tsv-sample.tsv`を参考に`data/purin-tsv.tsv`を配置

## Testing
```
$ docker-compose run --rm app poetry run pytest
```

## Linting
```
$ docker-compose run --rm app poetry run flake8
```
