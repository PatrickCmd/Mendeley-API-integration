from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import RedirectResponse
from mendeley_manager import MendeleyManager
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Read credentials from environment variables
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

if not CLIENT_ID or not CLIENT_SECRET or not REDIRECT_URI:
    raise RuntimeError("Missing CLIENT_ID, CLIENT_SECRET, or REDIRECT_URI in environment variables")

app = FastAPI()

# Initialize the MendeleyManager
manager = MendeleyManager(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)

@app.get("/")
def root():
    """Redirect the user to the Mendeley authorization URL."""
    auth_url = manager.get_auth_url()
    return RedirectResponse(auth_url)

@app.get("/callback")
async def callback(request: Request):
    """Handle the callback from Mendeley and exchange the authorization code for an access token."""
    try:
        # Extract the authorization code from the query parameters
        auth_code = request.query_params.get("code")
        if not auth_code:
            raise HTTPException(status_code=400, detail="Authorization code not provided")

        # Exchange the authorization code for an access token
        access_token = manager.get_access_token(auth_code)
        if not access_token:
            raise HTTPException(status_code=500, detail="Failed to fetch access token")

        # Return the access token (or handle it as needed)
        return {"access_token": access_token}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during callback: {e}")