import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import "../Login.css"; 

const Login = () => {
  const navigate = useNavigate();
  const [isRegister, setIsRegister] = useState(false);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(
        "http://localhost:5000/api/auth/login",
        { email, password }
      );
      localStorage.setItem("role", response.data.role);
      if (response.data.token) {
        localStorage.setItem("token", response.data.token);
      }
      alert("Login successful!");
      navigate("/dashboard");
    } catch (error) {
      alert(error.response?.data?.msg || error.message || "Login failed");
    }
  };

  const handleRegister = async (e) => {
    e.preventDefault();
    try {
       await axios.post("http://localhost:5000/api/auth/register", {
        email,
        password,
        role: "student", // Always register as student
      });
      alert("Registration successful! Please login.");
      setIsRegister(false);
      setEmail("");
      setPassword("");
    } catch (error) {
      alert(
        error.response?.data?.msg || error.message || "Registration failed"
      );
    }
  };

  return (
    <div className="login-container">
      <div className={`login-card${isRegister ? " registering" : ""}`}>
        <h2>{isRegister ? "Register" : "Login"}</h2>
        <form
          onSubmit={isRegister ? handleRegister : handleLogin}
          className="login-form"
        >
          <input
            type="email"
            placeholder="Email"
            value={email}
            required
            onChange={(e) => setEmail(e.target.value)}
            className="login-input"
          />
          <input
            type="password"
            placeholder="Password"
            value={password}
            required
            onChange={(e) => setPassword(e.target.value)}
            className="login-input"
          />
          <button type="submit" className="login-button">
            {isRegister ? "Register" : "Login"}
          </button>
        </form>
        <button
          className="login-toggle"
          onClick={() => setIsRegister((prev) => !prev)}
          style={{ marginTop: "10px" }}
        >
          {isRegister
            ? "Already have an account? Login"
            : "Don't have an account? Register"}
        </button>
      </div>
    </div>
  );
};

export default Login;
