import React, { useState } from "react";
import axios from "axios";
import UploadForm from "./components/UploadForm";
import Results from "./components/Results";
import "./styles.css";

function App() {
  const [prediction, setPrediction] = useState(null);

  const handleUpload = async (image, callback) => {
    const formData = new FormData();
    formData.append("file", image);

    try {
      const response = await axios.post("http://127.0.0.1:8000/predict/", formData);
      setPrediction(response.data);
    } catch (error) {
      console.error("Error:", error);
      alert("Prediction failed.");
    }
    callback();
  };

  return (
    <div className="container">
      <h2>Pathogen Detector AI</h2>
      <UploadForm onUpload={handleUpload} />
      <Results prediction={prediction} />
    </div>
  );
}

export default App;
