import os
from dotenv import load_dotenv
import cloudinary
import cloudinary.uploader

load_dotenv()

class Config:
    # Base de datos
    USER = os.getenv("user")
    PASSWORD = os.getenv("password")
    HOST = os.getenv("host")
    PORT = os.getenv("port")
    DBNAME = os.getenv("dbname")

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Cloudinary
    CLOUD_NAME = os.getenv("cloudinary_cloud_name")
    API_KEY  = os.getenv("cloudinary_api_key")
    API_SECRET = os.getenv("cloudinary_api_secret")

    cloudinary.config(
        cloud_name=CLOUD_NAME,
        api_key=API_KEY,
        api_secret=API_SECRET,
        secure=True
    )
