import pandas as pd

# Read the production data
data = pd.read_csv("data/production_data.csv")

# Calculate production shortfall
data["production_shortfall"] = (
    data["planned_production"] - data["actual_production"]
)

# Display the data
print(data)

# Display the shortfall column
print("\nProduction Shortfall:")
print(data[["date", "production_shortfall"]])

# Find the day with the highest shortfall
worst_day = data.loc[data["production_shortfall"].idxmax()]

print("\nHighest Production Shortfall:")
print(worst_day)

# Calculate average production shortfall
average_shortfall = data["production_shortfall"].mean()

print("\nAverage Production Shortfall:")
print(round(average_shortfall, 2))