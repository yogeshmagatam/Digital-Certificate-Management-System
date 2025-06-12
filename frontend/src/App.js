import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import AppRoutes from "./routes";

function App() {
  const navigate = useNavigate();

  useEffect(() => {
    const handlePageShow = (event) => {
      if (event.persisted) {
        // Page was restored from bfcache
        const token = localStorage.getItem('token');
        if (!token) {
          navigate("/", { replace: true });
        }
      }
    };

    window.addEventListener('pageshow', handlePageShow);

    return () => {
      window.removeEventListener('pageshow', handlePageShow);
    };
  }, [navigate]);

  return <AppRoutes />;
}

export default App;
