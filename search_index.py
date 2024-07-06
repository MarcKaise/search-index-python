def search_index(num: int, list: list) -> int:
    for index, val in enumerate(list):
        if num is val:
            return index
    return -1
