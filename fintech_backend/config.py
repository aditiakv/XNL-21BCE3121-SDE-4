import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:Aditi@localhost:5433/fintech_platform')
    SQLALCHEMY_TRACK_MODIFICATIONS = False