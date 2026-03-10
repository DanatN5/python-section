from dataclasses import dataclass, field
from itertools import batched
from typing import Iterable, TypeAlias

SomeRemoteData: TypeAlias = int


@dataclass
class Query:
    per_page: int = 3
    page: int = 1


@dataclass
class Page:
    per_page: int = 3
    results: Iterable[SomeRemoteData] = field(default_factory=list)
    next: int | None = None


def request(query: Query) -> Page:
    data = [i for i in range(0, 10)]
    chunks = list(batched(data, query.per_page))
    return Page(
        per_page=query.per_page,
        results=chunks[query.page - 1],
        next=query.page + 1 if query.page < len(chunks) else None,
    )


class RetrieveRemoteData:
    def __init__(self, per_page):
        self.per_page = per_page
        self.page = Page(per_page=per_page, next=1)

    def __iter__(self):
        while self.page.next is not None:
            self.page = request(Query(per_page=self.per_page, page=self.page.next))
            yield from self.page.results

    


class Fibo:
    def __init__(self, n: int):
        self.until: int = n
        self.counter: int = 0
        self.seq: list = [0, 1, 1]

    def __iter__(self):
        return self
    
    def __next__(self) -> int:

        if self.until == self.counter:
            raise StopIteration

        elif len(self.seq) > self.counter:
            val = self.seq[self.counter]
            self.counter  += 1
            return val
        else:
            new_val = self.seq[-1] + self.seq[-2]
            self.seq.append(new_val)
            self.counter  += 1
            return new_val
