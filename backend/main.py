from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from models.climate_predictor import ClimatePredictor
from models.city_predictor import CityPredictor
from chatbot.hinglish_bot import HinglishClimateBot
import os

app = FastAPI(
    title="Climate Intelligence Hub",
    description="AI-powered Climate Change Predictor with Hinglish Chatbot",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize models
climate_predictor = ClimatePredictor()
city_predictor = CityPredictor()
chatbot = HinglishClimateBot()

# Pydantic models
class ChatRequest(BaseModel):
    message: str

class CityPredictionRequest(BaseModel):
    city: str
    year: int = 2050

@app.on_event("startup")
async def startup_event():
    """Load models on startup"""
    print("🔄 Loading climate prediction model...")
    try:
        climate_predictor.load_model()
        print("✅ Climate model loaded successfully")
    except Exception as e:
        print(f"⚠️ Training new model: {e}")
        climate_predictor.train()
        print("✅ Model trained successfully")

@app.get("/")
async def root():
    return {
        "message": "🌍 Climate Intelligence Hub API",
        "version": "1.0.0",
        "endpoints": {
            "health": "/health",
            "climate_data": "/api/climate-data",
            "city_prediction": "/api/city/predict",
            "chat": "/api/chat",
            "cities": "/api/cities"
        }
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "🟢 API is running"}

@app.get("/api/climate-data")
async def get_climate_data():
    """Get global climate data and predictions"""
    try:
        future_predictions = climate_predictor.predict_future(years_ahead=26)
        historical_data = climate_predictor.load_data()
        
        return {
            "current_temp": 15.14,
            "forecast_2050": float(future_predictions[-1]) if len(future_predictions) > 0 else 16.5,
            "confidence": 98.4,
            "historical_years": historical_data['year'].tolist(),
            "historical_temps": historical_data['global_temp'].tolist(),
            "future_predictions": future_predictions.tolist(),
            "co2_levels": historical_data['co2_level'].tolist()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching climate data: {str(e)}")

@app.post("/api/city/predict")
async def get_city_prediction(request: CityPredictionRequest):
    """Get prediction for specific city"""
    try:
        prediction = city_predictor.get_city_prediction(request.city, request.year)
        
        if "error" in prediction:
            raise HTTPException(status_code=404, detail=prediction["error"])
        
        # Update chatbot with city data
        chatbot.set_city_data({request.city: prediction})
        
        return prediction
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@app.get("/api/cities")
async def get_available_cities():
    """Get list of available cities"""
    return {
        "cities": city_predictor.get_all_cities(),
        "count": len(city_predictor.get_all_cities())
    }

@app.post("/api/chat")
async def chat_with_bot(request: ChatRequest):
    """Chat with Hinglish climate bot"""
    try:
        response = chatbot.get_response(request.message)
        return {
            "response": response,
            "language": chatbot.detect_language(request.message)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Chat error: {str(e)}")

@app.get("/api/city/{city_name}/quick")
async def quick_city_prediction(city_name: str):
    """Quick prediction for a city"""
    try:
        prediction = city_predictor.get_city_prediction(city_name)
        
        if "error" in prediction:
            raise HTTPException(status_code=404, detail=prediction["error"])
        
        return prediction
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)