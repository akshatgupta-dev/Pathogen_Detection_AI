import React from "react";

const Results = ({ prediction }) => {
  if (!prediction) return null;

  return (
    <div className="results">
      <h3>Prediction Results:</h3>
      <p><strong>Bacteria Type:</strong> {prediction.bacteria_type}</p>
      {/* <p><strong>Antibiotic Resistance:</strong> {prediction.resistance}</p> */}
    </div>
  );
};

export default Results;
