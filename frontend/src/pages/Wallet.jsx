import React, { useEffect, useState } from "react";
import axios from "axios";
import CertificateCard from "../components/CertificateCard";

const Wallet = () => {
  const [certificates, setCertificates] = useState([]);

  useEffect(() => {
    axios
      .get("/api/my-certificates")
      .then((res) => setCertificates(res.data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold mb-4">My Certificates</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {certificates.map((cert) => (
          <CertificateCard key={cert._id} cert={cert} />
        ))}
      </div>
    </div>
  );
};

export default Wallet;
