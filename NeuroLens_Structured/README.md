# NeuroLens

**NeuroLens** is an AI-powered real-time drowsiness detection system using webcam inputs, ML (XGBoost), and a Retrieval-Augmented Generation (RAG) response system for actionable feedback.

## 📁 Structure
```
NeuroLens/
├── backend/
│   ├── app.py
│   ├── model_utils.py
│   ├── rag_pipeline.py
│   ├── requirements.txt
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.js
│   │   ├── WebcamCapture.js
│   │   ├── SolutionBox.js
├── ml_models/
│   └── attention_model.pkl
```

## 🚀 Run the Project

1. **Backend**
```bash
cd backend
pip install -r requirements.txt
python app.py
```

2. **Frontend**
Use any React development server or Vite setup:
```bash
npm install
npm start
```

Ensure model `attention_model.pkl` is present in `ml_models/`.

## 🔍 How it works

- Webcam simulates sending landmarks
- ML model predicts drowsiness
- RAG generates contextual advice
