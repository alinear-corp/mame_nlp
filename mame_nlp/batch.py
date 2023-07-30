from typing import Generator, TypeVar, Protocol

T = TypeVar('T')

class CountableWithGetItem(Protocol):
    def __getitem__(self, item: slice) -> T:
        ...

    def __len__(self) -> int:
        ...


def batch_by_slice(
        data: CountableWithGetItem,
        batch_size: int,
        drop_last: bool=False,
) -> Generator[T, None, None]:
    assert batch_size > 0

    start: int = 0
    end: int = start + batch_size
    n: int = len(data)

    while end <= n:
        yield data[start:end]
        start = end
        end += batch_size

    if (not drop_last) and start < n:
        yield data[start:n]
