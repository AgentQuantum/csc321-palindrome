# csc321-palindrome

A palindrome checker implementation with comprehensive test coverage and CI/CD pipeline.

## Features

The palindrome checker function:
- ✅ Returns `True` if a word or phrase is a palindrome
- ✅ Handles mixed case letters (case-insensitive)
- ✅ Ignores spaces
- ✅ Ignores punctuation marks
- ✅ Handles numbers and numeric palindromes
- ✅ Handles edge cases (empty strings, None, single characters)

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd csc321-palindrome
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

```python
from palindrome import is_palindrome

# Basic palindromes
is_palindrome("racecar")  # True
is_palindrome("hello")    # False

# With mixed case
is_palindrome("Racecar")  # True

# With spaces
is_palindrome("a man a plan a canal panama")  # True

# With punctuation
is_palindrome("A man, a plan, a canal: Panama!")  # True

# With numbers
is_palindrome("12321")  # True
is_palindrome(12321)     # True (accepts integers)
```

## Testing

Run all tests with pytest:
```bash
pytest -v
```

Run tests with coverage:
```bash
pytest --cov=palindrome --cov-report=term-missing
```

## CI/CD

This repository includes GitHub Actions for:
- **Linting**: Uses `flake8` for code quality checks
- **Formatting**: Uses `black` for code formatting checks
- **Testing**: Runs `pytest` with coverage reporting

The CI pipeline runs automatically on:
- Push to `main` or `master` branch
- Pull requests to `main` or `master` branch

## Project Structure

```
csc321-palindrome/
├── palindrome.py          # Main palindrome checker function
├── test_palindrome.py     # Comprehensive test suite
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore rules
├── .github/
│   └── workflows/
│       └── ci.yml        # GitHub Actions CI workflow
└── README.md             # This file
```

## License

This project is for educational purposes.
