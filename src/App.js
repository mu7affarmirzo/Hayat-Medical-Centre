import React, { lazy } from "react";
import {
  Navigate,
  Route,
  Routes,
} from "react-router-dom";
import "./App.css";
import Login from "./pages/Login/Login";
import ProtectedRoutes from "./Routes/ProtectedRoutes";

const Layout = lazy(() => import("./Layouts/Layout"));
const accessToken = localStorage.getItem("access-token");
function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route element={<ProtectedRoutes />}>
          <Route path={`/*`} element={<Layout />} />
        </Route>
        <Route
          path="/"
          element={<Navigate to={accessToken ? "reception" : "login"} replace />}
        />
      </Routes>
    </div>
  );
}

export default App;
