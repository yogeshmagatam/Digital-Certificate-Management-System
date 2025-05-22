import React from "react";
import { useNavigate } from "react-router-dom";

const LogoutButton = ({ className = "", style = {} }) => {
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.clear();
    navigate("/login");
  };

  return (
    <button
      className={`logout-top-right ${className}`}
      style={style}
      onClick={handleLogout}
    >
      Logout
    </button>
  );
};

export default LogoutButton;
