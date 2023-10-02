import React, { lazy } from "react";
import {
  Navigate,
  Route,
  Routes,
  useLocation,
  useNavigate,
} from "react-router-dom";
import "./App.css";
import Login from "./pages/Login/Login";
import ProtectedRoutes from "./Routes/ProtectedRoutes";

const Layout = lazy(() => import("./Layouts/Layout"));
const token = localStorage.getItem("token");
function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route element={<ProtectedRoutes />}>
          <Route path={`*`} element={<Layout />} />
        </Route>
        <Route
          path="*"
          element={<Navigate to={token ? "/reception" : "/login"} replace />}
        />
      </Routes>
    </div>
  );
}

export default App;
