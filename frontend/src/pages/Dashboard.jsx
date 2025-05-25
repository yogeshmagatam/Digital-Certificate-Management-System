import React, { useEffect } from "react";
import { Link, useNavigate } from "react-router-dom";
import "../Dashboard.css";
import LogoutButton from "../components/LogoutButton";

const Dashboard = () => {
  const navigate = useNavigate();
  const role = (localStorage.getItem("role") || "").toLowerCase().trim();

  useEffect(() => {
    if (!role) {
      navigate("/login");
    }
  }, [role, navigate]);

  // Debug: See what role is being read
  console.log("Role from localStorage:", role);

  return (
    <div className="dashboard-container" style={{ position: "relative" }}>
      <h2 className="dashboard-title">
        {role === "admin" ? "Admin Dashboard" : "Student Dashboard"}
      </h2>
      <ul className="dashboard-list">
        {role === "admin" ? (
          <>
            <li>
              <Link to="/generate" className="dashboard-link">
                Generate Certificates
              </Link>
            </li>
            <li>
              <Link to="/logs" className="dashboard-link">
                Audit Logs
              </Link>
            </li>
          </>
        ) : role === "student" ? (
          <>
            <li>
              <Link to="/student-info" className="dashboard-link">
                Student Information
              </Link>
            </li>
          </>
        ) : null}
      </ul>
      <LogoutButton />
    </div>
  );
};

export default Dashboard;
