import React from 'react';
import { Navigate } from 'react-router-dom';

const PrivateRoute = ({ children }) => {
  const isAuthenticated = localStorage.getItem('token'); // Check if token exists
  console.log('PrivateRoute: isAuthenticated', isAuthenticated);
  
  return isAuthenticated ? children : <Navigate to="/" replace />;
};

export default PrivateRoute; 