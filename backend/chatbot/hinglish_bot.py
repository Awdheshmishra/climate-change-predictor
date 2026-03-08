import re

class HinglishClimateBot:
    def __init__(self):
        self.city_predictions = {}
        
    def detect_language(self, text):
        """Detect if text is Hindi, Hinglish, or English"""
        hindi_pattern = re.compile(r'[\u0900-\u097F]')
        
        if hindi_pattern.search(text):
            return "hindi"
        
        hinglish_words = ['hai', 'kya', 'kaise', 'kyu', 'kyun', 'batao', 'dikha', 
                         'karo', 'hoga', 'tha', 'tha', 'mein', 'mera', 'tum', 'hum']
        
        if any(word in text.lower() for word in hinglish_words):
            return "hinglish"
        
        return "english"
    
    def set_city_data(self, city_data):
        """Store city prediction data"""
        self.city_predictions = city_data
    
    def get_response(self, user_input):
        """Generate response based on user input"""
        user_input = user_input.lower()
        lang = self.detect_language(user_input)
        
        # City-specific queries
        for city in ['lucknow', 'delhi', 'mumbai', 'kolkata', 'bangalore']:
            if city in user_input:
                return self.handle_city_query(city, lang, user_input)
        
        # General queries
        if any(word in user_input for word in ['temp', 'temperature', 'गर्मी', 'तापमान']):
            return self.handle_temp_query(lang)
        
        elif any(word in user_input for word in ['carbon', 'emission', 'प्रदूषण', 'pollution']):
            return self.handle_carbon_query(lang)
        
        elif any(word in user_input for word in ['acid rain', 'एसिड रेन', 'बारिश']):
            return self.handle_acid_rain_query(lang)
        
        elif any(word in user_input for word in ['help', 'madad', 'क्या कर', 'what can']):
            return self.handle_help_query(lang)
        
        else:
            return self.get_default_response(lang)
    
    def handle_city_query(self, city, lang, query):
        """Handle city-specific queries"""
        if not self.city_predictions:
            return "Data load nahi hua hai. Backend check karo."
        
        city_data = self.city_predictions.get(city, {})
        
        if lang == "hindi":
            return f"""
🏙️ **{city_data.get('city', city.title())} का जलवायु पूर्वानुमान:**

📊 वर्तमान तापमान: {city_data.get('current', {}).get('temperature', 'N/A')}°C
🔮 2050 में: {city_data.get('prediction_2050', {}).get('temperature', 'N/A')}°C
📈 वृद्धि: {city_data.get('prediction_2050', {}).get('increase', 'N/A')}°C

💡 सुझाव:
{chr(10).join(city_data.get('recommendations', []))}
            """
        
        elif lang == "hinglish":
            return f"""
🏙️ **{city_data.get('city', city.title())} ka Climate Prediction:**

📊 Current Temp: {city_data.get('current', {}).get('temperature', 'N/A')}°C
🔮 2050 tak: {city_data.get('prediction_2050', {}).get('temperature', 'N/A')}°C
📈 Increase: {city_data.get('prediction_2050', {}).get('increase', 'N/A')}°C

💡 Suggestions:
{chr(10).join(city_data.get('recommendations', []))}

Aur kuch puchna hai bhai?
            """
        
        else:  # English
            return f"""
🏙️ **Climate Prediction for {city_data.get('city', city.title())}:**

📊 Current Temperature: {city_data.get('current', {}).get('temperature', 'N/A')}°C
🔮 Predicted for 2050: {city_data.get('prediction_2050', {}).get('temperature', 'N/A')}°C
📈 Increase: {city_data.get('prediction_2050', {}).get('increase', 'N/A')}°C

💡 Recommendations:
{chr(10).join(city_data.get('recommendations', []))}
            """
    
    def handle_temp_query(self, lang):
        """Handle temperature queries"""
        if lang == "hindi":
            return "🌡️ Global temperature 1850 se 1.2°C badh chuka hai. 2050 tak 1.5-2°C aur badh sakta hai अगर emissions control nahi kiye."
        
        elif lang == "hinglish":
            return "🌡️ Bhai, global temperature 1850 se 1.2°C badh gaya hai. 2050 tak 1.5-2°C aur badh sakta hai agar humne action nahi liya."
        
        else:
            return "🌡️ Global temperature has increased by 1.2°C since 1850. It could rise by another 1.5-2°C by 2050 if emissions are not controlled."
    
    def handle_carbon_query(self, lang):
        """Handle carbon emission queries"""
        if lang == "hindi":
            return "🏭 Carbon emissions ko 2030 tak 45% kam karna hoga. Carbon neutrality 2050 tak achieve karni hogi. Renewable energy pe focus karo!"
        
        elif lang == "hinglish":
            return "🏭 Bhai, carbon emissions ko 2030 tak 45% kam karna padega. Carbon neutrality 2050 tak achieve karni hogi. Solar, wind energy pe focus karo!"
        
        else:
            return "🏭 Carbon emissions need to be reduced by 45% by 2030. Carbon neutrality must be achieved by 2050. Focus on renewable energy!"
    
    def handle_acid_rain_query(self, lang):
        """Handle acid rain queries"""
        if lang == "hindi":
            return "🌧️ Acid rain SO2 aur NO2 gases se hota hai. Ye buildings, plants aur water bodies ko damage karta hai. Pollution kam karo!"
        
        elif lang == "hinglish":
            return "🌧️ Acid rain SO2 aur NO2 gases se hota hai bhai. Ye buildings, plants aur paani ko damage karta hai. Pollution control karo!"
        
        else:
            return "🌧️ Acid rain is caused by SO2 and NO2 gases. It damages buildings, plants, and water bodies. Control pollution!"
    
    def handle_help_query(self, lang):
        """Handle help queries"""
        if lang == "hindi":
            return """
🤖 **मैं आपकी कैसे मदद कर सकता हूँ:**

1. किसी city का climate prediction पूछो (e.g., "Lucknow का temperature")
2. Global temperature के बारे में पूछो
3. Carbon emissions के बारे में जानो
4. Acid rain के बारे में पूछो
5. Solutions और suggestions लो

क्या जानना चाहते हैं?
            """
        
        elif lang == "hinglish":
            return """
🤖 **Main kaise help kar sakta hoon:**

1. Kisi city ka climate prediction pucho (e.g., "Lucknow ka temperature")
2. Global temperature ke baare mein pucho
3. Carbon emissions ke baare mein jano
4. Acid rain ke baare mein pucho
5. Solutions aur suggestions lo

Kya janna hai bhai?
            """
        
        else:
            return """
🤖 **How I can help:**

1. Ask for city climate prediction (e.g., "Lucknow temperature")
2. Ask about global temperature
3. Learn about carbon emissions
4. Ask about acid rain
5. Get solutions and suggestions

What would you like to know?
            """
    
    def get_default_response(self, lang):
        """Default response when query is not understood"""
        if lang == "hindi":
            return "मुझे समझ नहीं आया। क्या आप 'help' या 'madad' type कर सकते हैं?"
        
        elif lang == "hinglish":
            return "Bhai, samajh nahi aaya. 'Help' type karo ya clear batao kya janna hai?"
        
        else:
            return "I didn't understand. Type 'help' or ask clearly what you want to know."