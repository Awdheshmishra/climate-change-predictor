import numpy as np
import pandas as pd
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.preprocessing import MinMaxScaler
import joblib
import os

class ClimatePredictor:
    def __init__(self):
        self.model = None
        self.scaler = MinMaxScaler()
        self.lookback = 5  # Reduced from 10 for small dataset
        self.data_path = os.path.join(os.path.dirname(__file__), '../data/historical_data.csv')
        
    def load_data(self):
        """Load historical climate data"""
        try:
            df = pd.read_csv(self.data_path)
            print(f"✅ Data loaded successfully: {len(df)} rows")
            return df
        except Exception as e:
            print(f"❌ Error loading data: {e}")
            # Create sample data if file not found
            return self.create_sample_data()
    
    def create_sample_data(self):
        """Create sample data if CSV not found"""
        data = {
            'year': list(range(1980, 2025)),
            'global_temp': [14.12 + (i * 0.02) + (np.random.random() * 0.1) for i in range(45)],
            'lucknow_temp': [23.5 + (i * 0.025) for i in range(45)],
            'delhi_temp': [24.2 + (i * 0.027) for i in range(45)],
            'mumbai_temp': [26.8 + (i * 0.02) for i in range(45)],
            'co2_level': [338 + (i * 1.8) for i in range(45)]
        }
        return pd.DataFrame(data)
    
    def build_model(self):
        """Build CNN-LSTM hybrid model"""
        model = keras.Sequential([
            layers.LSTM(50, return_sequences=True, input_shape=(self.lookback, 1)),
            layers.LSTM(50),
            layers.Dense(25, activation='relu'),
            layers.Dense(1)
        ])
        
        model.compile(optimizer='adam', loss='mse', metrics=['mae'])
        self.model = model
        return model
    
    def train(self):
        """Train the model on historical data"""
        df = self.load_data()
        
        if df is None or len(df) < self.lookback + 1:
            print("❌ Not enough data to train model")
            return None
        
        temps = df['global_temp'].values.reshape(-1, 1)
        
        # Normalize
        scaled_temps = self.scaler.fit_transform(temps)
        
        # Create sequences
        X, y = [], []
        for i in range(self.lookback, len(scaled_temps)):
            X.append(scaled_temps[i-self.lookback:i, 0])
            y.append(scaled_temps[i, 0])
        
        X = np.array(X)
        y = np.array(y)
        
        # Check if we have data
        if len(X) == 0:
            print("❌ No training data created")
            return None
        
        # Reshape for LSTM
        X = X.reshape((X.shape[0], X.shape[1], 1))
        
        print(f"✅ Training data shape: X={X.shape}, y={y.shape}")
        
        # Build and train
        if not self.model:
            self.build_model()
        
        self.model.fit(X, y, epochs=50, batch_size=1, verbose=1)
        
        # Save scaler
        model_path = os.path.join(os.path.dirname(__file__), 'scaler.pkl')
        joblib.dump(self.scaler, model_path)
        
        print("✅ Model trained successfully")
        return self.model
    
    def predict_future(self, years_ahead=26):
        """Predict temperature for future years"""
        if not self.model:
            self.load_model()
        
        df = self.load_data()
        temps = df['global_temp'].values.reshape(-1, 1)
        scaled_temps = self.scaler.transform(temps)
        
        # Get last sequence
        last_seq = scaled_temps[-self.lookback:].reshape(1, self.lookback, 1)
        
        predictions = []
        current_seq = last_seq
        
        for _ in range(years_ahead):
            pred = self.model.predict(current_seq, verbose=0)
            predictions.append(pred[0, 0])
            # Update sequence
            new_seq = np.roll(current_seq[0], -1, axis=0)
            new_seq[-1] = pred[0, 0]
            current_seq = new_seq.reshape(1, self.lookback, 1)
        
        # Inverse transform
        predictions = self.scaler.inverse_transform(
            np.array(predictions).reshape(-1, 1)
        )
        
        return predictions.flatten()
    
    def load_model(self):
        """Load trained model"""
        model_path = os.path.join(os.path.dirname(__file__), 'climate_model.h5')
        scaler_path = os.path.join(os.path.dirname(__file__), 'scaler.pkl')
        
        if os.path.exists(model_path) and os.path.exists(scaler_path):
            try:
                self.model = keras.models.load_model(model_path)
                self.scaler = joblib.load(scaler_path)
                print("✅ Model loaded from disk")
                return
            except Exception as e:
                print(f"⚠️ Error loading model: {e}")
        
        print("🔄 Training new model...")
        self.train()
        
        # Save model
        if self.model:
            self.model.save(model_path)
            joblib.dump(self.scaler, scaler_path)