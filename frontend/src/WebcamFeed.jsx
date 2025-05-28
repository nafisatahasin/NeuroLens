import React, { useRef, useState } from "react";
import Webcam from "react-webcam";

const WebcamFeed = () => {
  const webcamRef = useRef(null);
  const [feedback, setFeedback] = useState("");

  const captureAndSend = async () => {
    const screenshot = webcamRef.current.getScreenshot();
    const res = await fetch("https://neuro-backend.onrender.com/analyze", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ image: screenshot }),
    });
    const data = await res.json();
    setFeedback(data.tip || "No feedback available.");
  };

  return (
    <div>
      <Webcam
        audio={false}
        ref={webcamRef}
        screenshotFormat="image/jpeg"
        width={320}
      />
      <br />
      <button onClick={captureAndSend}>Analyze Attention</button>
      <p style={{ marginTop: "10px", fontWeight: "bold" }}>{feedback}</p>
    </div>
  );
};

export default WebcamFeed;
