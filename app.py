import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from sklearn.ensemble import RandomForestRegressor

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Manganese AI",
    page_icon="⛏️",
    layout="wide"
)

# =========================================================
# TITLE
# =========================================================

st.title("⛏️ Manganese AI - Mining Production Dashboard")

st.write(
    "AI/ML based system for manganese reserve analysis "
    "and production shortfall prediction."
)

# =========================================================
# LOAD DATA
# =========================================================

data = pd.read_csv("data/production_data.csv")

reserve_data = pd.read_csv("data/reserve_data.csv")

prediction = pd.read_csv("prediction_results.csv")

# =========================================================
# CALCULATE PRODUCTION SHORTFALL
# =========================================================

data["production_shortfall"] = (
    data["planned_production"]
    - data["actual_production"]
)

# =========================================================
# EXISTING ML PREDICTION
# =========================================================

predicted_shortfall = prediction[
    "predicted_shortfall"
].iloc[0]

risk_level = prediction[
    "risk_level"
].iloc[0]

# =========================================================
# TRAIN INTERACTIVE ML MODEL
# =========================================================

features = [
    "equipment_downtime",
    "rainfall",
    "soil_moisture",
    "temperature",
    "blasting_delay"
]

X = data[features]

y = data["production_shortfall"]

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

# =========================================================
# PRODUCTION OVERVIEW
# =========================================================

st.subheader("📊 Production Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Average Shortfall",
        f"{data['production_shortfall'].mean():.2f} tonnes"
    )

with col2:
    st.metric(
        "Highest Shortfall",
        f"{data['production_shortfall'].max()} tonnes"
    )

with col3:
    st.metric(
        "Predicted Shortfall",
        f"{predicted_shortfall:.2f} tonnes"
    )

# =========================================================
# PRODUCTION RISK
# =========================================================

st.subheader("⚠️ Production Risk")

if risk_level == "High Risk":

    st.error("🚨 High Risk")

elif risk_level == "Medium Risk":

    st.warning("⚠️ Medium Risk")

else:

    st.success("✅ Low Risk")

# =========================================================
# PLANNED VS ACTUAL PRODUCTION
# =========================================================

st.subheader("📈 Planned vs Actual Production")

chart_data = data[
    [
        "date",
        "planned_production",
        "actual_production"
    ]
].set_index("date")

st.line_chart(chart_data)

# =========================================================
# FACTORS AFFECTING SHORTFALL
# =========================================================

st.subheader(
    "📊 Factors Affecting Production Shortfall"
)

factor_data = data[features].mean()

st.bar_chart(factor_data)

# =========================================================
# INTERACTIVE AI PREDICTOR
# =========================================================

st.subheader(
    "🤖 Interactive Production Shortfall Predictor"
)

st.write(
    "Enter expected mining conditions to estimate "
    "the possible production shortfall."
)

col1, col2 = st.columns(2)

with col1:

    equipment_input = st.number_input(
        "Equipment Downtime (hours)",
        min_value=0.0,
        max_value=24.0,
        value=5.0,
        step=1.0
    )

    rainfall_input = st.number_input(
        "Rainfall (mm)",
        min_value=0.0,
        max_value=200.0,
        value=30.0,
        step=1.0
    )

    soil_input = st.number_input(
        "Soil Moisture (%)",
        min_value=0.0,
        max_value=100.0,
        value=40.0,
        step=1.0
    )

with col2:

    temperature_input = st.number_input(
        "Temperature (°C)",
        min_value=0.0,
        max_value=60.0,
        value=28.0,
        step=1.0
    )

    blasting_input = st.number_input(
        "Blasting Delay (hours)",
        min_value=0.0,
        max_value=24.0,
        value=1.0,
        step=1.0
    )

# =========================================================
# PREDICT BUTTON
# =========================================================

if st.button("🔮 Predict Production Shortfall"):

    input_data = pd.DataFrame({
        "equipment_downtime": [equipment_input],
        "rainfall": [rainfall_input],
        "soil_moisture": [soil_input],
        "temperature": [temperature_input],
        "blasting_delay": [blasting_input]
    })

    predicted_value = model.predict(
        input_data
    )[0]

    # ---------------------------------------------
    # RESULT
    # ---------------------------------------------

    st.subheader("🔮 AI Prediction Result")

    st.metric(
        "Predicted Production Shortfall",
        f"{predicted_value:.2f} tonnes"
    )

    # ---------------------------------------------
    # RISK CALCULATION
    # ---------------------------------------------

    if predicted_value >= 15:

        st.error("🚨 High Risk")

        st.write(
            "Recommended action: Check equipment "
            "availability, rainfall conditions and "
            "blasting delays."
        )

    elif predicted_value >= 8:

        st.warning("⚠️ Medium Risk")

        st.write(
            "Recommended action: Monitor equipment "
            "and environmental conditions closely."
        )

    else:

        st.success("✅ Low Risk")

        st.write(
            "Current conditions indicate a relatively "
            "low production shortfall risk."
        )

