"""Clean Code in Python - Chapter 3: General Traits of Good Code

> Packing / unpacking
Works for *args and **kwargs
"""
from dataclasses import dataclass


USERS = [(i, f"first_name_{i}", f"last_name_{i}") for i in range(1_000)]


@dataclass
class User:
    user_id: int
    first_name: str
    last_name: str


def bad_users_from_rows(dbrows) -> list:
    """A bad case (non-pythonic) of creating ``User``s from DB rows."""
    return [User(row[0], row[1], row[2]) for row in dbrows]


def users_from_rows(dbrows) -> list:
    """Create ``User``s from DB rows."""
    return [
        User(user_id, first_name, last_name)
        for (user_id, first_name, last_name) in dbrows
    ]


def users_from_rows2(dbrows) -> list:
    """Create ``User``s from DB rows."""
    return [User(*row) for row in dbrows]


# Very simple examples of packing and unpacking
"""
>>> mylist = [1,2,3,4]
>>> first, *rest = mylist
first = 1, rest = [2, 3, 4]
>>> *rest, last = mylist
rest = [1, 2, 3], last = 4
>>> first, *middle, rest = mylist
first = 1, middle = [2, 3], last = 4
"""
