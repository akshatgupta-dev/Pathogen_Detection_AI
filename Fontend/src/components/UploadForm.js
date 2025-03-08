import React, { useState } from "react";

const UploadForm = ({ onUpload }) => {
  const [image, setImage] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleImageChange = (event) => {
    setImage(event.target.files[0]);
  };

  const handleSubmit = () => {
    if (!image) {
      alert("Please upload an image.");
      return;
    }
    setLoading(true);
    onUpload(image, () => setLoading(false));
  };

  return (
    <div className="upload-container">
      <input type="file" onChange={handleImageChange} />
      <button onClick={handleSubmit} disabled={loading}>
        {loading ? "Processing..." : "Upload & Analyze"}
      </button>
    </div>
  );
};

export default UploadForm;
