import React from "react";
import { useNavigate } from "react-router-dom";
import "./StudentDashboard.css"; // Import the CSS file

const StudentDashboard = () => {
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem("token");
    sessionStorage.clear();
    navigate("/login");
  };

  const handleCertificates = () => {
    navigate("/certificates");
  };

  return (
    <>
      <button className="logout-btn" onClick={handleLogout}>Logout</button>
      <div className="fade-in">
        <h2>Student Dashboard</h2>
        <button className="certificates-btn" onClick={handleCertificates}>
          List of Certificates
        </button>
        {/* Student-specific content */}
      </div>
    </>
  );
};

export default StudentDashboard;
