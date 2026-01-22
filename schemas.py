from pydantic import BaseModel

class TicketRequest(BaseModel):
    ticket_id: str
    description: str

class TicketResponse(BaseModel):
    category: str
    sentiment: str
