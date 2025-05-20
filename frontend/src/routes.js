// src/routes.js
import { Routes, Route } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import Generator from "./pages/Generator";
import Wallet from "./pages/Wallet";
import Verify from "./pages/Verify";
import Login from "./pages/Login";
import AuditLogs from "./pages/AuditLogs";

export default function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<Login />} />
      <Route path="/dashboard" element={<Dashboard />} />
      <Route path="/generate" element={<Generator />} />
      <Route path="/wallet" element={<Wallet />} />
      <Route path="/verify/:certificateId" element={<Verify />} />
      <Route path="/logs" element={<AuditLogs />} />
    </Routes>
  );
}
