import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import { QRCodeSVG } from "qrcode.react";

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
    <div className="p-8">
      {data ? (
        <div className="bg-white shadow-lg rounded-lg p-6">
          <h2 className="text-xl font-bold mb-2">{data.studentName}</h2>
          <p>Issued on: {data.issueDate}</p>
          <p>Course: {data.course}</p>
          <p>Status: {data.valid ? "✅ Verified" : "❌ Invalid"}</p>
          <QRCodeSVG value={window.location.href} className="mt-4" />
        </div>
      ) : (
        <p>Loading certificate...</p>
      )}
    </div>
  );
};

export default Verify;
