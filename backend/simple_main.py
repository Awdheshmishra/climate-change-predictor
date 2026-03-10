from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from groq import Groq
import uvicorn
import os

# Load environment variables
load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure Groq AI
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
groq_client = None

if GROQ_API_KEY:
    try:
        groq_client = Groq(api_key=GROQ_API_KEY)
        print("🤖 Groq AI Connected Successfully! ✅")
    except Exception as e:
        print(f"❌ Groq Connection Error: {e}")
else:
    print("⚠️ GROQ_API_KEY not found in .env file")

class ChatRequest(BaseModel):
    message: str

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

@app.get("/api/city/{city_name}/quick")
async def get_city(city_name: str):
    cities = {
        "delhi": {
            "city": "Delhi",
            "current": {"temperature": 26.5, "aqi": 320, "rainfall_mm": 780},
            "prediction_2050": {"temperature": 29.8, "aqi": 450, "rainfall_mm": 700, "increase": 3.3},
            "recommendations": ["Implement odd-even vehicle scheme", "Use air purifiers indoors", "Increase green cover to 33%", "Control construction dust", "Promote public transport"]
        },
        "mumbai": {
            "city": "Mumbai",
            "current": {"temperature": 28.3, "aqi": 180, "rainfall_mm": 2200},
            "prediction_2050": {"temperature": 30.5, "aqi": 250, "rainfall_mm": 2000, "increase": 2.2},
            "recommendations": ["Protect coastal areas", "Install vertical gardens", "Improve waste management", "Conserve mangroves", "Implement flood control measures"]
        },
        "bangalore": {
            "city": "Bangalore",
            "current": {"temperature": 24.5, "aqi": 145, "rainfall_mm": 970},
            "prediction_2050": {"temperature": 27.0, "aqi": 200, "rainfall_mm": 880, "increase": 2.5},
            "recommendations": ["Conserve lakes", "Stop uncontrolled construction", "Make rainwater harvesting mandatory", "Transform IT city into green city"]
        },
        "chennai": {
            "city": "Chennai",
            "current": {"temperature": 29.5, "aqi": 165, "rainfall_mm": 1400},
            "prediction_2050": {"temperature": 32.0, "aqi": 220, "rainfall_mm": 1300, "increase": 2.5},
            "recommendations": ["Prioritize water conservation", "Install desalination plants", "Enhance rainwater harvesting", "Protect coastal infrastructure"]
        },
        "kolkata": {
            "city": "Kolkata",
            "current": {"temperature": 27.8, "aqi": 195, "rainfall_mm": 1580},
            "prediction_2050": {"temperature": 30.2, "aqi": 280, "rainfall_mm": 1450, "increase": 2.4},
            "recommendations": ["Preserve parks and green spaces", "Address water logging", "Control industrial emissions", "Create cycling lanes"]
        },
        "lucknow": {
            "city": "Lucknow",
            "current": {"temperature": 25.8, "aqi": 210, "rainfall_mm": 850},
            "prediction_2050": {"temperature": 28.5, "aqi": 340, "rainfall_mm": 780, "increase": 2.7},
            "recommendations": ["Tree plantation drives", "Clean Gomti river", "Promote metro and e-rickshaws", "Control industrial pollution"]
        },
        "hyderabad": {
            "city": "Hyderabad",
            "current": {"temperature": 28.0, "aqi": 175, "rainfall_mm": 850},
            "prediction_2050": {"temperature": 30.5, "aqi": 240, "rainfall_mm": 780, "increase": 2.5},
            "recommendations": ["Increase green cover", "Prioritize water conservation", "Strengthen public transport", "Protect lakes"]
        },
        "pune": {
            "city": "Pune",
            "current": {"temperature": 25.5, "aqi": 160, "rainfall_mm": 750},
            "prediction_2050": {"temperature": 28.0, "aqi": 220, "rainfall_mm": 680, "increase": 2.5},
            "recommendations": ["Tree plantation drives", "Control industrial pollution", "Promote electric vehicles", "Preserve green zones"]
        },
        "ahmedabad": {
            "city": "Ahmedabad",
            "current": {"temperature": 28.5, "aqi": 210, "rainfall_mm": 650},
            "prediction_2050": {"temperature": 31.0, "aqi": 280, "rainfall_mm": 580, "increase": 2.5},
            "recommendations": ["Water conservation critical", "Increase green cover", "Control industrial emissions", "Implement heat action plan"]
        },
        "jaipur": {
            "city": "Jaipur",
            "current": {"temperature": 27.5, "aqi": 195, "rainfall_mm": 550},
            "prediction_2050": {"temperature": 30.0, "aqi": 260, "rainfall_mm": 480, "increase": 2.5},
            "recommendations": ["Tree plantation", "Water harvesting", "Protect heritage sites", "Combat desertification"]
        }
    }
    return cities.get(city_name.lower(), cities["lucknow"])

