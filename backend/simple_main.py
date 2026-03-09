from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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
        # INDIAN CITIES
        "delhi": {
            "city": "Delhi",
            "current": {"temperature": 26.5, "aqi": 320, "rainfall_mm": 780},
            "prediction_2050": {"temperature": 29.8, "aqi": 450, "rainfall_mm": 700, "increase": 3.3},
            "recommendations": ["🚗 Odd-even scheme lagao", "🌫️ Air purifiers use karo", "🌳 Green cover badhao"]
        },
        "mumbai": {
            "city": "Mumbai",
            "current": {"temperature": 28.3, "aqi": 180, "rainfall_mm": 2200},
            "prediction_2050": {"temperature": 30.5, "aqi": 250, "rainfall_mm": 2000, "increase": 2.2},
            "recommendations": ["🌊 Coastal protection karo", "🏙️ Vertical gardens lagao", "♻️ Waste management improve karo"]
        },
        "kolkata": {
            "city": "Kolkata",
            "current": {"temperature": 27.8, "aqi": 195, "rainfall_mm": 1580},
            "prediction_2050": {"temperature": 30.2, "aqi": 280, "rainfall_mm": 1450, "increase": 2.4},
            "recommendations": ["🌳 Parks bachao", "💧 Water logging solution", "🏭 Emissions control"]
        },
        "chennai": {
            "city": "Chennai",
            "current": {"temperature": 29.5, "aqi": 165, "rainfall_mm": 1400},
            "prediction_2050": {"temperature": 32.0, "aqi": 220, "rainfall_mm": 1300, "increase": 2.5},
            "recommendations": ["🌊 Coastal protection", "💧 Water conservation", "🌳 Tree plantation"]
        },
        "bangalore": {
            "city": "Bangalore",
            "current": {"temperature": 24.5, "aqi": 145, "rainfall_mm": 970},
            "prediction_2050": {"temperature": 27.0, "aqi": 200, "rainfall_mm": 880, "increase": 2.5},
            "recommendations": ["🌳 Lake conservation", "🏗️ Construction roko", "💧 Rainwater harvesting"]
        },
        "hyderabad": {
            "city": "Hyderabad",
            "current": {"temperature": 28.0, "aqi": 175, "rainfall_mm": 850},
            "prediction_2050": {"temperature": 30.5, "aqi": 240, "rainfall_mm": 780, "increase": 2.5},
            "recommendations": ["🌳 Green cover badhao", "💧 Water conservation", "🚲 Public transport"]
        },
        "pune": {
            "city": "Pune",
            "current": {"temperature": 25.5, "aqi": 160, "rainfall_mm": 750},
            "prediction_2050": {"temperature": 28.0, "aqi": 220, "rainfall_mm": 680, "increase": 2.5},
            "recommendations": ["🌳 Tree plantation", "🏭 Pollution control", "🚗 EV promote karo"]
        },
        "ahmedabad": {
            "city": "Ahmedabad",
            "current": {"temperature": 28.5, "aqi": 210, "rainfall_mm": 650},
            "prediction_2050": {"temperature": 31.0, "aqi": 280, "rainfall_mm": 580, "increase": 2.5},
            "recommendations": ["💧 Water conservation", "🌳 Green cover", "🏭 Industrial control"]
        },
        "jaipur": {
            "city": "Jaipur",
            "current": {"temperature": 27.5, "aqi": 195, "rainfall_mm": 550},
            "prediction_2050": {"temperature": 30.0, "aqi": 260, "rainfall_mm": 480, "increase": 2.5},
            "recommendations": ["🌳 Tree plantation", "💧 Water harvesting", "🏛️ Heritage protect karo"]
        },
        "lucknow": {
            "city": "Lucknow",
            "current": {"temperature": 25.8, "aqi": 210, "rainfall_mm": 850},
            "prediction_2050": {"temperature": 28.5, "aqi": 340, "rainfall_mm": 780, "increase": 2.7},
            "recommendations": ["🌳 Tree plantation karo", "💧 Water conservation", "🚲 Public transport use karo"]
        },
        "kanpur": {
            "city": "Kanpur",
            "current": {"temperature": 26.2, "aqi": 285, "rainfall_mm": 720},
            "prediction_2050": {"temperature": 29.0, "aqi": 380, "rainfall_mm": 650, "increase": 2.8},
            "recommendations": ["🏭 Industrial pollution control", "🌳 Green cover", "💧 Water management"]
        },
        "nagpur": {
            "city": "Nagpur",
            "current": {"temperature": 27.0, "aqi": 175, "rainfall_mm": 1100},
            "prediction_2050": {"temperature": 29.5, "aqi": 240, "rainfall_mm": 1000, "increase": 2.5},
            "recommendations": ["🌳 Orange city ko green banao", "💧 Water conservation", "🚗 EV promote karo"]
        },
        "indore": {
            "city": "Indore",
            "current": {"temperature": 26.0, "aqi": 165, "rainfall_mm": 950},
            "prediction_2050": {"temperature": 28.5, "aqi": 230, "rainfall_mm": 880, "increase": 2.5},
            "recommendations": ["♻️ Waste management", "🌳 Clean city maintain karo", "💧 Water conservation"]
        },
        "bhopal": {
            "city": "Bhopal",
            "current": {"temperature": 25.5, "aqi": 170, "rainfall_mm": 1050},
            "prediction_2050": {"temperature": 28.0, "aqi": 240, "rainfall_mm": 980, "increase": 2.5},
            "recommendations": ["🌳 Lakes protect karo", "🏭 Industrial control", "💧 Water management"]
        },
        "patna": {
            "city": "Patna",
            "current": {"temperature": 26.8, "aqi": 225, "rainfall_mm": 1050},
            "prediction_2050": {"temperature": 29.5, "aqi": 310, "rainfall_mm": 980, "increase": 2.7},
            "recommendations": ["💧 Flood control", "🌳 Green cover", "🏭 Pollution control"]
        },
        "vadodara": {
            "city": "Vadodara",
            "current": {"temperature": 28.0, "aqi": 185, "rainfall_mm": 800},
            "prediction_2050": {"temperature": 30.5, "aqi": 250, "rainfall_mm": 730, "increase": 2.5},
            "recommendations": ["🌳 Tree plantation", "🏭 Industrial control", "💧 Water conservation"]
        },
        "ghaziabad": {
            "city": "Ghaziabad",
            "current": {"temperature": 26.5, "aqi": 295, "rainfall_mm": 700},
            "prediction_2050": {"temperature": 29.5, "aqi": 400, "rainfall_mm": 630, "increase": 3.0},
            "recommendations": ["🌳 Green cover badhao", "🏭 Pollution control", "🚗 EV promote karo"]
        },
        "ludhiana": {
            "city": "Ludhiana",
            "current": {"temperature": 24.5, "aqi": 235, "rainfall_mm": 650},
            "prediction_2050": {"temperature": 27.0, "aqi": 320, "rainfall_mm": 580, "increase": 2.5},
            "recommendations": ["🏭 Industrial pollution control", "🌳 Tree plantation", "💧 Water management"]
        },
        "agra": {
            "city": "Agra",
            "current": {"temperature": 26.5, "aqi": 245, "rainfall_mm": 650},
            "prediction_2050": {"temperature": 29.0, "aqi": 330, "rainfall_mm": 580, "increase": 2.5},
            "recommendations": ["🏛️ Heritage protect karo", "🌳 Green cover", "🏭 Pollution control"]
        },
        "nashik": {
            "city": "Nashik",
            "current": {"temperature": 25.5, "aqi": 155, "rainfall_mm": 750},
            "prediction_2050": {"temperature": 28.0, "aqi": 220, "rainfall_mm": 680, "increase": 2.5},
            "recommendations": ["🍇 Wine city ko green banao", "💧 Water conservation", "🌳 Tree plantation"]
        },
        "faridabad": {
            "city": "Faridabad",
            "current": {"temperature": 26.8, "aqi": 285, "rainfall_mm": 680},
            "prediction_2050": {"temperature": 29.5, "aqi": 380, "rainfall_mm": 610, "increase": 2.7},
            "recommendations": ["🏭 Industrial control", "🌳 Green cover", "🚗 EV promote karo"]
        },
        "meerut": {
            "city": "Meerut",
            "current": {"temperature": 26.2, "aqi": 265, "rainfall_mm": 700},
            "prediction_2050": {"temperature": 29.0, "aqi": 360, "rainfall_mm": 630, "increase": 2.8},
            "recommendations": ["🏭 Pollution control", "🌳 Tree plantation", "💧 Water management"]
        },
        "rajkot": {
            "city": "Rajkot",
            "current": {"temperature": 28.0, "aqi": 175, "rainfall_mm": 650},
            "prediction_2050": {"temperature": 30.5, "aqi": 240, "rainfall_mm": 580, "increase": 2.5},
            "recommendations": ["💧 Water conservation", "🌳 Green cover", "🏭 Industrial control"]
        },
        "kalyan": {
            "city": "Kalyan",
            "current": {"temperature": 28.0, "aqi": 190, "rainfall_mm": 2000},
            "prediction_2050": {"temperature": 30.5, "aqi": 260, "rainfall_mm": 1850, "increase": 2.5},
            "recommendations": ["🌳 Tree plantation", "💧 Flood control", "🏘️ Urban planning"]
        },
        "thane": {
            "city": "Thane",
            "current": {"temperature": 28.2, "aqi": 185, "rainfall_mm": 2100},
            "prediction_2050": {"temperature": 30.7, "aqi": 255, "rainfall_mm": 1950, "increase": 2.5},
            "recommendations": ["🌳 Green cover", "💧 Water management", "🏙️ Urban planning"]
        },
        "varanasi": {
            "city": "Varanasi",
            "current": {"temperature": 26.5, "aqi": 235, "rainfall_mm": 950},
            "prediction_2050": {"temperature": 29.0, "aqi": 320, "rainfall_mm": 880, "increase": 2.5},
            "recommendations": ["🕉️ Heritage protect karo", "🌳 Ganga clean karo", "🏭 Pollution control"]
        },
        "srinagar": {
            "city": "Srinagar",
            "current": {"temperature": 14.5, "aqi": 85, "rainfall_mm": 650},
            "prediction_2050": {"temperature": 17.5, "aqi": 140, "rainfall_mm": 580, "increase": 3.0},
            "recommendations": ["🏔️ Environment protect karo", "🌳 Dal lake conserve karo", "❄️ Glacier protect karo"]
        },
        "chandigarh": {
            "city": "Chandigarh",
            "current": {"temperature": 24.0, "aqi": 165, "rainfall_mm": 850},
            "prediction_2050": {"temperature": 26.5, "aqi": 230, "rainfall_mm": 780, "increase": 2.5},
            "recommendations": ["🌳 Planned city maintain karo", "💧 Water conservation", "🏭 Pollution control"]
        },
        "coimbatore": {
            "city": "Coimbatore",
            "current": {"temperature": 27.5, "aqi": 145, "rainfall_mm": 650},
            "prediction_2050": {"temperature": 30.0, "aqi": 210, "rainfall_mm": 580, "increase": 2.5},
            "recommendations": ["🏭 Industrial control", "💧 Water management", "🌳 Green cover"]
        },
        "kochi": {
            "city": "Kochi",
            "current": {"temperature": 28.5, "aqi": 125, "rainfall_mm": 2800},
            "prediction_2050": {"temperature": 31.0, "aqi": 190, "rainfall_mm": 2600, "increase": 2.5},
            "recommendations": ["🌴 Coastal protection", "💧 Flood control", "🌳 Mangrove conserve karo"]
        },
        "thiruvananthapuram": {
            "city": "Trivandrum",
            "current": {"temperature": 28.0, "aqi": 115, "rainfall_mm": 2500},
            "prediction_2050": {"temperature": 30.5, "aqi": 180, "rainfall_mm": 2300, "increase": 2.5},
            "recommendations": ["🏛️ Heritage protect karo", "🌊 Coastal protection", "💧 Water management"]
        },
        "guwahati": {
            "city": "Guwahati",
            "current": {"temperature": 25.5, "aqi": 155, "rainfall_mm": 1700},
            "prediction_2050": {"temperature": 28.0, "aqi": 220, "rainfall_mm": 1550, "increase": 2.5},
            "recommendations": ["🍵 Tea gardens protect karo", "🌳 Green cover", "💧 Flood control"]
        },
        "bhubaneswar": {
            "city": "Bhubaneswar",
            "current": {"temperature": 28.0, "aqi": 165, "rainfall_mm": 1550},
            "prediction_2050": {"temperature": 30.5, "aqi": 230, "rainfall_mm": 1400, "increase": 2.5},
            "recommendations": ["🛕 Heritage protect karo", "🌳 Green cover", "💧 Water management"]
        },
        "ranchi": {
            "city": "Ranchi",
            "current": {"temperature": 24.5, "aqi": 145, "rainfall_mm": 1400},
            "prediction_2050": {"temperature": 27.0, "aqi": 210, "rainfall_mm": 1280, "increase": 2.5},
            "recommendations": ["🏞️ Nature protect karo", "🌳 Green cover", "💧 Water conservation"]
        },
        "raipur": {
            "city": "Raipur",
            "current": {"temperature": 26.5, "aqi": 175, "rainfall_mm": 1300},
            "prediction_2050": {"temperature": 29.0, "aqi": 240, "rainfall_mm": 1180, "increase": 2.5},
            "recommendations": ["🌾 Agriculture protect karo", "🌳 Green cover", "💧 Water management"]
        },
        "dehradun": {
            "city": "Dehradun",
            "current": {"temperature": 20.5, "aqi": 125, "rainfall_mm": 1350},
            "prediction_2050": {"temperature": 23.5, "aqi": 190, "rainfall_mm": 1220, "increase": 3.0},
            "recommendations": ["🏔️ Hills protect karo", "🌳 Green cover", "❄️ Environment conserve karo"]
        },
        "shimla": {
            "city": "Shimla",
            "current": {"temperature": 16.5, "aqi": 75, "rainfall_mm": 1100},
            "prediction_2050": {"temperature": 19.5, "aqi": 130, "rainfall_mm": 980, "increase": 3.0},
            "recommendations": ["🏔️ Hills protect karo", "❄️ Snow conserve karo", "🌳 Green cover"]
        },
        "gangtok": {
            "city": "Gangtok",
            "current": {"temperature": 16.0, "aqi": 65, "rainfall_mm": 2500},
            "prediction_2050": {"temperature": 19.0, "aqi": 120, "rainfall_mm": 2300, "increase": 3.0},
            "recommendations": ["🏔️ Mountains protect karo", "🌳 Green cover", "❄️ Environment conserve karo"]
        },
        "imphal": {
            "city": "Imphal",
            "current": {"temperature": 22.5, "aqi": 95, "rainfall_mm": 1400},
            "prediction_2050": {"temperature": 25.0, "aqi": 160, "rainfall_mm": 1280, "increase": 2.5},
            "recommendations": ["🌸 Nature protect karo", "🌳 Green cover", "💧 Water management"]
        },
        "agartala": {
            "city": "Agartala",
            "current": {"temperature": 25.5, "aqi": 115, "rainfall_mm": 2100},
            "prediction_2050": {"temperature": 28.0, "aqi": 180, "rainfall_mm": 1950, "increase": 2.5},
            "recommendations": ["🌳 Green cover", "💧 Water management", "🏞️ Nature conserve karo"]
        },
        
        # INTERNATIONAL CITIES
        "newyork": {
            "city": "New York",
            "current": {"temperature": 13.0, "aqi": 65, "rainfall_mm": 1200},
            "prediction_2050": {"temperature": 16.0, "aqi": 120, "rainfall_mm": 1100, "increase": 3.0},
            "recommendations": ["🗽 City infrastructure protect karo", "🌳 Green cover", "💧 Flood control"]
        },
        "london": {
            "city": "London",
            "current": {"temperature": 11.5, "aqi": 55, "rainfall_mm": 750},
            "prediction_2050": {"temperature": 14.5, "aqi": 110, "rainfall_mm": 680, "increase": 3.0},
            "recommendations": ["🎡 Heritage protect karo", "🌳 Green cover", "💧 Water management"]
        },
        "paris": {
            "city": "Paris",
            "current": {"temperature": 12.5, "aqi": 60, "rainfall_mm": 650},
            "prediction_2050": {"temperature": 15.5, "aqi": 115, "rainfall_mm": 580, "increase": 3.0},
            "recommendations": ["🗼 Heritage protect karo", "🌳 Green cover", "🏭 Pollution control"]
        },
        "tokyo": {
            "city": "Tokyo",
            "current": {"temperature": 16.0, "aqi": 45, "rainfall_mm": 1530},
            "prediction_2050": {"temperature": 19.0, "aqi": 100, "rainfall_mm": 1400, "increase": 3.0},
            "recommendations": ["🗾 Technology use karo", "🌳 Green cover", "💧 Flood control"]
        },
        "beijing": {
            "city": "Beijing",
            "current": {"temperature": 13.0, "aqi": 185, "rainfall_mm": 585},
            "prediction_2050": {"temperature": 16.0, "aqi": 250, "rainfall_mm": 520, "increase": 3.0},
            "recommendations": ["🏯 Air quality improve karo", "🌳 Green cover", "🏭 Pollution control"]
        },
        "dubai": {
            "city": "Dubai",
            "current": {"temperature": 33.0, "aqi": 145, "rainfall_mm": 100},
            "prediction_2050": {"temperature": 36.5, "aqi": 210, "rainfall_mm": 80, "increase": 3.5},
            "recommendations": ["🏙️ Cooling technology use karo", "💧 Water conservation", "🌳 Green buildings"]
        },
        "singapore": {
            "city": "Singapore",
            "current": {"temperature": 28.0, "aqi": 55, "rainfall_mm": 2340},
            "prediction_2050": {"temperature": 31.0, "aqi": 110, "rainfall_mm": 2150, "increase": 3.0},
            "recommendations": ["🦁 Green city maintain karo", "💧 Flood control", "🌳 Urban gardens"]
        },
        "sydney": {
            "city": "Sydney",
            "current": {"temperature": 19.0, "aqi": 35, "rainfall_mm": 1210},
            "prediction_2050": {"temperature": 22.0, "aqi": 90, "rainfall_mm": 1100, "increase": 3.0},
            "recommendations": ["🦘 Nature protect karo", "🌊 Coastal protection", "🌳 Green cover"]
        },
        "toronto": {
            "city": "Toronto",
            "current": {"temperature": 9.5, "aqi": 45, "rainfall_mm": 830},
            "prediction_2050": {"temperature": 13.0, "aqi": 100, "rainfall_mm": 750, "increase": 3.5},
            "recommendations": ["🍁 Green cover maintain karo", "💧 Water management", "🏭 Pollution control"]
        },
        "berlin": {
            "city": "Berlin",
            "current": {"temperature": 10.5, "aqi": 50, "rainfall_mm": 570},
            "prediction_2050": {"temperature": 14.0, "aqi": 105, "rainfall_mm": 500, "increase": 3.5},
            "recommendations": ["🍺 Green city maintain karo", "🌳 Renewable energy", "💧 Water conservation"]
        },
        "moscow": {
            "city": "Moscow",
            "current": {"temperature": 6.0, "aqi": 75, "rainfall_mm": 707},
            "prediction_2050": {"temperature": 10.0, "aqi": 130, "rainfall_mm": 630, "increase": 4.0},
            "recommendations": ["🏰 Heritage protect karo", "🌳 Green cover", "❄️ Winter conserve karo"]
        },
        "cairo": {
            "city": "Cairo",
            "current": {"temperature": 28.0, "aqi": 165, "rainfall_mm": 25},
            "prediction_2050": {"temperature": 32.0, "aqi": 230, "rainfall_mm": 20, "increase": 4.0},
            "recommendations": ["🔺 Heritage protect karo", "💧 Water conservation critical", "🌳 Desert greening"]
        },
        "saopaulo": {
            "city": "São Paulo",
            "current": {"temperature": 20.0, "aqi": 95, "rainfall_mm": 1455},
            "prediction_2050": {"temperature": 23.5, "aqi": 160, "rainfall_mm": 1320, "increase": 3.5},
            "recommendations": ["🇧🇷 Amazon protect karo", "🌳 Green cover", "💧 Water management"]
        },
        "mexicocity": {
            "city": "Mexico City",
            "current": {"temperature": 17.0, "aqi": 125, "rainfall_mm": 820},
            "prediction_2050": {"temperature": 20.5, "aqi": 190, "rainfall_mm": 740, "increase": 3.5},
            "recommendations": ["🌮 Air quality improve karo", "🌳 Green cover", "💧 Water management"]
        },
        "bangkok": {
            "city": "Bangkok",
            "current": {"temperature": 29.5, "aqi": 115, "rainfall_mm": 1620},
            "prediction_2050": {"temperature": 33.0, "aqi": 180, "rainfall_mm": 1480, "increase": 3.5},
            "recommendations": ["🛕 Heritage protect karo", "💧 Flood control", "🌳 Green cover"]
        },
        "kualalumpur": {
            "city": "Kuala Lumpur",
            "current": {"temperature": 28.5, "aqi": 95, "rainfall_mm": 2530},
            "prediction_2050": {"temperature": 32.0, "aqi": 160, "rainfall_mm": 2350, "increase": 3.5},
            "recommendations": ["🏙️ Green buildings", "💧 Flood control", "🌳 Urban gardens"]
        },
        "jakarta": {
            "city": "Jakarta",
            "current": {"temperature": 28.0, "aqi": 135, "rainfall_mm": 1790},
            "prediction_2050": {"temperature": 31.5, "aqi": 200, "rainfall_mm": 1630, "increase": 3.5},
            "recommendations": ["🏝️ Coastal protection", "💧 Flood control critical", "🌳 Green cover"]
        },
        "manila": {
            "city": "Manila",
            "current": {"temperature": 28.5, "aqi": 105, "rainfall_mm": 2100},
            "prediction_2050": {"temperature": 32.0, "aqi": 170, "rainfall_mm": 1930, "increase": 3.5},
            "recommendations": ["🏝️ Coastal protection", "💧 Flood control", "🌳 Green cover"]
        },
        "karachi": {
            "city": "Karachi",
            "current": {"temperature": 27.5, "aqi": 195, "rainfall_mm": 250},
            "prediction_2050": {"temperature": 31.0, "aqi": 260, "rainfall_mm": 220, "increase": 3.5},
            "recommendations": ["🕌 Coastal protection", "💧 Water conservation", "🌳 Green cover"]
        },
        "dhaka": {
            "city": "Dhaka",
            "current": {"temperature": 26.5, "aqi": 215, "rainfall_mm": 2120},
            "prediction_2050": {"temperature": 30.0, "aqi": 280, "rainfall_mm": 1950, "increase": 3.5},
            "recommendations": ["🇧🇩 Flood control", "💧 Water management", "🌳 Green cover"]
        },
        "colombo": {
            "city": "Colombo",
            "current": {"temperature": 28.0, "aqi": 95, "rainfall_mm": 2330},
            "prediction_2050": {"temperature": 31.5, "aqi": 160, "rainfall_mm": 2150, "increase": 3.5},
            "recommendations": ["🇱🇰 Coastal protection", "💧 Water management", "🌳 Green cover"]
        },
        "kathmandu": {
            "city": "Kathmandu",
            "current": {"temperature": 18.5, "aqi": 185, "rainfall_mm": 1400},
            "prediction_2050": {"temperature": 22.0, "aqi": 250, "rainfall_mm": 1270, "increase": 3.5},
            "recommendations": ["🏔️ Mountains protect karo", "🌳 Green cover", "💧 Water management"]
        },
        "kabul": {
            "city": "Kabul",
            "current": {"temperature": 12.5, "aqi": 165, "rainfall_mm": 310},
            "prediction_2050": {"temperature": 16.5, "aqi": 230, "rainfall_mm": 270, "increase": 4.0},
            "recommendations": ["🏔️ Environment protect karo", "💧 Water conservation", "🌳 Green cover"]
        },
        "tehran": {
            "city": "Tehran",
            "current": {"temperature": 17.5, "aqi": 175, "rainfall_mm": 230},
            "prediction_2050": {"temperature": 21.5, "aqi": 240, "rainfall_mm": 190, "increase": 4.0},
            "recommendations": ["🕌 Air quality improve karo", "💧 Water conservation", "🌳 Green cover"]
        }
    }
    
    return cities.get(city_name.lower(), cities["lucknow"])