# =========================================================
# AI RECOMMENDATION
# =========================================================

st.subheader("🤖 AI Recommendation")

if risk_level == "High Risk":

    st.error(
        "High production shortfall risk detected. "
        "Consider checking equipment downtime, "
        "rainfall conditions and blasting delays."
    )

elif risk_level == "Medium Risk":

    st.warning(
        "Medium production shortfall risk detected. "
        "Monitor equipment and environmental conditions."
    )

else:

    st.success(
        "Low production shortfall risk. "
        "Current conditions appear relatively stable."
    )

# =========================================================
# MANGANESE RESERVE ANALYSIS
# =========================================================

st.subheader("⛏️ Manganese Reserve Analysis")

st.dataframe(
    reserve_data,
    use_container_width=True
)

# =========================================================
# MANGANESE GRADE BY AREA
# =========================================================

st.subheader("🧪 Manganese Grade by Area")

grade_data = reserve_data[
    [
        "location",
        "manganese_grade"
    ]
].set_index("location")

st.bar_chart(grade_data)

# =========================================================
# RESERVE SUMMARY
# =========================================================

col1, col2 = st.columns(2)

with col1:

    average_grade = reserve_data[
        "manganese_grade"
    ].mean()

    st.metric(
        "Average Manganese Grade",
        f"{average_grade:.2f}%"
    )

with col2:

    total_reserve = reserve_data[
        "estimated_reserve"
    ].sum()

    st.metric(
        "Estimated Total Reserve",
        f"{total_reserve:,} tonnes"
    )

# =========================================================
# RESERVE LOCATION MAP
# =========================================================

st.subheader("🗺️ Manganese Reserve Locations")

reserve_map = folium.Map(
    location=[
        reserve_data["latitude"].mean(),
        reserve_data["longitude"].mean()
    ],
    zoom_start=10,
    tiles=None
)

# =========================================================
# NORMAL MAP
# =========================================================

folium.TileLayer(
    tiles="OpenStreetMap",
    name="🗺️ Normal Map",
    overlay=False,
    control=True
).add_to(reserve_map)

# =========================================================
# SATELLITE MAP
# =========================================================

folium.TileLayer(
    tiles=(
        "https://server.arcgisonline.com/"
        "ArcGIS/rest/services/World_Imagery/"
        "MapServer/tile/{z}/{y}/{x}"
    ),
    attr="Esri",
    name="🛰️ Satellite Imagery",
    overlay=False,
    control=True
).add_to(reserve_map)

# =========================================================
# RESERVE MARKERS
# =========================================================

for _, row in reserve_data.iterrows():

    if row["manganese_grade"] >= 45:

        marker_color = "red"
        potential = "High Potential"

    elif row["manganese_grade"] >= 35:

        marker_color = "orange"
        potential = "Medium Potential"

    else:

        marker_color = "blue"
        potential = "Lower Potential"

    folium.Marker(
        location=[
            row["latitude"],
            row["longitude"]
        ],

        popup=(
            f"<b>{row['location']}</b><br>"
            f"Manganese Grade: "
            f"{row['manganese_grade']}%<br>"
            f"Estimated Reserve: "
            f"{row['estimated_reserve']:,} tonnes<br>"
            f"Potential: {potential}"
        ),

        tooltip=(
            f"{row['location']} - {potential}"
        ),

        icon=folium.Icon(
            color=marker_color,
            icon="info-sign"
        )

    ).add_to(reserve_map)

# =========================================================
# MAP SWITCHER
# =========================================================

folium.LayerControl(
    position="topright",
    collapsed=False
).add_to(reserve_map)

# =========================================================
# DISPLAY MAP
# =========================================================

st_folium(
    reserve_map,
    width=1000,
    height=500
)

# =========================================================
# PRODUCTION DATA
# =========================================================

st.subheader("📋 Production Data")

st.dataframe(
    data,
    use_container_width=True
)

# =========================================================
# PROJECT STATUS
# =========================================================

st.success(
    "✅ Manganese AI prototype is operational."
)