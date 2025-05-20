import React, { useEffect, useState } from "react";
import axios from "axios";
import "../AuditLogs.css"; // Import the CSS file

const AuditLogs = () => {
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    axios
      .get("/api/audit-logs")
      .then((res) => setLogs(res.data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div className="auditlogs-container">
      <h2 className="auditlogs-title">Audit Logs</h2>
      <div className="auditlogs-table-container">
        <table className="auditlogs-table">
          <thead>
            <tr>
              <th>Timestamp</th>
              <th>User</th>
              <th>Action</th>
              <th>Details</th>
            </tr>
          </thead>
          <tbody>
            {logs.map((log, idx) => (
              <tr key={idx}>
                <td>{log.timestamp}</td>
                <td>{log.user}</td>
                <td>{log.action}</td>
                <td>{log.details}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default AuditLogs;
