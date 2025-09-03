# Project Structure

The repository is organized as follows:

```text
.
├── app/                    # Backend FastAPI application
│   ├── __init__.py         # Package initialization
│   ├── main.py             # Application entry point
│   ├── models.py           # SQLAlchemy models
│   ├── crud.py             # CRUD operations
│   ├── schemas.py          # Pydantic schemas
│   ├── database.py         # Database session and engine
│   ├── core/               # Core and config
│   │   ├── __init__.py     # Package initialization
│   │   └── config.py       # Configs
│   └── routers/            # API route modules
│       ├── __init__.py     # Package initialization
│       └── locations.py    # Location-related endpoints
│
├── docs/                   # Documentation
│   ├── contributing.md     # Contribution guidelines
│   ├── database.md         # Database documentation
│   ├── index.md            # Documentation index
│   ├── project-structure.md# Project structure (this file)
│   └── technologies.md     # Tech stack details
│
├── frontend/               # Frontend application
│   ├── node_modules/       # Node.js dependencies
│   ├── public/             # Public static files
│   ├── package.json        # Frontend dependencies
│   ├── package-lock.json   # Frontend lockfile
│   └── src/                # Source code (React/JS components)
│
├── img/                    # Project-related images
├── venv/                   # Python virtual environment
│
├── .env                    # Environment variables
├── .env.example            # Example environment variables
├── .gitignore              # Git ignore file
├── mkdocs.yml              # MkDocs configuration
├── README.md               # Project overview
└── requirements.txt        # Python dependencies
```


  