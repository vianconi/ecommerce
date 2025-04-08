import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://postgres:Password2025@localhost:5432/ecommerce")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
