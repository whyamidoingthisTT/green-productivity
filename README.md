# Green Productivity 

Green Productivity is a FastAPI-based backend service for a productivity and self-improvement application focused on focus sessions, task tracking, reflections, and analytics.
It follows clean architecture, uses SQLAlchemy ORM, Alembic for migrations, and is designed to scale with versioned APIs

## Features

- **Task Tracking**: Comprehensive task management with completion tracking
- **Focus Session Monitoring**: Track deep work sessions and focus time
- **Daily Reflections**: Record and analyze daily productivity patterns
- **Burnout Detection**: Analyze trends to identify early warning signs of burnout
- **Long-term Analytics**: View productivity trends over time to understand your sustainable work capacity
- **Sustainable Metrics**: Focus on quality and sustainability over pure quantity

## Tech Stack

- **Language**: Python
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Server**: Uvicorn
- **Validation**: Pydantic
- **Migrations**: Alembic for database versioning
- **API Framework**: FastAPI (assumed based on common Python project structure)

## Project Structure
```
green-productivity
│
├── alembic/                # Database migrations
│   ├── versions/
│   ├── env.py
│   ├── README
│   └── script.py.mako
│
├── app/
│   ├── api/
│   │   ├── v1/              # API version 1 routes
│   │   │   ├── analytics.py
│   │   │   ├── focus.py
│   │   │   ├── reflection.py
│   │   │   └── task.py
│   │   └── v2/              # Future version (empty)
│   │
│   ├── core/                # App core configs
│   │   ├── config.py
│   │   ├── database.py
│   │   └── deps.py
│   │
│   ├── models/              # SQLAlchemy models
│   │   ├── base.py
│   │   ├── focus_session.py
│   │   ├── reflection.py
│   │   └── task.py
│   │
│   ├── schemas/             # Pydantic schemas
│   │   ├── focus_session.py
│   │   ├── reflection.py
│   │   └── task.py
│   │
│   ├── services/            # Business logic
│   │   └── analytics.py
│   │
│   └── main.py              # FastAPI app entry point
│
├── scripts/
│   └── seed_data.sql        # Optional seed data
│
├── alembic.ini
├── requirements.txt
└── .gitignore

```

## Prerequisites

- Python 3.8 or higher
- PostgreSQL database
- pip (Python package manager)

## Usage

### Starting the Application
```bash
python app/main.py
```

The application will start and be accessible at `http://localhost:8000`.

### API Documentation

Once the application is running, you can access the interactive API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### Basic Workflow

1. **Tasks**: Add, update, delete tasks you want to accomplish
2. **Focus Sessions**: Record when you're doing deep work (start/ end a focus session)
3. **Daily Reflections**: End each day with a reflection on your productivity
4. **Analytics**: Check your dashboard for insights and burnout risk indicators using daily summary, weekly trends, mood correlation.

## Database Migrations

### Creating a new migration
```bash
alembic revision --autogenerate -m "Description of changes"
```

### Applying migrations
```bash
alembic upgrade head
```

### Rolling back migrations
```bash
alembic downgrade -1
```

## Scripts

The `scripts/` directory contains utility scripts for postgreSQL operations. Check script documentation for usage details.

## Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Contact the maintainer through the repository


--- 
