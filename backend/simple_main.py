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
        "kolkata": {
            "city": "Kolkata",
            "current": {"temperature": 27.8, "aqi": 195, "rainfall_mm": 1580},
            "prediction_2050": {"temperature": 30.2, "aqi": 280, "rainfall_mm": 1450, "increase": 2.4},
            "recommendations": ["Preserve parks and green spaces", "Address water logging", "Control industrial emissions", "Create cycling lanes"]
        },
        "chennai": {
            "city": "Chennai",
            "current": {"temperature": 29.5, "aqi": 165, "rainfall_mm": 1400},
            "prediction_2050": {"temperature": 32.0, "aqi": 220, "rainfall_mm": 1300, "increase": 2.5},
            "recommendations": ["Prioritize water conservation", "Install desalination plants", "Enhance rainwater harvesting", "Protect coastal infrastructure"]
        },
        "bangalore": {
            "city": "Bangalore",
            "current": {"temperature": 24.5, "aqi": 145, "rainfall_mm": 970},
            "prediction_2050": {"temperature": 27.0, "aqi": 200, "rainfall_mm": 880, "increase": 2.5},
            "recommendations": ["Conserve lakes", "Stop uncontrolled construction", "Make rainwater harvesting mandatory", "Transform IT city into green city"]
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
            "recommendations": ["Water conservation critical", "Increase green cover", "Control industrial emissions", "Heat action plan"]
        },
        "jaipur": {
            "city": "Jaipur",
            "current": {"temperature": 27.5, "aqi": 195, "rainfall_mm": 550},
            "prediction_2050": {"temperature": 30.0, "aqi": 260, "rainfall_mm": 480, "increase": 2.5},
            "recommendations": ["Tree plantation", "Water harvesting", "Protect heritage sites", "Combat desertification"]
        },
        "lucknow": {
            "city": "Lucknow",
            "current": {"temperature": 25.8, "aqi": 210, "rainfall_mm": 850},
            "prediction_2050": {"temperature": 28.5, "aqi": 340, "rainfall_mm": 780, "increase": 2.7},
            "recommendations": ["Tree plantation drives", "Clean Gomti river", "Promote metro and e-rickshaws", "Control industrial pollution"]
        }
    }
    
    return cities.get(city_name.lower(), cities["lucknow"])

