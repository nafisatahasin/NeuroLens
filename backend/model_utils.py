# model_utils.py
# Utility functions for processing input data

import numpy as np

def preprocess_input(landmarks):
    # Flatten the landmark list
    return np.array(landmarks).flatten()
