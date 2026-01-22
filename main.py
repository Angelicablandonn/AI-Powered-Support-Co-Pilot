from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from schemas import TicketRequest, TicketResponse
from llm import classify_ticket
from supabase_client import update_ticket

load_dotenv()

app = FastAPI(title="AI Support Co-Pilot API")

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/process-ticket", response_model=TicketResponse)
def process_ticket(ticket: TicketRequest):
    try:
        result = classify_ticket(ticket.description)

        if "category" not in result or "sentiment" not in result:
            raise ValueError("Invalid LLM response")

        update_ticket(
            ticket_id=ticket.ticket_id,
            category=result["category"],
            sentiment=result["sentiment"]
        )

        return result

    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500,
            detail="Error processing ticket"
        )
