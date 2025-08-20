# Sprint Package Installation

## Quick Install

### Option 1: Install from local source (development)
```bash
# Clone the repository
git clone <your-repo-url>
cd sprint

# Install with Poetry
poetry install

# Or install with pip in development mode
pip install -e .
```

### Option 2: Install from built package
```bash
# Build the package first
poetry build

# Install the built wheel
pip install dist/sprint-0.1.0-py3-none-any.whl
```

## Usage

```python
import sprint

# Basic usage
sprint.printok("Success message")
sprint.printinfo("Info message")
sprint.printwarn("Warning message")
sprint.printfail("Error message")

# With indentation
sprint.printok("Indented message", lvl=2)

# With custom formatting
sprint.printinfo("Custom message", bold=True, max_line_length=60)
```

## Dependencies

- Python 3.7+
- colorama (for cross-platform colors)

## Development

```bash
# Install development dependencies
poetry install

# Run tests
poetry run pytest

# Build package
poetry build

# Publish to PyPI (when ready)
poetry publish
```
