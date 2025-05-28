# GitHub Org Utilities

This project provides generic utility functions for accessing nested mappings, fetching JSON from URLs, and memoizing class methods. It is built with Python 3.7+, follows PEP8 standards, and includes complete unit tests.

## 📁 Project Structure

```
.
├── utils.py             # Core utility functions
├── test_utils.py        # Unit tests using unittest & parameterized
├── README.md            # Project documentation
```

## 📆 Requirements

- Python 3.7+
- `requests`
- `parameterized`
- `pycodestyle==2.5.0`

Install dependencies:

```bash
pip install requests parameterized pycodestyle==2.5.0
```

## 🚀 Features

### `access_nested_map(nested_map, path)`

Safely access values in a deeply nested mapping using a sequence of keys.

```python
from utils import access_nested_map

nested = {"a": {"b": {"c": 3}}}
value = access_nested_map(nested, ["a", "b", "c"])  # returns 3
```

### `get_json(url)`

Sends a `GET` request to the provided URL and returns the response JSON as a Python dictionary.

```python
from utils import get_json

data = get_json("https://api.github.com")
```

### `memoize`

A decorator to cache the result of an instance method the first time it's called.

```python
from utils import memoize

class MyClass:
    @memoize
    def calculate(self):
        print("Calculating...")
        return 42

obj = MyClass()
print(obj.calculate)  # prints "Calculating..." then 42
print(obj.calculate)  # prints just 42 (cached)
```

## 🧪 Running Tests

Tests use `unittest` and `parameterized`.

Run tests with:

```bash
python3 test_utils.py
```

Sample test:

```python
from parameterized import parameterized
from utils import access_nested_map
import unittest

class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)
```

## ✅ Code Style

Follow PEP8 with `pycodestyle`.

To check:

```bash
python -m pycodestyle utils.py test_utils.py
```

## 🔐 Executable Scripts

Make scripts executable (Unix):

```bash
chmod +x *.py
```

Ensure shebang is included:

```python
#!/usr/bin/env python3
```

## 👤 Author

**Your Name**
GitHub: [Emmanuel-Ebiwari](https://github.com/Emmanuel-Ebiwari)

## 📜 License

Licensed under the MIT License.
