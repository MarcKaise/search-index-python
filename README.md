# search-index-python

return index of given number in list.

## quick start

In your terminal, run python.

```sh
$ python3
```

Then type below command

```py
>>> from search_index import search_index
>>> search_index(2,[0,1,2])
2
```

## setup

### for mac
```sh
brew install python@3.12
brew install pipx
pipx ensurepath
pipx install pytest
```

## test

In your terminal, run pytest.

```sh
pytest -v test_search_index.py
```
