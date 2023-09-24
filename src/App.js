import React, { lazy } from "react";
import { Route, Routes } from "react-router-dom";
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
          <Route path="*" element={<Layout />} />
        </Route>
        <Route path="*" element={token ? "/" : "/login"} />
      </Routes>
    </div>
  );
}

export default App;
