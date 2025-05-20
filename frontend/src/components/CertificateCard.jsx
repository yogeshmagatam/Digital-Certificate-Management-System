import React from "react";
import { Link } from "react-router-dom";

const CertificateCard = ({ cert }) => (
  <div className="border p-4 rounded shadow-md bg-white">
    <h3 className="text-lg font-semibold">{cert.title}</h3>
    <p>Issued: {cert.issueDate}</p>
    <p>Institution: {cert.institution}</p>
    <Link
      to={`/verify/${cert._id}`}
      className="text-blue-500 mt-2 inline-block"
    >
      Verify
    </Link>
  </div>
);

export default CertificateCard;
