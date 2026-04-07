import os

API_ID    = os.environ.get("API_ID", "29719806")
API_HASH  = os.environ.get("API_HASH", "c8e87805739aa77bd5bd4076148a9a66")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8870))  # Default to 8000 if not set
