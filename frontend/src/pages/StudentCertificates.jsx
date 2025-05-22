import React, { useEffect, useState } from "react";

const StudentCertificates = () => {
  const [certificates, setCertificates] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("http://localhost:5000/api/certificates/student/cert", {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    })
      .then((res) => {
        if (!res.ok) {
          throw new Error("Network response was not ok");
        }
        return res.json();
      })
      .then((data) => {
        setCertificates(data.certificates || []);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Failed to fetch certificates:", err);
        setLoading(false);
      });
  }, []);

  if (loading) return <div>Loading certificates...</div>;

  return (
    <div>
      <h2>Your Certificates</h2>
      {certificates.length === 0 ? (
        <p>No certificates found.</p>
      ) : (
        <ul>
          {certificates.map((cert) => (
            <li key={cert._id}>
              {cert.name} - {cert.event} - {cert.date}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default StudentCertificates;
