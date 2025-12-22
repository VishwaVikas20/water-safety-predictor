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

# Water Safety Predictor 🚰

A full-stack machine learning web application that predicts whether water is safe to drink. Built with **Flask** and **Scikit-Learn**.

## 📝 Overview
This project demonstrates an end-to-end machine learning workflow, moving from data analysis in Jupyter Notebooks to a deployed web application.

The goal was to build a system where users can input water quality metrics (like pH, Hardness, and Chloramines) and receive an instant prediction on whether the water is potable.

**Model Selection:**
During the development process, I initially experimented with the **XGBClassifier**. However, given the relatively small size of the dataset, I found that the **Random Forest Classifier** provided better stability and generalized better. Therefore, the final deployed model utilizes Random Forest.

## 🚀 Features
- **Interactive Web Interface:** A clean HTML/CSS frontend for user input.
- **ML Integration:** Connects a Python-based machine learning model to a web server.
- **Real-time Prediction:** Instant classification of water samples as "Potable" or "Not Potable."
- **Scalable Structure:** Built using Flask, allowing for easy expansion or model swapping.

## 🛠️ Tech Stack
- **Frontend:** HTML5, CSS3
- **Backend:** Flask (Python)
- **Machine Learning:** Scikit-Learn, Pandas, NumPy
- **Model:** Random Forest Classifier

## 📂 Project Structure
```text
├── templates/
│   └── index.html                    # User Interface
├── app.py                            # Flask Application (API & Routing)
├── PotabilityPredictor.pkl           # Final pipeline
├── water_potability.csv              # Dataset source
└── README.md
