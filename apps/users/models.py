from typing import NamedTuple


class User(NamedTuple):
    name: str
    text: str
    num: int

    def __str__(self):
        return f"{self.name}_{self.text}{self.num}"
