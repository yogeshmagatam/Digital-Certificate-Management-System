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
    <div
      style={{
        minHeight: "100vh",
        background: "linear-gradient(135deg, #e0eafc 0%, #cfdef3 100%)",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        fontFamily: "Segoe UI, sans-serif",
        position: "relative",
        overflow: "hidden",
      }}
    >
      {/* Animated floating shapes */}
      <div
        style={{
          position: "absolute",
          top: "10%",
          left: "5%",
          width: "80px",
          height: "80px",
          background: "radial-gradient(circle, #667eea 60%, #fff0 100%)",
          borderRadius: "50%",
          opacity: 0.25,
          animation: "float1 6s ease-in-out infinite",
          zIndex: 0,
        }}
      />
      <div
        style={{
          position: "absolute",
          bottom: "15%",
          right: "8%",
          width: "100px",
          height: "100px",
          background: "radial-gradient(circle, #43cea2 60%, #fff0 100%)",
          borderRadius: "50%",
          opacity: 0.18,
          animation: "float2 7s ease-in-out infinite",
          zIndex: 0,
        }}
      />
      <style>
        {`
          @keyframes float1 {
            0% { transform: translateY(0px);}
            50% { transform: translateY(-30px);}
            100% { transform: translateY(0px);}
          }
          @keyframes float2 {
            0% { transform: translateY(0px);}
            50% { transform: translateY(40px);}
            100% { transform: translateY(0px);}
          }
          @keyframes pop {
            0% { transform: scale(0.8); opacity: 0.5;}
            80% { transform: scale(1.05);}
            100% { transform: scale(1); opacity: 1;}
          }
          @keyframes shine {
            0% { background-position: -200px; }
            100% { background-position: 200px; }
          }
        `}
      </style>
      <button
        onClick={() => setShowForm(true)}
        style={{
          padding: "14px 34px",
          fontSize: "1.2rem",
          background: "linear-gradient(90deg, #667eea 0%, #764ba2 100%)",
          color: "#fff",
          border: "none",
          borderRadius: "12px",
          cursor: "pointer",
          boxShadow: "0 6px 18px rgba(118,75,162,0.18)",
          marginBottom: "38px",
          transition: "background 0.3s, transform 0.2s",
          animation: "pop 0.7s cubic-bezier(.68,-0.55,.27,1.55)",
          position: "relative",
          overflow: "hidden",
        }}
        onMouseOver={(e) => (e.currentTarget.style.transform = "scale(1.06)")}
        onMouseOut={(e) => (e.currentTarget.style.transform = "scale(1)")}
      >
        <span
          style={{
            position: "absolute",
            top: 0,
            left: 0,
            right: 0,
            bottom: 0,
            background:
              "linear-gradient(120deg, rgba(255,255,255,0.2) 30%, rgba(255,255,255,0.05) 70%)",
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
        <form
          onSubmit={handleSubmit}
          style={{
            background: "#fff",
            padding: "36px 48px",
            borderRadius: "20px",
            boxShadow: "0 10px 36px rgba(102,126,234,0.18)",
            display: "flex",
            flexDirection: "column",
            gap: "22px",
            minWidth: "340px",
            animation: "pop 0.7s cubic-bezier(.68,-0.55,.27,1.55)",
            zIndex: 2,
            position: "relative",
          }}
        >
          <input
            name="name"
            placeholder="Name"
            value={form.name}
            onChange={handleChange}
            required
            style={{
              padding: "12px 16px",
              border: "1.5px solid #b4c5e4",
              borderRadius: "8px",
              fontSize: "1.05rem",
              outline: "none",
              transition: "border 0.2s, box-shadow 0.2s",
              boxShadow: "0 2px 8px rgba(102,126,234,0.06)",
            }}
          />
          <input
            name="email"
            type="email"
            placeholder="Email"
            value={form.email}
            onChange={handleChange}
            required
            style={{
              padding: "12px 16px",
              border: "1.5px solid #b4c5e4",
              borderRadius: "8px",
              fontSize: "1.05rem",
              outline: "none",
              transition: "border 0.2s, box-shadow 0.2s",
              boxShadow: "0 2px 8px rgba(102,126,234,0.06)",
            }}
          />
          <input
            name="event"
            placeholder="Event"
            value={form.event}
            onChange={handleChange}
            required
            style={{
              padding: "12px 16px",
              border: "1.5px solid #b4c5e4",
              borderRadius: "8px",
              fontSize: "1.05rem",
              outline: "none",
              transition: "border 0.2s, box-shadow 0.2s",
              boxShadow: "0 2px 8px rgba(102,126,234,0.06)",
            }}
          />
          <input
            name="date"
            type="date"
            value={form.date}
            onChange={handleChange}
            required
            style={{
              padding: "12px 16px",
              border: "1.5px solid #b4c5e4",
              borderRadius: "8px",
              fontSize: "1.05rem",
              outline: "none",
              transition: "border 0.2s, box-shadow 0.2s",
              boxShadow: "0 2px 8px rgba(102,126,234,0.06)",
            }}
          />
          <button
            type="submit"
            style={{
              padding: "14px 0",
              background: "linear-gradient(90deg, #43cea2 0%, #185a9d 100%)",
              color: "#fff",
              border: "none",
              borderRadius: "10px",
              fontSize: "1.15rem",
              cursor: "pointer",
              marginTop: "12px",
              boxShadow: "0 3px 12px rgba(67,206,162,0.16)",
              transition: "background 0.3s, transform 0.2s",
              animation: "pop 0.7s cubic-bezier(.68,-0.55,.27,1.55)",
              position: "relative",
              overflow: "hidden",
            }}
            onMouseOver={(e) =>
              (e.currentTarget.style.transform = "scale(1.05)")
            }
            onMouseOut={(e) => (e.currentTarget.style.transform = "scale(1)")}
          >
            <span
              style={{
                position: "absolute",
                top: 0,
                left: 0,
                right: 0,
                bottom: 0,
                background:
                  "linear-gradient(120deg, rgba(255,255,255,0.18) 30%, rgba(255,255,255,0.05) 70%)",
                backgroundSize: "200px 100%",
                backgroundRepeat: "no-repeat",
                animation: "shine 2.5s linear infinite",
                zIndex: 1,
                pointerEvents: "none",
                borderRadius: "10px",
              }}
            />
            <span style={{ position: "relative", zIndex: 2 }}>Submit</span>
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
