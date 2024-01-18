from fastapi import FastAPI

from routers.product import router as product_router
from routers.users import router as user_router
from routers.auth import router as auth_router

from dependencies.db import engine, Base


app = FastAPI()


# Initialize SQL database tables
Base.metadata.create_all(bind=engine)


app.include_router(product_router, prefix="/api/v1", tags=["Product"])
app.include_router(user_router, prefix="/api/v1", tags=["User"])
app.include_router(auth_router, prefix="/api/v1", tags=["Auth"])



