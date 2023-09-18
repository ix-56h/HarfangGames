import logging
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

logger = logging.getLogger(__name__) 

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "")
 
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        logger.info("New database session.")
        yield db
    finally:
        logger.info("Database session closed.")
        db.close()

Base = declarative_base()