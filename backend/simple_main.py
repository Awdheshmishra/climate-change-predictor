from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import os

app = FastAPI()

# Allow frontend requests (important for deployment)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str


@app.get("/")
async def root():
    return {
        "message": "🌍 Climate Intelligence Hub API",
        "status": "Running"
    }


@app.get("/api/climate-data")
async def get_climate_data():
    return {
        "current_temp": 15.14,
        "forecast_2050": 16.50,
        "confidence": 98.4,
        "historical_years": list(range(1980, 2025)),
        "historical_temps": [14.12 + (i * 0.023) for i in range(45)],
        "future_predictions": [15.14 + (i * 0.05) for i in range(26)],
        "co2_levels": [338 + (i * 1.8) for i in range(45)]
    }


@app.post("/api/chat")
async def chat(request: ChatRequest):

    message = request.message.lower()

    if "lucknow" in message:
        response = """🏙️ Lucknow Climate

Current Temp: 25.8°C  
2050 Prediction: 28.5°C  

Suggestions:
• Tree plantation badhao  
• Gomti river clean rakho  
• Metro aur public transport use karo
"""

    elif "delhi" in message:
        response = """🏙️ Delhi Climate

Current Temp: 26.5°C  
2050 Prediction: 29.8°C  

Suggestions:
• Odd-even traffic  
• Pollution control  
• Green cover badhao
"""

    elif "mumbai" in message:
        response = """🏙️ Mumbai Climate

Current Temp: 28.3°C  
2050 Prediction: 30.5°C  

Risk: Sea level rise
"""

    elif "temperature" in message or "temp" in message:
        response = """🌡️ Global Temperature

Current: 15.14°C  
2050 Prediction: 16.50°C  

Paris Agreement target < 1.5°C"""

    else:
        response = """🤖 Aap ye try kar sakte ho:

• Lucknow temperature  
• Delhi climate  
• Mumbai prediction  
• 2050 kya hoga
"""

    return {"response": response}


@app.get("/api/cities")
async def get_cities():
    return {
        "cities": ["lucknow", "delhi", "mumbai", "kolkata", "bangalore"],
        "count": 5
    }


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)