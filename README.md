# NeuroLens

NeuroLens is a real-time attention monitoring system that uses a webcam, AI/ML, and a web interface to detect if a user is attentive or distracted.

## Features
- React frontend with webcam integration
- Flask backend to process image data
- Simple ML model (Random Forest) to classify attention
- Realtime feedback to users

## Project Structure
```
NeuroLens/
├── backend/             # Flask backend
├── frontend/            # React frontend
└── ml_models/           # ML model training and storage
```

## Setup Instructions

### Backend
1. Navigate to the backend folder:
    ```
    cd backend
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    pip install -r requirements.txt
    python app.py
    ```

### Frontend
1. Navigate to the frontend folder:
    ```
    cd frontend
    npm install
    npm start
    ```

### Model
1. Go to `ml_models` and run:
    ```
    python train_model.py
    ```

Make sure you have Python and Node.js installed.
