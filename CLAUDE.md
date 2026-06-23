# Web Apo - FastAPI Web Application

A standard FastAPI project for providing core APIs and transactional APIs for web app functionality.

## Tech Stack
- **Framework**: FastAPI (Python web framework for scalability, reliability)
- **Database**: PostgreSQL with SQLAlchemy async ORM
- **Validation**: Pydantic models
- **Migrations**: Alembic
- **Test Framework**: pytest with asyncio support

## Project Structure
```
src/app/
├── api/               # API Route definitions (Controllers)
├── core/              # Configuration, security, and global constants
├── db/                # Database connection, engine setup, session management
├── models/            # SQLAlchemy database models
├── schemas/           # Pydantic request/response schemas
├── services/          # Business logic & CRUD operations
└── main.py            # Application entry point
```

## Development Commands

### Environment Setup
```bash
uv sync
```

### Run Application
```bash
uv run uvicorn app.main:app --reload
# or for development
uv run fastapi dev src/app/main.py
```

### Testing
```bash
PYTHONPATH=. uv run pytest tests/ -x --tb=short
```

### Code Quality
```bash
uv run ruff check .
uv run ruff format .
uv run mypy src/
```

## Key Configuration
- **Database URL**: `DATABASE_URL` environment variable (PostgreSQL async)
- **Pool Size**: `DB_POOL_SIZE` (default: 10)
- **SQL Echo**: `SQL_ECHO` (default: false)

## Engineering Practices
- API-first thinking with OpenAPI documentation
- Observability-first (metrics, logging, traces for OpenTelemetry integration)
- Cloud-native infrastructure ready
- Async/await patterns for async database operations
- Type hints on all function signatures
- Context managers for resource handling
