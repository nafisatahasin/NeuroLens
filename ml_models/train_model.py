from sklearn.ensemble import RandomForestClassifier
import numpy as np
import joblib

X = np.random.rand(200, 4096)
y = np.random.choice([0, 1], 200)

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "attention_model.pkl")
print("Model saved.")