@app.post("/api/chat")
async def chat(request: ChatRequest):
    message = request.message.lower()
    
    # City-specific queries
    city_responses = {
        "lucknow": """🏙️ **Lucknow Climate Prediction**

📊 Current Temperature: 25.8°C
🔮 2050 Projection: 28.5°C
📈 Temperature Increase: +2.7°C

⚠️ **Alert:** Temperature is rising rapidly!

💡 **Recommendations:**
• Increase tree plantation
• Clean and conserve Gomti River
• Promote metro and e-rickshaw usage
• Control industrial pollution
• Implement green building norms""",
        
        "delhi": """🏙️ **Delhi Climate Prediction**

📊 Current Temperature: 26.5°C
🔮 2050 Projection: 29.8°C
📈 Temperature Increase: +3.3°C

⚠️ **Critical Alert:** Highest risk among major cities! Air quality is severely degraded.

💡 **Recommendations:**
• Implement odd-even vehicle scheme regularly
• Use air purifiers indoors
• Increase green cover to 33%
• Control construction dust
• Promote public transport and metro
• Shift to electric vehicles""",
        
        "mumbai": """🏙️ **Mumbai Climate Prediction**

📊 Current Temperature: 28.3°C
🔮 2050 Projection: 30.5°C
📈 Temperature Increase: +2.2°C

🌊 **Coastal Risk:** Sea level rise poses significant threat.

💡 **Recommendations:**
• Protect coastal areas and mangroves
• Install vertical gardens on buildings
• Improve waste management systems
• Implement flood control measures
• Strengthen coastal infrastructure
• Conserve green spaces""",
        
        "bangalore": """🏙️ **Bangalore Climate Prediction**

📊 Current Temperature: 24.5°C
🔮 2050 Projection: 27.0°C
📈 Temperature Increase: +2.5°C

💻 **Tech City Challenge:** Rapid urbanization affecting climate.

💡 **Recommendations:**
• Conserve and restore lakes
• Stop uncontrolled construction
• Make rainwater harvesting mandatory
• Transform IT city into green city
• Promote sustainable urban planning
• Increase urban forests""",
        
        "chennai": """🏙️ **Chennai Climate Prediction**

📊 Current Temperature: 29.5°C
🔮 2050 Projection: 32.0°C
📈 Temperature Increase: +2.5°C

💧 **Water Crisis:** Water scarcity is a critical concern.

💡 **Recommendations:**
• Prioritize water conservation
• Install desalination plants
• Enhance rainwater harvesting
• Protect coastal infrastructure
• Manage groundwater sustainably
• Reduce water wastage""",
        
        "kolkata": """🏙️ **Kolkata Climate Prediction**

📊 Current Temperature: 27.8°C
🔮 2050 Projection: 30.2°C
📈 Temperature Increase: +2.4°C

🌊 **Flooding Risk:** Water logging and flooding increasing.

💡 **Recommendations:**
• Preserve parks and green spaces
• Address water logging issues
• Control industrial emissions
• Create cycling lanes
• Improve drainage systems
• Protect wetlands""",
        
        "hyderabad": """🏙️ **Hyderabad Climate Prediction**

📊 Current Temperature: 28.0°C
🔮 2050 Projection: 30.5°C
📈 Temperature Increase: +2.5°C

🏙️ **Urban Challenge:** Balancing growth with environment.

💡 **Recommendations:**
• Increase green cover
• Prioritize water conservation
• Strengthen public transport
• Protect lakes and water bodies
• Promote sustainable development
• Implement green building codes"""
    }
    
    # Check for city names
    for city_name, response in city_responses.items():
        if city_name in message:
            return {"response": response, "language": "english"}
    
    # Temperature queries
    if any(word in message for word in ["temp", "temperature", "hot", "heat", "warming"]):
        return {
            "response": """🌡️ **Global Temperature Status**

📊 **Current (2024):** 15.14°C
🔮 **2050 Projection:** 16.50°C
📈 **Total Increase:** +1.36°C

⚠️ **Paris Agreement Target:** Limit warming to 1.5°C

**Current Status:** We are approaching the critical threshold!

**If emissions continue unchecked:** Temperature could rise by 2-3°C by 2050, leading to catastrophic consequences.

🌍 **Every 0.1°C matters!** Immediate action is essential to prevent irreversible climate change.""",
            "language": "english"
        }
    
    # Carbon emissions queries
    elif any(word in message for word in ["carbon", "emission", "co2", "pollution", "greenhouse"]):
        return {
            "response": """🏭 **Carbon Emissions Crisis**

📊 **Current CO₂ Levels:** 420 ppm
📈 **Pre-industrial Level:** 280 ppm
📊 **Increase:** +140 ppm (50% rise!)

🎯 **Critical Targets:**
• Reduce emissions by 45% by 2030
• Achieve Carbon Neutrality by 2050
• Net-zero emissions by 2070

💡 **Solutions:**
• Transition to renewable energy (Solar, Wind)
• Adopt electric vehicles
• Increase tree plantation
• Improve energy efficiency
• Reduce fossil fuel consumption
• Implement carbon pricing

🌱 **The time to act is NOW!**""",
            "language": "english"
        }
    
    # Future predictions
    elif any(word in message for word in ["2050", "future", "prediction", "forecast", "will happen"]):
        return {
            "response": """🔮 **Climate Scenario by 2050**

🌡️ **Temperature Rise:** 1.5-3°C increase
🌊 **Sea Level Rise:** 30-50 cm
🏙️ **Cities at Risk:** Coastal megacities
🌾 **Food Security:** Under threat
💧 **Water Scarcity:** Will intensify
🔥 **Extreme Weather:** More frequent and severe

⚠️ **Potential Impacts:**
• Increased heatwaves and droughts
• More intense storms and flooding
• Loss of biodiversity
• Agricultural disruption
• Mass migration from affected areas
• Economic losses in trillions

✅ **But we can still prevent the worst:**
• Rapid transition to renewable energy
• Massive carbon emission reductions
• Large-scale reforestation
• Sustainable lifestyle changes
• Green technology adoption

**The future is in our hands!** 🌍""",
            "language": "english"
        }
    
    # Help menu
    elif any(word in message for word in ["help", "what can", "how to", "assist"]):
        return {
            "response": """🤖 **How I Can Help You**

**1️⃣ City Climate Predictions:**
   • "What is the temperature in Lucknow?"
   • "Delhi climate forecast"
   • "Mumbai 2050 prediction"
   • "Bangalore weather outlook"

**2️⃣ Global Climate Information:**
   • "What is the current temperature?"
   • "How much CO2 is in the atmosphere?"
   • "What will happen by 2050?"
   • "Why is climate change happening?"

**3️⃣ Solutions & Actions:**
   • "What can we do?"
   • "How to reduce carbon footprint?"
   • "Climate solutions"
   • "How to help the environment?"

**4️⃣ Specific Topics:**
   • "Sea level rise"
   • "Global warming"
   • "Air quality"
   • "Renewable energy"

**Just type your question - I'm here to help!** 😊""",
            "language": "english"
        }
    
    # Solutions
    elif any(word in message for word in ["solution", "solve", "what can we do", "action", "prevent"]):
        return {
            "response": """🌱 **Climate Change Solutions**

**Individual Actions:**
✅ Use electric or public transport
✅ Install solar panels
✅ Reduce, reuse, recycle
✅ Plant trees
✅ Use energy-efficient appliances
✅ Reduce meat consumption
✅ Conserve water
✅ Support sustainable products

**Community Actions:**
✅ Build green infrastructure
✅ Implement rainwater harvesting
✅ Adopt renewable energy
✅ Create awareness programs
✅ Establish community gardens

**Government/Policy Actions:**
✅ Implement carbon tax
✅ Ban single-use plastics
✅ Promote renewable energy
✅ Improve public transport
✅ Enforce emission standards
✅ Protect forests and wetlands

**Corporate Actions:**
✅ Adopt sustainable practices
✅ Reduce carbon footprint
✅ Invest in green technology
✅ Implement circular economy

**Every action counts! Together we can make a difference! 🌍**""",
            "language": "english"
        }
    
    # Sea level rise
    elif any(word in message for word in ["sea level", "ocean", "coastal", "flooding"]):
        return {
            "response": """🌊 **Sea Level Rise**

📊 **Current Situation:**
• Sea level has risen 8 inches since 1880
• Rising at 3.3mm per year
• Rate is accelerating

🔮 **2050 Projection:**
• Additional 30-50 cm rise expected
• Could reach 1 meter by 2100

🏙️ **Cities at High Risk:**
• Mumbai, Kolkata, Chennai (India)
• Miami, New York (USA)
• Bangkok (Thailand)
• Jakarta (Indonesia)
• Venice (Italy)

⚠️ **Consequences:**
• Coastal flooding
• Erosion of shorelines
• Saltwater intrusion into freshwater
• Displacement of millions
• Loss of coastal ecosystems
• Economic damage in billions

💡 **Solutions:**
• Build coastal defenses
• Restore mangroves and wetlands
• Reduce emissions
• Planned retreat from vulnerable areas
• Sustainable coastal development

**Urgent action needed!** 🌍""",
            "language": "english"
        }
    
    # Air quality
    elif any(word in message for word in ["air quality", "aqi", "pollution", "breathe"]):
        return {
            "response": """😷 **Air Quality Crisis**

📊 **Current Status:**
• 22 Indian cities in world's 30 most polluted
• Delhi AQI regularly exceeds 300-400
• 99% of global population breathes unhealthy air

⚠️ **Health Impacts:**
• Respiratory diseases (asthma, COPD)
• Heart disease and stroke
• Lung cancer
• Reduced life expectancy
• Children most vulnerable
• 7 million premature deaths annually

📈 **AQI Scale:**
🟢 0-50: Good
🟡 51-100: Moderate
🟠 101-150: Unhealthy for Sensitive Groups
🔴 151-200: Unhealthy
🟣 201-300: Very Unhealthy
⚫ 301+: Hazardous

💡 **Solutions:**
• Use air purifiers indoors
• Wear N95 masks on high pollution days
• Use public transport
• Control industrial emissions
• Increase green cover
• Ban crop burning
• Promote electric vehicles

**Protect yourself and the planet!** 🌱""",
            "language": "english"
        }
    
    # Global warming
    elif any(word in message for word in ["global warming", "climate change", "why"]):
        return {
            "response": """🌡️ **Global Warming Explained**

**What is it?**
Global warming is the long-term heating of Earth's surface due to human activities, primarily fossil fuel burning.

**How much has it warmed?**
• Since 1850: +1.2°C globally
• India (1901-2018): +0.7°C
• Arctic warming 2-3 times faster

**Why is it happening?**
🏭 Burning fossil fuels (coal, oil, gas)
🌳 Deforestation and land use change
🐄 Agriculture and livestock (methane)
🏗️ Industrial processes
🚗 Transportation emissions

**Effects:**
🔥 More frequent and intense heatwaves
🌊 Melting glaciers and ice caps
🌾 Disrupted agriculture and food security
💧 Water scarcity
🦠 Spread of diseases
🌪️ Extreme weather events
🐻 Loss of biodiversity

**The Solution:**
✅ Transition to renewable energy
✅ Protect and restore forests
✅ Sustainable agriculture
✅ Green transportation
✅ Energy efficiency
✅ Circular economy

**We must act now to secure our future!** 🌍""",
            "language": "english"
        }
    
    # Renewable energy
    elif any(word in message for word in ["renewable", "solar", "wind", "clean energy", "green energy"]):
        return {
            "response": """☀️ **Renewable Energy - The Future**

**Types of Renewable Energy:**
🌞 Solar Energy - Harnessing sunlight
🌬️ Wind Energy - Using wind turbines
💧 Hydroelectric - Water power
🌊 Tidal/Wave Energy - Ocean power
🔥 Geothermal - Earth's heat
🌱 Biomass - Organic materials

**India's Renewable Energy Targets:**
• 500 GW by 2030
• 50% electricity from renewables by 2030
• Net-zero emissions by 2070

**Benefits:**
✅ Zero carbon emissions
✅ Unlimited and sustainable
✅ Decreasing costs
✅ Job creation
✅ Energy independence
✅ Improved air quality
✅ Climate change mitigation

**Challenges:**
❌ High initial investment
❌ Energy storage needs
❌ Grid infrastructure upgrades
❌ Intermittency issues

**The Future:**
Solar + Wind + Battery Storage = Clean, Reliable Energy 24/7

**Renewable energy is not just the future - it's the present!** 🌍⚡""",
            "language": "english"
        }
    
    # Default response
    else:
        return {
            "response": """🤔 **I'm not sure I understand.**

**Here's what you can ask me:**

📍 **City Predictions:**
• "What is the climate forecast for Delhi?"
• "Tell me about Mumbai's temperature"
• "Bangalore 2050 prediction"

🌡️ **Climate Information:**
• "What is the current global temperature?"
• "How much CO2 is in the atmosphere?"
• "What will happen by 2050?"

💡 **Solutions:**
• "What can we do about climate change?"
• "How to reduce carbon emissions?"
• "Climate solutions"

❓ **General Topics:**
• "Sea level rise"
• "Air quality"
• "Global warming"
• "Renewable energy"

**Or simply type "help" for more options!**

I'm here to provide accurate climate information and predictions. 😊""",
            "language": "english"
        }

@app.get("/api/cities")
async def get_cities():
    return {
        "cities": ["delhi", "mumbai", "kolkata", "chennai", "bangalore", "hyderabad", "pune", "ahmedabad", "jaipur", "lucknow"],
        "count": 10
    }

@app.get("/")
async def root():
    return {
        "message": "🌍 Climate Intelligence Hub API",
        "status": "Running",
        "version": "2.0 - Professional Edition"
    }

if __name__ == "__main__":
    print("🚀 Climate Intelligence Hub API starting...")
    print("📊 Server running on http://localhost:8000")
    print("🌍 Ready to serve climate data!")
    uvicorn.run(app, host="0.0.0.0", port=8000)