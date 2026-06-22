## Web App - About Tech part of project
- This is a Python web server for providing Core APIs, Core Transactional APIs for web app's functionality

## Tech Stack
- A web service, using FastAPI engineered for scalability, reliability and one of the core service in a cloud native distributed platform
- Service will leverage PostgrSQL for persistance, as database too need to be scalable to avoid bottlenecks, singlepoint of faiulre, hence expected to have a distributed database 
- Uses SQLAlchemy, Pydantic for type validation, Alembic for keeping DB migration automated and easier
- Some of the services needed to be driven, powered by AI, hence the project needs to be able to easily integrate to leverage the power of AI

## Engineering Practices
- Many best practices required for a production grade, enterprise system
    - API first thinking with documentation (powered by FastAPI but requires a good developer experience)
    - Observability first thinking, requires metrics, logging, traces easily integratable with Open Telemetry, cloud monitoring tools like Grafana or simillar 
    - Cloud native infrastructure for scalability, reliability
- Will accomodate AI assisted development practices, tools, automations

## Project structure
```shell
src/app/
├── api/             # API Route definitions (Controllers)
├── core/            # Configuration, security, and global constants
├── db/              # Database connection, engine setup, session management
├── models/          # SQLAlchemy database models
├── schemas/         # Pydantic request/response schemas
├── services/        # Business logic & CRUD operations
└── main.py          # Application entry point
```

## Development and Testing
To run the application locally:
```bash
uv run python -m app.main
```

To run the test suite (ensures database connection and session management):
```bash
PYTHONPATH=. uv run pytest tests/test_db.py
```

To run the applicaiton
```bash
uv run uvicorn app.main:app --reload
```

or using fastapi for development purpose only

```bash
uv run fastapi dev src/app/main.py
```