import pandas as pd
import numpy as np
import os

class CityPredictor:
    def __init__(self):
        self.city_data = {
            "lucknow": {
                "name": "Lucknow",
                "lat": 26.8467,
                "lon": 80.9462,
                "current_temp": 25.8,
                "trend": 0.035,
                "aqi": 210,
                "rainfall": 850
            },
            "delhi": {
                "name": "Delhi",
                "lat": 28.7041,
                "lon": 77.1025,
                "current_temp": 26.5,
                "trend": 0.038,
                "aqi": 320,
                "rainfall": 780
            },
            "mumbai": {
                "name": "Mumbai",
                "lat": 19.0760,
                "lon": 72.8777,
                "current_temp": 28.3,
                "trend": 0.025,
                "aqi": 180,
                "rainfall": 2200
            },
            "kolkata": {
                "name": "Kolkata",
                "lat": 22.5726,
                "lon": 88.3639,
                "current_temp": 27.8,
                "trend": 0.030,
                "aqi": 195,
                "rainfall": 1580
            },
            "bangalore": {
                "name": "Bangalore",
                "lat": 12.9716,
                "lon": 77.5946,
                "current_temp": 24.5,
                "trend": 0.028,
                "aqi": 145,
                "rainfall": 970
            }
        }
    
    def get_city_prediction(self, city_name, target_year=2050):
        """Get prediction for specific city"""
        city_name = city_name.lower()
        
        if city_name not in self.city_data:
            return {"error": f"City {city_name} not found"}
        
        city = self.city_data[city_name]
        years_ahead = target_year - 2024
        
        predicted_temp = city["current_temp"] + (city["trend"] * years_ahead)
        predicted_aqi = city["aqi"] + int(5 * years_ahead)
        predicted_rainfall = city["rainfall"] - int(2 * years_ahead)
        
        return {
            "city": city["name"],
            "coordinates": {
                "latitude": city["lat"],
                "longitude": city["lon"]
            },
            "current": {
                "temperature": city["current_temp"],
                "aqi": city["aqi"],
                "rainfall_mm": city["rainfall"]
            },
            "prediction_2050": {
                "temperature": round(predicted_temp, 2),
                "aqi": predicted_aqi,
                "rainfall_mm": max(predicted_rainfall, 400),
                "increase": round(predicted_temp - city["current_temp"], 2)
            },
            "recommendations": self.get_recommendations(city_name, predicted_temp)
        }
    
    def get_recommendations(self, city, temp):
        """City-specific recommendations"""
        base_recommendations = {
            "lucknow": [
                "🌳 Tree plantation drive karo - Nawabi sheher ko green banao",
                "💧 Gomti river conservation zaroori hai",
                "🚲 Metro aur e-rickshaw ko promote karo",
                "🏭 Industrial pollution control strict karo"
            ],
            "delhi": [
                "🚗 Odd-even scheme regularly lagao",
                "🌫️ Air purifiers ka use badhao",
                "🌳 Green cover badhao - 33% target",
                "🏗️ Construction dust control karo"
            ],
            "mumbai": [
                "🌊 Coastal areas ko protect karo",
                "🏙️ Vertical gardens lagao buildings pe",
                "🚇 Public transport ko aur strong karo",
                "♻️ Waste management improve karo"
            ],
            "kolkata": [
                "🌳 Parks aur green spaces bachao",
                "💧 Water logging ka solution nikalo",
                "🏭 Industrial emissions control karo",
                "🚲 Cycle lanes banao"
            ],
            "bangalore": [
                "🌳 Lake conservation priority do",
                "🏗️ Uncontrolled construction roko",
                "💧 Rainwater harvesting mandatory karo",
                "🌿 Tech city ko green city banao"
            ]
        }
        
        if temp > 28:
            base_recommendations[city].append("⚠️ Heat action plan implement karo - summer dangerous ho sakta hai")
        
        return base_recommendations.get(city, ["🌍 General climate action lo"])
    
    def get_all_cities(self):
        """Get list of all available cities"""
        return list(self.city_data.keys())