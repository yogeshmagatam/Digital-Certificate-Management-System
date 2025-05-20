import React from "react";
import { Link } from "react-router-dom";
import "../Dashboard.css"; // Import the CSS file

const Dashboard = () => {
  return (
    <div className="dashboard-container">
      <h2 className="dashboard-title">Admin Dashboard</h2>
      <ul className="dashboard-list">
        <li>
          <Link to="/generate" className="dashboard-link">
            Generate Certificates
          </Link>
        </li>
        <li>
          <Link to="/wallet" className="dashboard-link">
            My Wallet
          </Link>
        </li>
        <li>
          <Link to="/logs" className="dashboard-link">
            Audit Logs
          </Link>
        </li>
      </ul>
    </div>
  );
};

export default Dashboard;
