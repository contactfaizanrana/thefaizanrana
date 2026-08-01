# To run this locally: pip install fastapi uvicorn pydantic
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import datetime

# Initialize the Python Backend App
app = FastAPI(title="Faizan Infrastructure API")

# Essential: This allows your GitHub Pages website to talk to this Python server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows requests from your github.io site
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the data structure matching your HTML form
class ContactRequest(BaseModel):
    name: str
    email: str
    message: str

# API Health Check Endpoint
@app.get("/")
def read_root():
    return {"status": "Python Backend is Live", "timestamp": datetime.datetime.utcnow()}

# The Endpoint that receives the form data from your GitHub Page
@app.post("/contact")
def process_contact_form(request: ContactRequest):
    # Here you would typically write code to save this to a database (like Supabase)
    # or send an email notification to yourself.
    
    print(f"NEW INQUIRY RECEIVED from {request.name} ({request.email})")
    print(f"Message: {request.message}")
    
    if not request.email or "@" not in request.email:
        raise HTTPException(status_code=400, detail="Invalid Email Architecture")
        
    return {
        "status": "success",
        "message": "Transmission received. Data logged securely.",
        "processed_by": "FastAPI (Python)"
    }

# Run the server using: uvicorn main:app --reload
