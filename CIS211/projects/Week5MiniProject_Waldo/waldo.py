Waldo = 'W'
Other = '.'


"""Main two Base Cases"""
def for_all(p: list, thing: str) -> bool:
    for item in p:
        if item != thing:
            return False
    return True


def there_exists(p: list, thing: str) -> bool:
    for item in p:
        if item == thing:
            return True
    return False


"""Inverting Columns and Rows"""
def invert(p: list) -> list:
    col_then_row = []
    for col in range (len(p[0])):
        new_list = []
        for row in range(len(p)):
            new_list.append(p[row][col])
        col_then_row.append(new_list)
    return col_then_row


"""4 Sub-cases Combining 2 Base Cases"""
def for_all_all(p: list) -> bool:
    for item in p:
        if not for_all(item, Waldo):
            return False
    return True


def for_all_there_exists(p: list) -> bool:
    for item in p:
        if not there_exists(item, Waldo):
            return False
    return True


def there_exists_there_exists(p: list) -> bool:
    for item in p:
        if there_exists(item, Waldo):
            return True
    return False


def there_exists_for_all(p:list) -> bool:
    for item in p:
        if for_all(item, Waldo):
            return True
    return False


"""Row Functions"""
def all_row_exists_waldo(p: list) -> bool:
    return for_all_there_exists(p)


def all_row_all_waldo(p: list) -> bool:
    return for_all_all(p)


def exists_row_exists_waldo(p:list) -> bool:
    return there_exists_there_exists(p)


def exists_row_all_waldo(p: list) -> bool:
    return there_exists_for_all(p)


"""Column Functions"""
def all_col_exists_waldo(p: list) -> bool:
    if len(p) == 0:
        return True
    return for_all_there_exists(invert(p))


def all_col_all_waldo(p: list) -> bool:
    return for_all_all(p)


def exists_col_exists_waldo(p:list) -> bool:
    return there_exists_there_exists(p)


def exists_col_all_waldo(p: list) -> bool:
    if len(p) == 0:
        return False
    return there_exists_for_all(invert(p))

