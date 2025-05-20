import React, { useEffect, useState } from "react";
import axios from "axios";

const AuditLogs = () => {
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    axios
      .get("/api/audit-logs")
      .then((res) => setLogs(res.data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold mb-4">Audit Logs</h2>
      <div className="overflow-auto">
        <table className="min-w-full border text-left">
          <thead>
            <tr className="bg-gray-100">
              <th className="p-2 border">Timestamp</th>
              <th className="p-2 border">User</th>
              <th className="p-2 border">Action</th>
              <th className="p-2 border">Details</th>
            </tr>
          </thead>
          <tbody>
            {logs.map((log, idx) => (
              <tr key={idx}>
                <td className="p-2 border">{log.timestamp}</td>
                <td className="p-2 border">{log.user}</td>
                <td className="p-2 border">{log.action}</td>
                <td className="p-2 border">{log.details}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default AuditLogs;
