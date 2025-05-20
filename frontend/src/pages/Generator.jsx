// src/pages/Generator.jsx
import React, { useState } from "react";
import axios from "axios";
import "../Generator.css"; // Import the CSS file

function Generator() {
  const [file, setFile] = useState(null);

  const uploadFile = () => {
    const formData = new FormData();
    formData.append("file", file);
    axios
      .post("http://127.0.0.1:5000/api/generate-certificates", formData)
      .then((res) => alert("Certificates Generated!"))
      .catch((err) => console.error(err));
  };

  return (
    <div className="generator-container">
      <div className="generator-card">
        <input
          className="generator-input"
          type="file"
          accept=".csv"
          onChange={(e) => setFile(e.target.files[0])}
        />
        <button className="generator-button" onClick={uploadFile}>
          Generate Certificates
        </button>
      </div>
    </div>
  );
}

export default Generator;
