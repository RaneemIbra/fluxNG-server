import os
from supabase import create_client, AsyncClient

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_ANON_KEY")

async_supabase: AsyncClient = create_client(SUPABASE_URL, SUPABASE_KEY)