@app.post("/api/chat")
async def chat(request: ChatRequest):
    if not groq_client:
        return {
            "response": "⚠️ AI Model not configured. Please check your API key.",
            "language": "english",
            "model": "error"
        }
    
    try:
        # System prompt for climate assistant
        system_prompt = """You are Climate AI Assistant, an expert climate scientist and environmental consultant.

**YOUR KNOWLEDGE BASE:**

**Global Climate Data:**
- Current Global Temperature: 15.14°C (2024)
- 2050 Projection: 16.50°C (+1.36°C increase)
- Current CO₂ Levels: 420 ppm (Pre-industrial: 280 ppm)
- Paris Agreement Target: Limit warming to 1.5°C

**City-Specific Predictions:**
- Delhi: 26.5°C → 29.8°C by 2050 (+3.3°C) - CRITICAL
- Mumbai: 28.3°C → 30.5°C by 2050 (+2.2°C) - Coastal Risk
- Bangalore: 24.5°C → 27.0°C by 2050 (+2.5°C) - Water Scarcity
- Chennai: 29.5°C → 32.0°C by 2050 (+2.5°C) - Water Crisis
- Kolkata: 27.8°C → 30.2°C by 2050 (+2.4°C) - Flooding
- Lucknow: 25.8°C → 28.5°C by 2050 (+2.7°C) - Air Quality
- Hyderabad: 28.0°C → 30.5°C by 2050 (+2.5°C)
- Pune: 25.5°C → 28.0°C by 2050 (+2.5°C)
- Ahmedabad: 28.5°C → 31.0°C by 2050 (+2.5°C) - Heat Waves
- Jaipur: 27.5°C → 30.0°C by 2050 (+2.5°C) - Desertification

**RESPONSE GUIDELINES:**
- Always respond in ENGLISH
- Use emojis to make responses engaging (🌍🌡️🌊🌱🏭💧🔥)
- Provide accurate, science-based information
- Give specific, actionable recommendations
- Be concise but comprehensive (100-300 words)
- Use bullet points for clarity
- End with positive, action-oriented message
- If unsure, admit it and suggest reliable sources (IPCC, NASA, NOAA)

**TOPICS YOU CAN DISCUSS:**
- Global warming and temperature rise
- Carbon emissions and greenhouse gases
- Air pollution and AQI
- Water crisis and conservation
- Sea level rise and coastal flooding
- Extreme weather events
- Renewable energy solutions
- Deforestation and biodiversity
- Sustainable practices
- Climate policies and agreements
- Green technology
- Individual and community actions"""

        user_message = f"""{system_prompt}

User Question: {request.message}

Please provide a helpful, accurate, and engaging response."""

        # Generate AI response using Groq
        completion = groq_client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            temperature=0.7,
            max_tokens=500,
            top_p=1
        )
        
        ai_response = completion.choices[0].message.content
        
        return {
            "response": ai_response,
            "language": "english",
            "model": "groq-llama3",
            "status": "success"
        }
    
    except Exception as e:
        print(f"AI Error: {str(e)}")
        return {
            "response": f"""🤖 **AI Service Temporarily Unavailable**

**Error:** {str(e)}

**But I can still help you with:**

📊 **Current Climate Data:**
• Global Temperature: 15.14°C
• 2050 Projection: 16.50°C
• CO₂ Levels: 420 ppm

🏙️ **City Predictions Available:**
Delhi, Mumbai, Bangalore, Chennai, Kolkata, Lucknow, Hyderabad, Pune, Ahmedabad, Jaipur

💡 **Quick Climate Tips:**
✅ Switch to renewable energy
✅ Plant more trees
✅ Use public transport
✅ Reduce, reuse, recycle
✅ Save water and energy

**Please try your question again!** 🌍""",
            "language": "english",
            "model": "fallback",
            "status": "error"
        }

@app.get("/api/cities")
async def get_cities():
    return {
        "cities": ["delhi", "mumbai", "kolkata", "chennai", "bangalore", "hyderabad", "pune", "ahmedabad", "jaipur", "lucknow"],
        "count": 10
    }

@app.get("/")
async def root():
    ai_status = "Active" if groq_client else "Not Configured"
    return {
        "message": "🌍 Climate Intelligence Hub API",
        "status": "Running",
        "version": "3.0 - AI Powered by Groq",
        "ai_model": "Groq Llama3 8B",
        "ai_status": ai_status
    }

if __name__ == "__main__":
    print("🚀 Climate Intelligence Hub API Starting...")
    print(f"🤖 AI Model: Groq Llama3 8B")
    print(f"🔑 API Key: {'Configured ✅' if GROQ_API_KEY else 'Not Found ❌'}")
    print("📊 Server: http://localhost:8000")
    print("🌍 Ready to serve climate data with AI!")
    uvicorn.run(app, host="0.0.0.0", port=8000)