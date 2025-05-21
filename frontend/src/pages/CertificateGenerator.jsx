// Example: CertificateGenerator.jsx
import React, { useState } from "react";

const CertificateGenerator = () => {
  const [showForm, setShowForm] = useState(false);
  const [form, setForm] = useState({
    name: "",
    event: "",
    date: "",
    email: "",
  });
  const [success, setSuccess] = useState(false);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
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
      // Optionally, verify certificate here or show a message
      alert("Certificate generated successfully!");
    } else {
      alert("Failed to generate certificate.");
    }
  };

  return (
    <div>
      <button onClick={() => setShowForm(true)}>Generate Certificate</button>
      {showForm && (
        <form onSubmit={handleSubmit}>
          <input
            name="name"
            placeholder="Name"
            value={form.name}
            onChange={handleChange}
            required
          />
          <input
            name="email"
            type="email"
            placeholder="Email"
            value={form.email}
            onChange={handleChange}
            required
          />
          <input
            name="event"
            placeholder="Event"
            value={form.event}
            onChange={handleChange}
            required
          />
          <input
            name="date"
            type="date"
            value={form.date}
            onChange={handleChange}
            required
          />
          <button type="submit">Submit</button>
        </form>
      )}
      {success && <div>Certificate generated and verified!</div>}
    </div>
  );
};

export default CertificateGenerator;
