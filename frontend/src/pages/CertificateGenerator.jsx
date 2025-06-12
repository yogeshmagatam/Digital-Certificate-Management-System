// Example: CertificateGenerator.jsx
import React, { useState } from "react";
import "../CertificateGenerator.css";

const CertificateGenerator = () => {
  const [showForm, setShowForm] = useState(false);
  const [form, setForm] = useState({
    name: "",
    event: "",
    date: "",
    email: "",
    template_type: 1,
  });
  const [success, setSuccess] = useState(false);

  const handleChange = (e) => {
    const value = e.target.name === 'template_type' ? parseInt(e.target.value) : e.target.value;
    setForm({ ...form, [e.target.name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    // Call your backend API to generate certificate
    const token = localStorage.getItem("token");
    const response = await fetch(
      "http://localhost:5000/api/certificates/generate-certificates",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify(form),
      }
    );
    if (response.ok) {
      setSuccess(true);
      setShowForm(false);
      alert("Certificate generated successfully!");
    } else {
      alert("Failed to generate certificate.");
    }
  };

  return (
    <div className="certificate-generator-container">
      <button
        onClick={() => setShowForm(true)}
        className="generate-button"
      >
        <span
          style={{
            position: "absolute",
            top: 0,
            left: 0,
            right: 0,
            bottom: 0,
            background: "linear-gradient(120deg, rgba(255,255,255,0.2) 30%, rgba(255,255,255,0.05) 70%)",
            backgroundSize: "200px 100%",
            backgroundRepeat: "no-repeat",
            animation: "shine 2.5s linear infinite",
            zIndex: 1,
            pointerEvents: "none",
            borderRadius: "12px",
          }}
        />
        <span style={{ position: "relative", zIndex: 2 }}>
          Generate Certificate
        </span>
      </button>
      {showForm && (
        <form onSubmit={handleSubmit} className="generate-form">
          <input
            name="name"
            placeholder="Name"
            value={form.name}
            onChange={handleChange}
            required
            className="form-input"
          />
          <input
            name="email"
            type="email"
            placeholder="Email"
            value={form.email}
            onChange={handleChange}
            required
            className="form-input"
          />
          <input
            name="event"
            placeholder="Event"
            value={form.event}
            onChange={handleChange}
            required
            className="form-input"
          />
          <input
            name="date"
            type="date"
            value={form.date}
            onChange={handleChange}
            required
            className="form-input"
          />
          <select
            name="template_type"
            value={form.template_type}
            onChange={handleChange}
            required
            className="form-input"
          >
            <option value={1}>Template 1</option>
            <option value={2}>Template 2</option>
          </select>
          <button type="submit" className="generate-button">
            Generate
          </button>
        </form>
      )}
      {success && (
        <div
          style={{
            marginTop: "36px",
            background: "linear-gradient(90deg, #f7971e 0%, #ffd200 100%)",
            color: "#333",
            padding: "22px 38px",
            borderRadius: "14px",
            fontWeight: "bold",
            fontSize: "1.18rem",
            boxShadow: "0 3px 12px rgba(247,151,30,0.13)",
            animation: "pop 0.7s cubic-bezier(.68,-0.55,.27,1.55)",
            zIndex: 2,
            position: "relative",
            border: "2px solid #fffbe6",
            letterSpacing: "0.5px",
          }}
        >
          <span role="img" aria-label="star" style={{ marginRight: 8 }}>
            🌟
          </span>
          Certificate generated and verified!
        </div>
      )}
    </div>
  );
};

export default CertificateGenerator;
