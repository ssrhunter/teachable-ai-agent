"""
Run using: uvicorn main:app --reload

Access the API
Once the server is running, you can access:
The API endpoint at 127.0.0.1.
The interactive API documentation (Swagger UI) at http://127.0.0.1:8000/docs.
The alternative API documentation (ReDoc) at http://127.0.0.1:8000/redoc. 

"""
from fastapi import FastAPI
from dotenv import load_dotenv
import os
import logging
from pythonjsonlogger import jsonlogger

# Make sure that the log dir exists.
os.makedirs('./log/', exist_ok=True)

# Set up logger
logger = logging.getLogger("app_logger")
logger.setLevel(logging.INFO)

# Create file handler
logHandler = logging.FileHandler('./log/app_logger.log')

# Set up JSON logger
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)
#test
logger.info("Application started", extra={"service": "api", "version": "1.0.0"})

# Load variables from .env into os.environment.
load_dotenv()
print(f"DEBUG_MODE: {os.getenv('DEBUG_MODE')}")

# Initialize an instance of FastAPI.
app = FastAPI()

# Define a health check URL.
@app.get("/health")
def health_check():
    return { "status": "ok" }
