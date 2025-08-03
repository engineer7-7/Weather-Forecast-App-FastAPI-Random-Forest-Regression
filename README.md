# 🌤️ Weather Forecast App

This is a full-stack weather forecasting web application built with **FastAPI** (backend) and **HTML + Bootstrap** (frontend).  
It uses **live weather data** from the [OpenWeatherMap API](https://openweathermap.org/api) to **train a machine learning model** that predicts the average temperature for any city worldwide within the next 5 days.

---

## 🚀 Features

- 🔍 Predict temperature by **city and date**
- 📅 Date selection limited to **today + 5 days**
- 🌡️ Results shown in both **Celsius (°C)** and **Fahrenheit (°F)**
- 🌙 Dark mode support (toggle switch)
- 🧠 Trained **Random Forest Regressor** model
- 📦 Feature scaling with `StandardScaler`
- 🎯 Accurate predictions using real-time OpenWeatherMap API data
- ⚡ Built with **FastAPI**, **Jinja2**, and **Bootstrap 5**
