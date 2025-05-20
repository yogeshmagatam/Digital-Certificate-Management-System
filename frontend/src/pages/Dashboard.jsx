import React from "react";
import { Link } from "react-router-dom";

const Dashboard = () => {
  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold mb-4">Admin Dashboard</h2>
      <ul className="space-y-4">
        <li>
          <Link to="/generate" className="text-blue-600">
            Generate Certificates
          </Link>
        </li>
        <li>
          <Link to="/wallet" className="text-blue-600">
            My Wallet
          </Link>
        </li>
        <li>
          <Link to="/logs" className="text-blue-600">
            Audit Logs
          </Link>
        </li>
      </ul>
    </div>
  );
};

export default Dashboard;
