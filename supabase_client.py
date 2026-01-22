import os
from dotenv import load_dotenv
from supabase import create_client, Client

# 🔹 Cargar variables de entorno
load_dotenv()

SUPABASE_URL: str = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_ROLE_KEY: str = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

# (opcional pero recomendado)
if not SUPABASE_URL or not SUPABASE_SERVICE_ROLE_KEY:
    raise RuntimeError("Faltan variables de entorno de Supabase")

supabase: Client = create_client(
    SUPABASE_URL,
    SUPABASE_SERVICE_ROLE_KEY
)

def update_ticket(ticket_id: str, category: str, sentiment: str):
    supabase.table("tickets").update({
        "category": category,
        "sentiment": sentiment,
        "processed": True
    }).eq("id", ticket_id).execute()
