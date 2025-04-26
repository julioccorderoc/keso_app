# TODO: make this platform agnostic (not only for supabase)

import os
from supabase import Client, create_client
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

def get_db_client() -> Client | None:
    """
    Initializes and returns the Supabase client.
    Handles potential missing configuration. 
    Returns None if config missing.
    """
    if not SUPABASE_URL or not SUPABASE_KEY:
        print("Error: SUPABASE_URL and SUPABASE_KEY environment variables must be set.")
        return None
    try:
        # Standard client creation (returns async-capable client in v2+)
        client = create_client(SUPABASE_URL, SUPABASE_KEY)
        return client
    except Exception as e:
        print(f"Error creating Supabase client: {e}")
        return None