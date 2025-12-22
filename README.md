# Water Safety Predictor 🚰

A full-stack machine learning web application that predicts whether water is safe to drink. Built with **Flask** and **Scikit-Learn**.

## 📝 Overview
This project demonstrates an end-to-end machine learning workflow, moving from data analysis in Jupyter Notebooks to a deployed web application.

The goal was to build a system where users can input water quality metrics (like pH, Hardness, and Chloramines) and receive an instant prediction on whether the water is potable.

I tried with XGBClassifier but the data was small so I finished this with RandomForestClassifier

## 🚀 Features
- **Interactive Web Interface:** A clean webpage for user input.
- **ML Integration:** Connects a Python-based machine learning model to a web server.
- **Real-time Prediction:** Instant classification of water samples as "Potable" or "Not Potable."
- **Scalable Structure:** Built using Flask, allowing for easy expansion or model swapping.

## 🛠️ Tech Stack
- **Frontend:** HTML5, Bootstrap
- **Backend:** Flask (Python)
- **Machine Learning:** Scikit-Learn, Pandas, Matplotlib

