from sqlalchemy import Boolean, Column, String, CheckConstraint, BigInteger
from dependencies.db import Base

class User(Base):
    __tablename__ = "user"

    id = Column(BigInteger, CheckConstraint('id > 0'), primary_key=True, index=True, autoincrement=True)
    email = Column(String, unique=True, index=True, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)