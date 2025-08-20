# Sprint Package Installation

## Quick Install

### Option 1: Install from local source (development)
```bash
# Clone the repository
git clone <your-repo-url>
cd sprint

# Install with uv (recommended)
uv pip install -e .

# Or install with pip in development mode
pip install -e .
```

### Option 2: Install from built package
```bash
# Build the package first with uv
uv build

# Install the built wheel
uv pip install dist/sprint-0.1.1-py3-none-any.whl

# Or with pip
pip install dist/sprint-0.1.1-py3-none-any.whl
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

- Python 3.10+
- colorama (for cross-platform colors)

## Development

```bash
# Install development dependencies with uv
uv pip install -e .

# Run tests (if pytest is installed)
pytest

# Or with uv
uv run pytest

# Build package
uv build

# Publish to PyPI (when ready)
uv publish
```
