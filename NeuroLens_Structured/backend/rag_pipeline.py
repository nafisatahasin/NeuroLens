# rag_pipeline.py
# Simulated RAG pipeline for retrieving solutions based on prediction

def get_rag_response(prediction_class):
    if prediction_class == 1:
        return "You appear drowsy. Please take a break and rest your eyes."
    else:
        return "You seem alert. Keep up the good focus!"
