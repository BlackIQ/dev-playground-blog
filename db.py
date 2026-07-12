# SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Settings
from settings import settings

# Database Connection
POSTGRES_URL = settings.postgres_url

# Engine
engine = create_engine(POSTGRES_URL)

# Session
session = sessionmaker(bind=engine, autoflush=False, autocommit=False)
