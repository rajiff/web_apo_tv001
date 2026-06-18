# Claude System Prompt: Staff Engineer Mode (Python)

## 1. Environment & Package Management
* **Environment Execution**: NEVER run raw commands like `python` or `pytest`. ALWAYS prefix with `uv run python` or `uv run pytest`.
* **Dependency Management**: Use `uv add <pkg>`. Do NOT edit `pyproject.toml` or `requirements.txt` manually.
* **Lockfile Integrity**: Ensure lockfiles are automatically updated after adding dependencies.

## 2. Python Architecture & Coding Standards
* **Type Hints**: Type annotations are mandatory for all function signatures, arguments, and return values.
* **Static Analysis**: Code must pass `mypy --strict`. Do not use `Any` types unless absolutely unavoidable.
* **Formatting & Linting**: Strictly adhere to Black/Ruff standards (88-character line limit). Use `ruff check --fix`.
* **Anti-Pattern Prevention**: 
  * NEVER use mutable default arguments (e.g., `def task(items=[])`).
  * NEVER use wildcard imports (`from module import *`).
  * ALWAYS use context managers (`with` statements) for file/resource operations.
* **Clean Design**: Return early to minimize code nesting. Prefer `dataclasses` or Pydantic models for simple data containers.

## 3. Testing Strategy
* **Framework**: Use `pytest` exclusively.
* **Mocking**: Mock all external API endpoints, databases, and network requests.
* **Pattern**: Follow the Arrange-Act-Assert structure for test readability.

## 4. Automation Commands
* **Build/Environment**: `uv sync`
* **Run Tests**: `uv run pytest tests/ -x --tb=short`
* **Linting**: `uv run ruff check .`
* **Formatting**: `uv run ruff format .`
* **Type Check**: `uv run mypy src/`

