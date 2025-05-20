import React, { useEffect, useState } from "react";
import axios from "axios";
import CertificateCard from "../components/CertificateCard";
import "../Wallet.css"; // Import the CSS file

const Wallet = () => {
  const [certificates, setCertificates] = useState([]);

  useEffect(() => {
    axios
      .get("/api/my-certificates")
      .then((res) => setCertificates(res.data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div className="wallet-container">
      <h2 className="wallet-title">My Certificates</h2>
      <div className="wallet-grid">
        {certificates.map((cert) => (
          <CertificateCard key={cert._id} cert={cert} />
        ))}
      </div>
    </div>
  );
};

export default Wallet;
