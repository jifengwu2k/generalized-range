# `generalized-range`

A flexible Python generator function that extends the capabilities of Python's built-in `range` to all types, using customizable comparator and successor functions.

## Installation

```bash
pip install generalized-range
```

## Usage

```python
# coding=utf-8
from __future__ import print_function
from generalized_range import generalized_range

for number in generalized_range(
    start=10,
    stop=14,
    step=1,
    comparator=lambda x, y: x < y,
    successor=lambda x: x + 1
):
    print(number)  # Output: 10, 11, 12, 13

for char in generalized_range(
    start='A',
    stop='F',
    step=2,
    comparator=lambda x, y: ord(x) < ord(y),
    successor=lambda x: chr(ord(x) + 1)
):
    print(char)  # Output: A, C, E

for number in generalized_range(
    start=5,
    stop=1,
    step=1,
    comparator=lambda x, y: x > y,
    successor=lambda x: x - 1
):
    print(number)  # Output: 5, 4, 3, 2
```

## Contributing

If you find a bug or have a new feature you'd like to implement, please feel free to submit a pull request or open an issue.

## License

This project is open-source and available under the MIT license. See the [LICENSE](LICENSE) file for more details.