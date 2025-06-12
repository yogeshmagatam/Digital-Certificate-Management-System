import React, { useEffect, useState } from "react";
import "../Dashboard.css"; 

const StudentCertificates = () => {
  const [certificates, setCertificates] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("http://localhost:5000/api/certificates/student/cert", {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    })
      .then((res) => {
        if (!res.ok) {
          throw new Error("Network response was not ok");
        }
        return res.json();
      })
      .then((data) => {
        setCertificates(data.certificates || []);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Failed to fetch certificates:", err);
        setLoading(false);
      });
  }, []);

  const handleDownload = async (certId) => {
    try {
      const response = await fetch(
        `http://localhost:5000/api/certificates/download/${certId}`,
        {
          headers: {
            Authorization: `Bearer ${localStorage.getItem("token")}`,
          },
        }
      );
      
      if (!response.ok) {
        throw new Error('Failed to download certificate');
      }
      
      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `certificate.pdf`;
      document.body.appendChild(a);
      a.click();
      window.URL.revokeObjectURL(url);
      document.body.removeChild(a);
    } catch (error) {
      console.error('Error downloading certificate:', error);
      alert('Failed to download certificate. Please try again.');
    }
  };

  if (loading) return (
    <div className="dashboard-container">
      <div className="loading">Loading certificates...</div>
    </div>
  );

  return (
    <div className="dashboard-container" style={{ position: "relative" }}>
      <h2 className="dashboard-title">Student Dashboard</h2>
      <ul className="dashboard-list">
        {certificates.length === 0 ? (
          <li className="no-certificates">No certificates found.</li>
        ) : (
          certificates.map((cert) => (
            <li key={cert.id} className="dashboard-item">
              <div className="certificate-details">
                <h3>{cert.name}</h3>
                <p>Event: {cert.event}</p>
                <p>Date: {cert.date}</p>
                <p>Email: {cert.email}</p>
                <button
                  onClick={() => handleDownload(cert.id)}
                  className="download-button"
                  style={{
                    backgroundColor: '#4CAF50',
                    color: 'white',
                    padding: '8px 16px',
                    border: 'none',
                    borderRadius: '4px',
                    cursor: 'pointer',
                    marginTop: '10px',
                    fontSize: '14px',
                    display: 'flex',
                    alignItems: 'center',
                    gap: '8px'
                  }}
                >
                  <span>📥</span> Download Certificate
                </button>
              </div>
            </li>
          ))
        )}
      </ul>
    </div>
  );
};

export default StudentCertificates;
