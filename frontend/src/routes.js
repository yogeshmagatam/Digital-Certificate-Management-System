import { Routes, Route } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import Verify from "./pages/Verify";
import Login from "./pages/Login";
import AuditLogs from "./pages/AuditLogs";
import GenerateCertificate from "./pages/CertificateGenerator";
import StudentCertificates from "./pages/StudentCertificates";
import PrivateRoute from "./components/PrivateRoute";

export default function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<Login />} />
      <Route
        path="/dashboard"
        element={
          <PrivateRoute>
            <Dashboard />
          </PrivateRoute>
        }
      />
      <Route
        path="/generate"
        element={
          <PrivateRoute>
            <GenerateCertificate />
          </PrivateRoute>
        }
      />
      <Route path="/verify/:certificateId" element={<Verify />} />
      <Route
        path="/logs"
        element={
          <PrivateRoute>
            <AuditLogs />
          </PrivateRoute>
        }
      />
      <Route
        path="/student-info"
        element={
          <PrivateRoute>
            <StudentCertificates />
          </PrivateRoute>
        }
      />
      <Route path="*" element={<Login />} />
    </Routes>
  );
}
