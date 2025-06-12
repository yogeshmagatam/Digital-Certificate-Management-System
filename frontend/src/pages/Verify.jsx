import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import { QRCodeSVG } from "qrcode.react";
import "../Verify.css"; 

const Verify = () => {
  const { certificateId } = useParams();
  const [data, setData] = useState(null);

  useEffect(() => {
    axios
      .get(`/api/verify/${certificateId}`)
      .then((res) => setData(res.data))
      .catch((err) => console.error(err));
  }, [certificateId]);

  return (
    <div className="verify-container">
      {data ? (
        <div className="verify-card">
          <h2 className="verify-title">{data.studentName}</h2>
          <p>Issued on: {data.issueDate}</p>
          <p>Course: {data.course}</p>
          <p className={`verify-status${data.valid ? "" : " invalid"}`}>
            {data.valid ? "✅ Verified" : "❌ Invalid"}
          </p>
          <div className="verify-qr">
            <QRCodeSVG value={window.location.href} />
          </div>
        </div>
      ) : (
        <p>Loading certificate...</p>
      )}
    </div>
  );
};

export default Verify;
