# Numbers Extract
Numbers extract from string

## Installation

```
pip install Numbers-Extract
```

## Usage

```py
import numbers_extract

string = """Hello,
You can contact me.
Ph No. +910000000000"""
print(numbers_extract.extract(string))
# => ['+910000000000']
```
