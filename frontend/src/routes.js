// src/routes.js
import { Routes, Route } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import Verify from "./pages/Verify";
import Login from "./pages/Login";
import AuditLogs from "./pages/AuditLogs";
import GenerateCertificate from "./pages/CertificateGenerator";
import StudentCertificates from "./pages/StudentCertificates";

export default function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<Login />} />
      <Route path="/dashboard" element={<Dashboard />} />
      <Route path="/generate" element={<GenerateCertificate />} />
      <Route path="/verify/:certificateId" element={<Verify />} />
      <Route path="/logs" element={<AuditLogs />} />
      <Route path="/student-info" element={<StudentCertificates />} />
      <Route path="*" element={<Login />} />
    </Routes>
  );
}
