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
from schemas import LLMQuery, LLMResponse, IngestionPayload

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

##### FastAPI Endpoints #####
# Define a health check URL.
@app.get("/health")
def health_check():
    """
    Health check endpoing for checking the health status of the app.
    """
    return { "status": "ok" }

# Define an ingest endpoint (stub)
@app.post("/ingest")
def ingest_document(payload: IngestionPayload):
    """ 
    Endpoint for uploading a TXT or PDF document and storing it in the vector database.
    """
    return { "ingest": "ok"}

# Define a query endpoint (stub)
@app.post("/query", response_model=LLMResponse)
def llm_query(request_query: LLMQuery):
    """
    Endpoint for querying the LLM and returning a query response.
    """
    return  LLMResponse(response_text="The llm_query endpoint is working.")

