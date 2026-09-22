import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Read the production data
data = pd.read_csv("data/production_data.csv")

# Calculate production shortfall
data["production_shortfall"] = (
    data["planned_production"] - data["actual_production"]
)

# Features used by the model
features = [
    "equipment_downtime",
    "rainfall",
    "soil_moisture",
    "temperature",
    "blasting_delay"
]

X = data[features]
y = data["production_shortfall"]

# Create the machine-learning model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# Train the model
model.fit(X, y)

print("Production shortfall model trained successfully!")

# New mining conditions for prediction
new_data = pd.DataFrame({
    "equipment_downtime": [7],
    "rainfall": [30],
    "soil_moisture": [60],
    "temperature": [27],
    "blasting_delay": [3]
})

# Predict production shortfall
prediction = model.predict(new_data)

print("\nPredicted Production Shortfall:")
print(round(prediction[0], 2), "tonnes")

# Show the importance of each factor
importance = pd.DataFrame({
    "factor": features,
    "importance": model.feature_importances_
})

importance = importance.sort_values(
    by="importance",
    ascending=False
)

print("\nFactors influencing production shortfall:")
print(importance)

# Classify the predicted shortfall risk
predicted_shortfall = prediction[0]

if predicted_shortfall < 5:
    risk = "Low Risk"
elif predicted_shortfall <= 15:
    risk = "Medium Risk"
else:
    risk = "High Risk"

print("\nShortfall Risk:")
print(risk)

# Save prediction results
results = pd.DataFrame({
    "predicted_shortfall": [round(predicted_shortfall, 2)],
    "risk_level": [risk]
})

results.to_csv("prediction_results.csv", index=False)

print("\nPrediction results saved successfully!")