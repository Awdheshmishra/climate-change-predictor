from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
        "lucknow": {
            "city": "Lucknow",
            "current": {"temperature": 25.8, "aqi": 210, "rainfall_mm": 850},
            "prediction_2050": {"temperature": 28.5, "aqi": 340, "rainfall_mm": 780, "increase": 2.7},
            "recommendations": ["🌳 Tree plantation karo", "💧 Water conservation", "🚲 Public transport use karo", "🏭 Pollution control"]
        },
        "delhi": {
            "city": "Delhi",
            "current": {"temperature": 26.5, "aqi": 320, "rainfall_mm": 780},
            "prediction_2050": {"temperature": 29.8, "aqi": 450, "rainfall_mm": 700, "increase": 3.3},
            "recommendations": ["🚗 Odd-even scheme lagao", "🌫️ Air purifiers use karo", "🌳 Green cover badhao", "🏗️ Dust control karo"]
        },
        "mumbai": {
            "city": "Mumbai",
            "current": {"temperature": 28.3, "aqi": 180, "rainfall_mm": 2200},
            "prediction_2050": {"temperature": 30.5, "aqi": 250, "rainfall_mm": 2000, "increase": 2.2},
            "recommendations": ["🌊 Coastal protection karo", "🏙️ Vertical gardens lagao", "♻️ Waste management improve karo", "🚇 Public transport badhao"]
        },
        "kolkata": {
            "city": "Kolkata",
            "current": {"temperature": 27.8, "aqi": 195, "rainfall_mm": 1580},
            "prediction_2050": {"temperature": 30.2, "aqi": 280, "rainfall_mm": 1450, "increase": 2.4},
            "recommendations": ["🌳 Parks bachao", "💧 Water logging solution", "🏭 Emissions control", "🚲 Cycle lanes banao"]
        },
        "bangalore": {
            "city": "Bangalore",
            "current": {"temperature": 24.5, "aqi": 145, "rainfall_mm": 970},
            "prediction_2050": {"temperature": 27.0, "aqi": 200, "rainfall_mm": 880, "increase": 2.5},
            "recommendations": ["🌳 Lake conservation", "🏗️ Construction roko", "💧 Rainwater harvesting", "🌿 Green city banao"]
        }
    }
    return cities.get(city_name.lower(), cities["lucknow"])

@app.post("/api/chat")
async def chat(request: ChatRequest):
    message = request.message.lower()
    
    if "lucknow" in message:
        response = """🏙️ **Lucknow ka Climate Prediction:**

📊 Current Temp: 25.8°C
🔮 2050 tak: 28.5°C
📈 Increase: +2.7°C

⚠️ Temperature badh raha hai!

💡 Suggestions:
• Tree plantation badhao
• Gomti river clean karo
• Metro use badhao"""
    
    elif "delhi" in message:
        response = """🏙️ **Delhi ka Climate Prediction:**

📊 Current Temp: 26.5°C
🔮 2050 tak: 29.8°C
📈 Increase: +3.3°C

⚠️ Sabse zyada risk!

💡 Suggestions:
• Odd-even scheme lagao
• Air purifiers use karo
• Green cover badhao"""
    
    elif "mumbai" in message:
        response = """🏙️ **Mumbai ka Climate Prediction:**

📊 Current Temp: 28.3°C
🔮 2050 tak: 30.5°C
📈 Increase: +2.2°C

🌊 Sea level rise ka risk!

💡 Suggestions:
• Coastal protection karo
• Vertical gardens lagao
• Waste management improve karo"""
    
    elif "temp" in message or "temperature" in message:
        response = """🌡️ **Global Temperature:**

📊 Current (2024): 15.14°C
🔮 2050 Prediction: 16.50°C
📈 Total Rise: +1.36°C

⚠️ Paris Agreement target: <1.5°C"""
    
    elif "carbon" in message or "emission" in message:
        response = """🏭 **Carbon Emissions:**

📊 Current CO₂: 420 ppm
📈 Pre-industrial: 280 ppm

🎯 Target:
• 2030 tak 45% reduction
• 2050 tak Carbon Neutrality"""
    
    elif "2050" in message or "future" in message:
        response = """🔮 **2050 Tak Ka Scenario:**

🌡️ Temperature: 1.5-3°C increase
🌊 Sea Level: 30-50cm rise
💧 Water Scarcity: Badh jayegi

✅ Action lo toh bach sakte hain!"""
    
    elif "help" in message or "madad" in message:
        response = """🤖 **Main kaise help karu:**

1️⃣ City prediction: "Lucknow temp"
2️⃣ Global info: "Temperature kya hai"
3️⃣ Solutions: "Kya kar sakte hain"

Kya janna hai?"""
    
    else:
        response = """🤔 Samajh nahi aaya bhai.

Try karo:
• "Lucknow climate"
• "Delhi temperature"
• "2050 kya hoga"
• "Help" """
    
    return {"response": response, "language": "hinglish"}

@app.get("/api/cities")
async def get_cities():
    return {"cities": ["lucknow", "delhi", "mumbai", "kolkata", "bangalore"], "count": 5}

@app.get("/")
async def root():
    return {"message": "🌍 Climate Intelligence Hub API", "status": "Running"}
@app.route("/")
def home():
    return {"message": "Climate backend running"}

if __name__ == "__main__":
    print("🚀 Backend starting on http://localhost:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)