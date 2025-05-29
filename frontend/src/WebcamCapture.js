import React, { useRef } from 'react';

function WebcamCapture() {
  const videoRef = useRef(null);

  const captureAndSend = async () => {
    // Placeholder for real landmark detection
    const dummyLandmarks = Array(30).fill(0.5);
    const response = await fetch('/predict', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ landmarks: dummyLandmarks })
    });
    const result = await response.json();
    alert(`Prediction: ${result.prediction}\nAdvice: ${result.solution}`);
  };

  return (
    <div>
      <button onClick={captureAndSend}>Simulate Capture</button>
    </div>
  );
}

export default WebcamCapture;
