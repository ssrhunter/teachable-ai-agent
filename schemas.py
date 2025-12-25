from pydantic import BaseModel, Field

##### Pydantic Schemas #####
class LLMQuery(BaseModel):
    query: str = Field(...)

class IngestionPayload(BaseModel):
    document: str = Field(...)

class LLMResponse(BaseModel):
    response_text: str = Field(...)
    