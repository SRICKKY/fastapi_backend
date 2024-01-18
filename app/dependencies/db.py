from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from motor.motor_asyncio import AsyncIOMotorClient
from contextlib import asynccontextmanager

# SQL Database Connection
DATABASE_URL = "postgresql://catalog_user:password@postgres:5432/product_catalog"


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# MongoDB Connection
MONGODB_URL = "mongodb://mongo:27017"
motor_client = AsyncIOMotorClient(MONGODB_URL)
mongo_db = motor_client.product_catalog

# Dependency to get SQL database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

        # yield mongo_db


# Dependency to get MongoDB client
@asynccontextmanager
async def create_mongo_client():
    motor_client = AsyncIOMotorClient("mongodb://mongo:27017")
    try:
        yield motor_client.product_catalog
    finally:
        motor_client.close()

async def get_mongo_db():
    async with create_mongo_client() as mongo_db:
        yield mongo_db