@app.post("/api/chat")
async def chat(request: ChatRequest):
    message = request.message.lower()
    
    if "lucknow" in message:
        response = "🏙️ Lucknow ka Climate Prediction:\n\n📊 Current Temp: 25.8°C\n🔮 2050 tak: 28.5°C\n📈 Increase: +2.7°C\n\n💡 Suggestions:\n• Tree plantation badhao\n• Gomti river clean karo"
    elif "delhi" in message:
        response = "🏙️ Delhi ka Climate Prediction:\n\n📊 Current Temp: 26.5°C\n🔮 2050 tak: 29.8°C\n📈 Increase: +3.3°C\n\n💡 Suggestions:\n• Odd-even scheme lagao\n• Air purifiers use karo"
    elif "mumbai" in message:
        response = "🏙️ Mumbai ka Climate Prediction:\n\n📊 Current Temp: 28.3°C\n🔮 2050 tak: 30.5°C\n📈 Increase: +2.2°C\n\n💡 Suggestions:\n• Coastal protection karo\n• Vertical gardens lagao"
    elif "help" in message:
        response = "🤖 Main kaise help karu:\n\n1️⃣ City prediction: \"Lucknow temp\"\n2️⃣ Global info: \"Temperature kya hai\"\n3️⃣ Solutions: \"Kya kar sakte hain\""
    else:
        response = "🤔 Samajh nahi aaya bhai.\n\nTry karo:\n• \"Lucknow climate\"\n• \"Delhi temperature\"\n• \"Help\""
    
    return {"response": response, "language": "hinglish"}

@app.get("/api/cities")
async def get_cities():
    return {"cities": ["lucknow", "delhi", "mumbai", "kolkata", "chennai", "bangalore"], "count": 6}

@app.get("/")
async def root():
    return {"message": "🌍 Climate Intelligence Hub API", "status": "Running"}

if __name__ == "__main__":
    print("🚀 Backend starting on http://localhost:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)