# HeArtInizer: AI-Based Heart Rate Stabilizer

An intelligent heart rate control system using Adaptive Neuro-Fuzzy Inference System (ANFIS) designed to personalize and stabilize cardiac rhythms in real-time.

## 🧠 Architecture Diagram
![Architecture Diagram](./Architecture%20Diagram.jpg)

## 🚀 Overview
HeArtInizer leverages the strengths of fuzzy logic and neural networks to adaptively regulate heart rate under dynamic physiological conditions like rest, exercise, and stress. It aims to improve upon conventional PID-based controllers by offering personalized and accurate control with minimal delay and overshoot.

## 🧠 Key Features
- **ANFIS Controller**: Adaptive Neuro-Fuzzy system trained on real-world physiological data.
- **Personalization**: Learns individual heart rate patterns for tailored control.
- **Real-time Monitoring**: Simulates real-time heart rate tracking and prediction.
- **High Accuracy**: Achieves 93–98% precision in heart rate stabilization.
- **Gradient Descent Optimization**: Fine-tunes parameters dynamically to reduce MSE.

## 📊 Dataset
Used the [Bellabeat Fitbit Dataset](https://www.kaggle.com/datasets/kyle007hendricks/bellabeat-dataset) containing second-by-second heart rate data and user activity.

## 🧪 Results
- **MSE Reduced**: From 39.29 → 0.079
- **Settling Time**: ~1.23 seconds
- **Overshoot**: <1.5%
- **Accuracy**: 93–98%

## 🔧 Technologies Used
- Python
- ANFIS (Neuro-Fuzzy)
- Time Series Analysis
- Gradient Descent
- Fuzzy Logic
- PID and FO-PID comparison

## 📈 Future Scope
- Integration with wearable devices
- Clinical testing and IoMT deployment
- Expansion to multi-physiological signal stabilization (e.g., BP, ECG)

---

🧠 A project that bridges biomedical engineering and AI for personalized cardiovascular health.
