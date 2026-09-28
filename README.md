# Manganese AI

## AI/ML and Space Technology for Manganese Reserve Identification and Production Shortfall Prediction

Manganese AI is a prototype dashboard that uses Artificial Intelligence, Machine Learning, and satellite-inspired environmental data to analyze manganese mining operations.

The system focuses on two major areas:

1. Manganese reserve analysis
2. Production shortfall prediction

## Features

- 📊 Production data analysis
- 🤖 AI-based production shortfall prediction
- ⚠️ Production risk classification
- 🧠 Mining Health Score
- 📍 Manganese reserve location visualization
- 🗺️ Interactive reserve map
- 📈 Planned vs Actual Production analysis
- 🌧️ Environmental factor analysis
- 🔧 Equipment downtime analysis
- 💥 Blasting delay analysis
- 💡 AI-based recommendations
- 🔮 Interactive production shortfall predictor

## Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- Folium
- Streamlit-Folium
- Git & GitHub

## Machine Learning

The project uses a Random Forest Regression model to predict production shortfall.

The model considers factors such as:

- Equipment downtime
- Rainfall
- Soil moisture
- Temperature
- Blasting delay

Production shortfall is calculated as:

Production Shortfall = Planned Production - Actual Production

## Project Structure

```text
manganese_ai/
│
├── app.py
├── production_model.py
├── read_data.py
├── test.py
├── prediction_results.csv
├── requirements.txt
├── .gitignore
│
└── data/
    ├── production_data.csv
    └── reserve_data.csv
