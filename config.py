import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    USER = os.getenv("user")
    PASSWORD = os.getenv("password")
    HOST = os.getenv("host")
    PORT = os.getenv("port")
    DBNAME = os.getenv("dbname")

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{USER}:{PASSWORD}"
        f"@{HOST}:{PORT}/{DBNAME}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False